from pydantic import BaseModel

class User(BaseModel):
    full_name:str
    email:str
    phone_no:str
    

class UserCreate(User):
    pass


class Store(BaseModel):
    id:int
    photo:str
    title:str
    description:str
    price:float

class StoreCreate(BaseModel):
    photo:str
    title:str
    description:str
    price:float

class StoreRead(Store):
    pass
