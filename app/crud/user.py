from sqlalchemy.orm import Session

from app.auth import get_password_hash
from app.data_types.user import UserCreate
from app.db_models.user import User


def create_user(db: Session, user: UserCreate):
    hashed = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
