from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found with user_id: {user_id}")
    return user

@router.post("/", response_model=User, status_code=201)
def create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    user = User.model_validate(user_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserUpdate, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found with user_id: {user_id}")
    user.sqlmodel_update(user_data.model_dump(exclude_unset=True))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found with user_id: {user_id}")
    session.delete(user)
    session.commit()
