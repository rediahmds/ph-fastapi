from fastapi import Depends, APIRouter
from src.schemas.ph import PhSchema
from src.models.ph import PhModel
from sqlalchemy.orm import Session
from src.databases.connection_manager import get_db

router = APIRouter()


@router.get("/ph-latest")
async def get_latest(limit: int = 20, db: Session = Depends(get_db)):
    latest_list = (
        db.query(PhModel).order_by(PhModel.created_at.desc()).limit(limit).all()
    )
    return latest_list


@router.post("/ph", status_code=201)
async def create_ph(request: PhSchema, db: Session = Depends(get_db)):
    by_esp = PhModel(ph=request.ph, result=request.result)
    db.add(by_esp)
    db.commit()
    db.refresh(by_esp)

    return by_esp


@router.get("/ph")
async def get_all_phs(db: Session = Depends(get_db)):
    phs = db.query(PhModel).all()
    return phs


@router.get("/ph/{id}")
async def get_ph_by_id(id: int, db: Session = Depends(get_db)):
    ph = db.query(PhModel).filter(PhModel.id == id).first()
    return ph


@router.put("/ph/{id}")
async def update_ph(id: int, request: PhSchema, db: Session = Depends(get_db)):
    current_ph = db.query(PhModel).filter(PhModel.id == id).first()
    current_ph.ph = request.ph
    current_ph.result = request.result
    db.commit()
    db.refresh(current_ph)

    return current_ph


@router.delete("/ph/{id}")
async def delete_ph(id: int, db: Session = Depends(get_db)):
    ph = db.query(PhModel).filter(PhModel.id == id)
    ph.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Ph with id {id} has been deleted successfully."}
