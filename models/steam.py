from typing import Optional
from pydantic import BaseModel

class SteamDatesForGithub(BaseModel):
    id: Optional[str] 
    url: str
    name: str
    categories: str
    img_url: str
    price: str
    
class SteamDatesForComplementary(BaseModel):
    id: Optional[str]
    idSteamDatesForGithub: str
    user_reviews: str
    all_reviews: str
    date: str
    developer: str
    publisher: str
    pegi: str
    pegi_url: str