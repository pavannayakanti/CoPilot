from pydantic import BaseModel

class FakeDataRequest(BaseModel):
	name: str
	age: int
	city: str