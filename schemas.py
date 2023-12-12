from pydantic import BaseModel, EmailStr, Field


class Owner(BaseModel):
    fullname: str
    email: EmailStr

class OwnerResponse(Owner):
    id: int = 1


    class Config:
        from_attributes = True