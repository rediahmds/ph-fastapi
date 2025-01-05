from pydantic import BaseModel


class PhSchema(BaseModel):
    ph: float
    result: str
