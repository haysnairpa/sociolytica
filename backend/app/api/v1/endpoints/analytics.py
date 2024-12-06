from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.analytics import NetworkAnalysis
from app.schemas.analytics import NetworkAnalysisCreate, NetworkAnalysis as NetworkAnalysisSchema

router = APIRouter()

@router.post("/network", response_model=NetworkAnalysisSchema)
def create_network_analysis(analysis: NetworkAnalysisCreate, db: Session = Depends(get_db)):
    db_analysis = NetworkAnalysis(**analysis.dict())
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

@router.get("/network/{user_id}", response_model=List[NetworkAnalysisSchema])
def get_user_network_analysis(user_id: int, db: Session = Depends(get_db)):
    analyses = db.query(NetworkAnalysis)\
        .filter(NetworkAnalysis.user_id == user_id)\
        .order_by(NetworkAnalysis.created_at.desc())\
        .all()
    return analyses
