from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any, List

class HashtagBase(BaseModel):
    tag: str
    count: int = 0

class HashtagCreate(HashtagBase):
    pass

class Hashtag(HashtagBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class SentimentAnalysisBase(BaseModel):
    content_id: str
    platform: str
    sentiment_score: float
    sentiment_magnitude: float
    analysis_data: Dict[str, Any]

class SentimentAnalysisCreate(SentimentAnalysisBase):
    pass

class SentimentAnalysis(SentimentAnalysisBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class NetworkAnalysisBase(BaseModel):
    platform: str = Field(..., description="Social media platform (e.g., Twitter, LinkedIn)")
    connections_count: int = Field(..., ge=0, description="Number of connections/followers")
    influence_score: float = Field(..., ge=0, le=1, description="Influence score between 0 and 1")
    community_data: Dict[str, Any] = Field(default_factory=dict, description="JSON data about communities")

class NetworkAnalysisCreate(NetworkAnalysisBase):
    pass

class NetworkAnalysis(NetworkAnalysisBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class NetworkAnalysisResponse(BaseModel):
    status: str
    data: NetworkAnalysis
    message: str

class NetworkMetrics(BaseModel):
    user_id: int
    platform: Optional[str]
    total_connections: int = Field(..., ge=0)
    average_influence_score: float = Field(..., ge=0, le=1)
    analysis_count: int = Field(..., ge=0)
    last_updated: datetime

class EngagementMetricsBase(BaseModel):
    content_id: str
    platform: str
    likes: int = Field(default=0, ge=0)
    shares: int = Field(default=0, ge=0)
    comments: int = Field(default=0, ge=0)
    engagement_rate: float = Field(..., ge=0)

class EngagementMetricsCreate(EngagementMetricsBase):
    pass

class EngagementMetrics(EngagementMetricsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
