from sqlmodel import SQLModel, Field,Relationship
from typing import Optional

class User(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    full_name:str
    email:str
    phone_no:str
    stores : list["Store"] = Relationship(back_populates="user")

class Store(SQLModel,table=True):
    id:Optional[int] = Field(primary_key=True,default=None)
    photo:str
    title:str
    description:str
    price:float

    user_id:int = Field(foreign_key="user.id")
    user : list["User"] = Relationship(back_populates="stores")

class OrderSwag(SQLModel,table=True):
    id:Optional[int] = Field(primary_key=True,default=None)
    name:str
    phone:str
    email:str
    address:str
    payment_type:str
    user_id:int = Field(foreign_key="user.id")
    user : list["User"] = Relationship(back_populates="orders")

    store_id:int = Field(foreign_key="store.id")
    store : list["Store"] = Relationship(back_populates="orders")
