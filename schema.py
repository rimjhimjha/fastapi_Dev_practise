from enum import Enum
from pydantic import BaseModel,Field
from datetime import date

class GeneralURLChoice(str,Enum):
    rocks ='rock'
    electronics ='electronics'
    metal = 'metal'
    hip_hop = 'hip-hop'

class Album (BaseModel):
    title: str
    release_date : date
    

class Band (BaseModel):
    name: str
    genre : str
    albums : list[Album] = Field(default_factory=list)

class BandCreate (Band):
    pass


class BandwithID(Band):
    id:int



