from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import authenticate_user, create_access_token, get_current_user
from app.crud.expense import get_expenses, store_expense
from app.crud.user import create_user
from app.data_types.expense import Expense, ExpenseCreate
from app.data_types.user import Token, User, UserCreate
from app.database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(db, user)


@app.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(SessionLocal),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/expenses/", response_model=Expense)
def create_expense(
    expense: ExpenseCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(SessionLocal),
):
    return store_expense(db, expense, user_id=current_user.id)


@app.get("/expenses/", response_model=list[Expense])
def read_expenses(
    current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)
):
    return get_expenses(db, user_id=current_user.id)
