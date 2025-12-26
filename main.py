from fastapi import FastAPI,HTTPException,Path,Depends
from models import GeneralURLChoice, BandBase, BandCreate,Band,Album
from typing import Annotated
from contextlib import asynccontextmanager
from db import init_db, get_session
from sqlmodel import Session

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan= lifespan)




#band is a list of dictionaries
BANDS = [
    {'id': 1, 'name': 'The Kinkss', 'genre': 'rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'electronics'},
    {'id': 3, 'name': 'Slow Dive', 'genre': 'metal'},
    {
        'id': 4,
        'name': 'Wu-Tang',
        'genre': 'hip-hop',
        'albums': [
            {'title': 'Master of Reality', 'release_date': '1972-09-21'}
        ]
    },
]

'''@app.get("/")
async def index() -> dict[str,int]:
    return {'hello':123}
'''

'''@app.get("/about")
async def about()-> str:
    return 'An exceptional Company.'
'''

'''# return all bands
@app.get('/bands')
async def get_bands() ->list[dict]:
    return BANDS
'''

#return single band by id number

'''@app.get("/bands/{band_id}")
def get_band(band_id: int):
    for band in BANDS:
        if band["id"] == band_id:
            return band

    raise HTTPException(
        status_code=404,
        detail="Band not found"
    
    )
'''

'''@app.get("/bands/{band_id}",response_model=Band)
def get_band(band_id: int):
    for band in BANDS:
        if band["id"] == band_id:
            return band

    raise HTTPException(
        status_code=404,
        detail="Band not found"
    
    )
    '''

''' @app.get('/band/genre/{genre}')
async def bands_for_genre( genre: GeneralURLChoice) -> list[dict]:
    result =[]
    for band in BANDS:
        if band['genre'] ==  genre.value:
            result.append(band)
    if not result:
        raise HTTPException(status_code=404, detail="no band found")

    return result
'''

'''@app.get('/bands')
async def bands()->list[Band]:
    return [Band(**b) for b in BANDS]
'''
'''
#query parameter
@app.get('/bands')
async def bands( genre: GeneralURLChoice | None= None)->list[BandBase]:
    if genre is None:
        return BANDS
    result =[
        band for band in BANDS
        if band['genre'] ==  genre.value
    ]
    if not result:
        raise HTTPException(status_code=404, detail= "No band found")
    return result
'''
'''
@app.post('/bands')
async def create_band(band_data: BandCreate)-> Band:
    id= BANDS[-1]['id']+1
    newband= BandwithID(id = id, **band_data.model_dump()).model_dump()
    BANDS.append(newband)
    return newband

'''
'''
#annotated data
@app.get("/bands/{band_id}",response_model=BandBase)
def get_band(band_id: Annotated[int,Path (title="The band ID")]):
    for band in BANDS:
        if band["id"] == band_id:
            return band

    raise HTTPException(
        status_code=404,
        detail="Band not found"
    
    )
        
   ''' 

#database

@app.post("/bands", response_model=Band)
def create_band(
    band_data: BandCreate,
    session: Session = Depends(get_session)
) -> Band:
    band = Band(
        name=band_data.name,
        genre=band_data.genre
    )
    session.add(band)

    if band_data.albums:
        for album in band_data.albums:
            album_obj = Album(title= album.title, release_date =album.release_date, band=band )
            session.add()

    session.commit()
    session.refresh(band)
    return band