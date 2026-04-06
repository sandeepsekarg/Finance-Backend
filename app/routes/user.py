from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.middleware.role import require_role
from fastapi import Depends

router = APIRouter()

# Create User
@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db), role: str = Depends(require_role(["admin"]))):
    db_user = User(
        name=user.name,
        email=user.email,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Get All Users
@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), role: str = Depends(require_role(["admin"]))):
    return db.query(User).all()


# Update User
@router.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db), role: str = Depends(require_role(["admin"]))):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.role:
        db_user.role = user.role
    if user.status:
        db_user.status = user.status

    db.commit()
    db.refresh(db_user)
    return db_user