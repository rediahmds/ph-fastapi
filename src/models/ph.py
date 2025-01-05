from sqlalchemy import Column, Integer, Float, String
from src.databases.db import Base


class PhModel(Base):
    __tablename__ = "ph"

    id = Column(Integer, primary_key=True)
    ph = Column(Float)
    result = Column(String)


# meta = MetaData()
# ph_table = Table(PhModel.__tablename__, meta, PhModel.id, PhModel.ph, PhModel.result)

# meta.create_all(bind=engine)
