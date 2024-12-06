from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.analytics import EngagementMetrics
from app.schemas.analytics import EngagementMetricsCreate, EngagementMetrics as EngagementMetricsSchema

router = APIRouter()

@router.post("/metrics", response_model=EngagementMetricsSchema)
def create_engagement_metrics(metrics: EngagementMetricsCreate, db: Session = Depends(get_db)):
    db_metrics = EngagementMetrics(**metrics.dict())
    db.add(db_metrics)
    db.commit()
    db.refresh(db_metrics)
    return db_metrics

@router.get("/metrics/{platform}", response_model=List[EngagementMetricsSchema])
def get_engagement_metrics(platform: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = db.query(EngagementMetrics)\
        .filter(EngagementMetrics.platform == platform)\
        .order_by(EngagementMetrics.engagement_rate.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()
    return metrics
