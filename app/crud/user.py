from sqlalchemy.orm import Session

from app.auth import get_password_hash
from app.data_types.expense import ExpenseCreate
from app.data_types.user import UserCreate
from app.db_models.expense import Expense
from app.db_models.user import User


def create_user(db: Session, user: UserCreate):
    hashed = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_expense(db: Session, expense: ExpenseCreate, user_id: int):
    db_exp = Expense(**expense.dict(), user_id=user_id)
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp
