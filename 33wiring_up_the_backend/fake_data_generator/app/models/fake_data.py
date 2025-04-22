from pydantic import BaseModel
from typing import Optional

class FakeData(BaseModel):
	Name: Optional[str]
	Gender: Optional[str]
	Email: Optional[str]
	Address: Optional[str]
	Phone_Number: Optional[str]
	Job: Optional[str]
	Company: Optional[int]
	field8: Optional[str]
	field9: Optional[str]
	field10: Optional[str]