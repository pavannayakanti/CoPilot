from fastapi import APIRouter
from app.services.fake_data_generator import FakeDataGenerator
from app.models.fake_data_request import FakeDataRequest
from pydantic import BaseModel

router = APIRouter()
@router.post("/getfakedata")
async def get_fake_data(request: FakeDataRequest) -> dict:
	generator = FakeDataGenerator()
	fake_data = generator.generate_fake_data()
	return {
		"status": "success",
		"data": fake_data
	}

class FakeDataByCountRequest(BaseModel):
	count: int

@router.post("/getfakedata/bycount")
async def get_fake_data_by_count(request: FakeDataByCountRequest):
	generator = FakeDataGenerator()  # Create an instance of FakeDataGenerator
	fake_data = generator.generate_fake_data(request.count)
	return {
		"status": "success",
		"data": fake_data
	}

# Export the router
fake_data_router = router

