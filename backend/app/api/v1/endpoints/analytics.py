from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.db.session import get_db
from app.models.analytics import NetworkAnalysis, EngagementMetrics
from app.schemas.analytics import (
    NetworkAnalysisCreate,
    NetworkAnalysis as NetworkAnalysisSchema,
    NetworkAnalysisResponse,
    NetworkMetrics
)
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/network", response_model=NetworkAnalysisResponse)
async def create_network_analysis(
    analysis: NetworkAnalysisCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        # Validate user permissions
        if not current_user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")

        # Create network analysis
        db_analysis = NetworkAnalysis(
            **analysis.dict(),
            user_id=current_user.id
        )
        db.add(db_analysis)
        db.commit()
        db.refresh(db_analysis)
        
        return {
            "status": "success",
            "data": db_analysis,
            "message": "Network analysis created successfully"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/network/{user_id}", response_model=List[NetworkAnalysisSchema])
async def get_user_network_analysis(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    platform: Optional[str] = None
):
    try:
        # Check if user has permission to view the data
        if current_user.id != user_id and not current_user.is_superuser:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to access this user's data"
            )

        # Build query
        query = db.query(NetworkAnalysis).filter(NetworkAnalysis.user_id == user_id)
        
        # Apply platform filter if specified
        if platform:
            query = query.filter(NetworkAnalysis.platform == platform)
        
        # Apply pagination
        analyses = query.offset(skip).limit(limit).all()
        
        if not analyses:
            raise HTTPException(status_code=404, detail="No network analyses found")
            
        return analyses
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/network/{user_id}/metrics", response_model=NetworkMetrics)
async def get_network_metrics(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    platform: Optional[str] = None
):
    try:
        # Check permissions
        if current_user.id != user_id and not current_user.is_superuser:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to access this user's data"
            )

        # Build base query
        query = db.query(NetworkAnalysis).filter(NetworkAnalysis.user_id == user_id)
        
        if platform:
            query = query.filter(NetworkAnalysis.platform == platform)
            
        analyses = query.all()
        
        if not analyses:
            raise HTTPException(status_code=404, detail="No network analyses found")
            
        # Calculate metrics
        avg_influence = sum(a.influence_score for a in analyses) / len(analyses)
        total_connections = sum(a.connections_count for a in analyses)
        
        return {
            "user_id": user_id,
            "platform": platform,
            "total_connections": total_connections,
            "average_influence_score": avg_influence,
            "analysis_count": len(analyses),
            "last_updated": datetime.utcnow()
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/network/{analysis_id}")
async def delete_network_analysis(
    analysis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        analysis = db.query(NetworkAnalysis).filter(NetworkAnalysis.id == analysis_id).first()
        
        if not analysis:
            raise HTTPException(status_code=404, detail="Network analysis not found")
            
        if analysis.user_id != current_user.id and not current_user.is_superuser:
            raise HTTPException(status_code=403, detail="Not authorized to delete this analysis")
            
        db.delete(analysis)
        db.commit()
        
        return {"status": "success", "message": "Network analysis deleted successfully"}
    except HTTPException as he:
        raise he
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
