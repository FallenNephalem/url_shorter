from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from dto import UrlCreate
from models import Url, init_db, get_db
from settings import get_settings
from sqlalchemy.exc import IntegrityError


app = FastAPI()


@app.on_event('startup')
def startup():
    return init_db()


@app.post('/create-url/')
def create_short_link(url: UrlCreate, db: Session = Depends(get_db)) -> UrlCreate:
    print('--' * 10)
    print('--' * 10)
    print('--' * 10)
    print('--' * 10)
    print('--' * 10)
    try:
        db_item = Url(**url.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail='Database error')
    print(url)
    print(url)
    print(url)
    print(url)
    print(url)
    print(url)
    print(url)
    return url


@app.delete('/{short}')
def delete_short_link(short: str, db: Session = Depends(get_db)):
    url = db.query(Url).get(short)
    if url is None:
        raise HTTPException(status_code=404, detail='Item not found')
    try:
        db.delete(url)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail='Database error')


@app.get('/{short}')
def redirect(short: str, db: Session = Depends(get_db)) -> RedirectResponse:
    return RedirectResponse(url=db.query(Url).get(short).url)
