from sqlalchemy.orm import Session

from app.db_models.expense import Expense


def get_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()
