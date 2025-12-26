from enum import Enum
from pydantic import BaseModel,Field
from datetime import date
from sqlmodel import SQLModel,Field, Relationship

class GeneralURLChoice(str,Enum):
    rocks ='rock'
    electronics ='electronics'
    metal = 'metal'
    hip_hop = 'hip-hop'

class BandBase (SQLModel):
    name: str
    genre : str

class AlbumBase (SQLModel):
    title: str
    release_date : date
    band_id :int = Field(foreign_key="band.id")


class Album(AlbumBase, table = True):
    id: int = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")
    
class Band(BandBase, table=True):
    id: int= Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")


    

class BandCreate (BandBase):
    albums : list[AlbumBase] = []


class BandwithID(BandBase, table = True):
    id:int = Field(default=None, primary_key=True)




