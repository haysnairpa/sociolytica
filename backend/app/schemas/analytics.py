from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

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
    user_id: int
    platform: str
    connections_count: int
    influence_score: float
    community_data: Dict[str, Any]

class NetworkAnalysisCreate(NetworkAnalysisBase):
    pass

class NetworkAnalysis(NetworkAnalysisBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class EngagementMetricsBase(BaseModel):
    content_id: str
    platform: str
    likes: int = 0
    shares: int = 0
    comments: int = 0
    engagement_rate: float

class EngagementMetricsCreate(EngagementMetricsBase):
    pass

class EngagementMetrics(EngagementMetricsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
