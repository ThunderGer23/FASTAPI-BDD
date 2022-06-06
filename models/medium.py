from typing import Optional
from pydantic import BaseModel

class MediumDatesForRepo(BaseModel):
    id: Optional[str]
    idMediumText: str
    title: str
    url: str
    authors: str
    timestamp: str

class MediumText(BaseModel):
    id: Optional[str]
    text: str
    tags: str

