from pydantic import BaseModel

class item(BaseModel):
    """Товар."""
    id: int
    name: str
    category: str
    price: int
    currency: str
    count: int

    def __str__(self):
        return f'"name": {self.name}, "category": {self.category}, "price": {self.price}, "currency": {self.currency}, "count": {self.count}'