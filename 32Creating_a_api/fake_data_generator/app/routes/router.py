from fastapi import APIRouter
from pydantic import BaseModel
from app.services import FakeDataGenerator

# Initialize the router
router = APIRouter()

# Define the request body model
class FakeDataRequest(BaseModel):
	name: str
	age: int
	city: str

# Define the /getfakedata route
@router.post("/getfakedata")
async def get_fake_data(request: FakeDataRequest):
	generator = FakeDataGenerator()
	fake_data = generator.generate_fake_data()
	return {
		"message": f"Hello {request.name}, aged {request.age}, from {request.city}!",
		"status": "success",
		"data": fake_data
	}