from fastapi import APIRouter, Depends, HTTPException, status,Response
from models import Store
from db import get_session
from sqlmodel import Session, select
from schemas import StoreRead, StoreCreate

router = APIRouter(tags=["Admin"])


@router.get("/swag", response_model=list[StoreRead])
async def swag(session: Session = Depends(get_session)):
    res = select(Store)
    result = session.exec(res).all()
    if not result:
        raise HTTPException(status_code=404, detail="No swag found")
    return result


@router.post("/swag", response_model=StoreRead)
async def create_swag(swag: StoreCreate, session: Session = Depends(get_session)):
    swag = Store.from_orm(swag)
    session.add(swag)
    session.commit()
    session.refresh(swag)
    return swag


@router.get("/swag/{id}", response_model=StoreRead)
async def get_id(id: int, session: Session = Depends(get_session)):
    swag_id = session.get(Store, id)
    if not swag_id:
        raise HTTPException(status_code=404, detail="No swag found")
    return swag_id


@router.delete("/swag/{id}", response_model=StoreRead)
async def delete_swag(id: int, session: Session = Depends(get_session)):
    swag_id = session.get(Store, id)
    if not swag_id:
        raise HTTPException(status_code=404, detail="No swag found")
    session.delete(swag_id)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
