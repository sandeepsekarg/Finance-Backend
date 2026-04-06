from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import get_db
from app.models.record import FinancialRecord
from app.schemas.record import RecordCreate, RecordResponse, RecordUpdate
from app.middleware.role import require_role

router = APIRouter()


# Create Record
@router.post("/records", response_model=RecordResponse)
def create_record(record: RecordCreate, db: Session = Depends(get_db), role: str = Depends(require_role(["admin"]))):
    db_record = FinancialRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


# Get Records with Filters
@router.get("/records", response_model=list[RecordResponse])
def get_records(
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    role: str = Depends(require_role(["admin", "analyst"]))
):
    query = db.query(FinancialRecord)

    if type:
        query = query.filter(FinancialRecord.type == type)
    if category:
        query = query.filter(FinancialRecord.category == category)
    if date:
        query = query.filter(FinancialRecord.date == date)

    return query.all()


# Update Record
@router.put("/records/{record_id}", response_model=RecordResponse)
def update_record(record_id: int, record: RecordUpdate, db: Session = Depends(get_db), role: str = Depends(require_role(["admin"]))):
    db_record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()

    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")

    for key, value in record.dict(exclude_unset=True).items():
        setattr(db_record, key, value)

    db.commit()
    db.refresh(db_record)
    return db_record


# Delete Record
@router.delete("/records/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db), role: str = Depends(require_role(["admin"]))):
    db_record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()

    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(db_record)
    db.commit()
    return {"message": "Record deleted successfully"}