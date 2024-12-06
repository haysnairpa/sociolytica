from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.analytics import SentimentAnalysis
from app.schemas.analytics import SentimentAnalysisCreate, SentimentAnalysis as SentimentAnalysisSchema

router = APIRouter()

@router.post("/analyze", response_model=SentimentAnalysisSchema)
def analyze_sentiment(analysis: SentimentAnalysisCreate, db: Session = Depends(get_db)):
    db_analysis = SentimentAnalysis(**analysis.dict())
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

@router.get("/history/{platform}", response_model=List[SentimentAnalysisSchema])
def get_sentiment_history(platform: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    analyses = db.query(SentimentAnalysis)\
        .filter(SentimentAnalysis.platform == platform)\
        .order_by(SentimentAnalysis.created_at.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()
    return analyses
