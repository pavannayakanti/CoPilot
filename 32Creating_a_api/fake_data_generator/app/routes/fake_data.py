from fastapi import APIRouter
from app.models.fake_data import FakeDataRequest
from app.services import FakeDataGenerator

router = APIRouter()

@router.post("/getfakedata")
async def get_fake_data(request: FakeDataRequest):
	generator = FakeDataGenerator()
	fake_data = generator.generate_fake_data()
	return {
		"message": f"Hello {request.name}, aged {request.age}, from {request.city}!",
		"status": "success",
		"data": fake_data
	}