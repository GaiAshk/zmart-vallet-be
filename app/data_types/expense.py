from datetime import datetime

from pydantic import BaseModel


class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
