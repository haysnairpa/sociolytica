from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.analytics import Hashtag
from app.schemas.analytics import HashtagCreate, Hashtag as HashtagSchema

router = APIRouter()

@router.get("/trending", response_model=List[HashtagSchema])
def get_trending_hashtags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    hashtags = db.query(Hashtag).order_by(Hashtag.count.desc()).offset(skip).limit(limit).all()
    return hashtags

@router.post("/", response_model=HashtagSchema)
def create_hashtag(hashtag: HashtagCreate, db: Session = Depends(get_db)):
    db_hashtag = Hashtag(**hashtag.dict())
    db.add(db_hashtag)
    db.commit()
    db.refresh(db_hashtag)
    return db_hashtag

@router.get("/{tag}", response_model=HashtagSchema)
def get_hashtag(tag: str, db: Session = Depends(get_db)):
    hashtag = db.query(Hashtag).filter(Hashtag.tag == tag).first()
    if hashtag is None:
        raise HTTPException(status_code=404, detail="Hashtag not found")
    return hashtag
