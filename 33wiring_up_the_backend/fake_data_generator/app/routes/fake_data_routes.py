from fastapi import APIRouter
from app.services.fake_data_generator import FakeDataGenerator
from app.models.fake_data_request import FakeDataRequest
from pydantic import BaseModel

# Initialize the FastAPI router
router = APIRouter()

# Endpoint for fetching all fake data
@router.post("/api/v1/getfakedata")
async def get_fake_data(request: FakeDataRequest) -> dict:
	# Create an instance of FakeDataGenerator
	generator = FakeDataGenerator()
	# Generate fake data without any specific count
	fake_data = generator.generate_fake_data()
	# Return the generated fake data in a success response
	return {
		"status": "success",
		"data": fake_data
	}

# Pydantic model for the request body to fetch fake data by count
class FakeDataByCountRequest(BaseModel):
	count: int  # Number of fake data items to generate

# Endpoint for fetching fake data by a specified count
@router.post("/api/v1/getfakedata/bycount")
async def get_fake_data_by_count(request: FakeDataByCountRequest):
	# Create an instance of FakeDataGenerator
	generator = FakeDataGenerator()
	# Generate fake data based on the count provided in the request
	fake_data = generator.generate_fake_data(request.count)
	# Return the generated fake data in a success response
	return {
		"status": "success",
		"data": fake_data
	}

# Export the router to be included in the main application
fake_data_router = router

