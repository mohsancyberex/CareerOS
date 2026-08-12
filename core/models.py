from pydantic import BaseModel
from typing import Optional


class Job(BaseModel):
    source: str
    source_id: str
    title: str
    company: str
    location: Optional[str] = None
    url: str
    description: Optional[str] = None
    employment_type: Optional[str] = None
    remote: Optional[bool] = None
