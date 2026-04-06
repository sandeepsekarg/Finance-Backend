from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base

class FinancialRecord(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # income or expense
    category = Column(String)
    date = Column(Date)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))