from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.record import FinancialRecord

router = APIRouter(prefix="/summary")


# Total Income
@router.get("/total-income")
def total_income(db: Session = Depends(get_db)):
    total = db.query(func.sum(FinancialRecord.amount))\
        .filter(FinancialRecord.type == "income")\
        .scalar()
    
    return {"total_income": total or 0}


# Total Expense
@router.get("/total-expense")
def total_expense(db: Session = Depends(get_db)):
    total = db.query(func.sum(FinancialRecord.amount))\
        .filter(FinancialRecord.type == "expense")\
        .scalar()
    
    return {"total_expense": total or 0}


# Net Balance
@router.get("/net-balance")
def net_balance(db: Session = Depends(get_db)):
    income = db.query(func.sum(FinancialRecord.amount))\
        .filter(FinancialRecord.type == "income")\
        .scalar() or 0

    expense = db.query(func.sum(FinancialRecord.amount))\
        .filter(FinancialRecord.type == "expense")\
        .scalar() or 0

    return {"net_balance": income - expense}


# Category-wise Summary
@router.get("/category-wise")
def category_summary(db: Session = Depends(get_db)):
    results = db.query(
        FinancialRecord.category,
        func.sum(FinancialRecord.amount)
    ).group_by(FinancialRecord.category).all()

    return [
        {"category": r[0], "total": r[1]}
        for r in results
    ]