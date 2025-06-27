from sqlalchemy.orm import Session

from app.data_types.expense import ExpenseCreate
from app.db_models.expense import Expense


def get_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()


def store_expense(db: Session, expense: ExpenseCreate, user_id: int):
    db_exp = Expense(**expense.dict(), user_id=user_id)
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp
