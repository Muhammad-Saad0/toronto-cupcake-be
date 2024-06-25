import datetime
from typing import List, Literal
from pydantic import BaseModel

class Cupcake(BaseModel):
    id: int
    name: str
    description: str
    type: Literal["Always Available", "Holidays", "Special Events", "Custom"]
    price: float
    image: str
    
class Address(BaseModel):
    firstName: str
    lastName: str
    fullAddress: str
    phoneNumber: str
    email: str
    zipCode: str
    
class LineItem(BaseModel):
    item_id: int
    quantity: int
    
class CreateCheckoutSessionRequest(BaseModel):
    items: List[LineItem]
    address: Address