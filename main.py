from fastapi import FastAPI,HTTPException
from schema import  GeneralURLChoice, Band, BandCreate,BandwithID

app = FastAPI()




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

@app.get("/bands/{band_id}",response_model=Band)
def get_band(band_id: int):
    for band in BANDS:
        if band["id"] == band_id:
            return band

    raise HTTPException(
        status_code=404,
        detail="Band not found"
    
    )

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
#query parameter
@app.get('/bands')
async def bands( genre: GeneralURLChoice | None= None)->list[Band]:
    if genre is None:
        return BANDS
    result =[
        band for band in BANDS
        if band['genre'] ==  genre.value
    ]
    if not result:
        raise HTTPException(status_code=404, detail= "No band found")
    return result

@app.post('/bands')
async def create_band(band_data: BandCreate)-> BandwithID:
    id= BANDS[-1]['id']+1
    newband= BandwithID(id = id, **band_data.model_dump()).model_dump()
    BANDS.append(newband)
    return newband
        
    