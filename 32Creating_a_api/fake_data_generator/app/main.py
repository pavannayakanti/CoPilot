# I would like to create a web API that uses REST
# I would like to create a web api in python with my ezxisting file. I would like to accept REST commands.
# which is the best python framework for building a web api? list the pros and cons.
# JSON based on parameters in that post.
from fastapi import FastAPI
from app.routes.fake_data import router

# Initialize the FastAPI app
app = FastAPI(
	title="Fake Data Generator API",
	description="An API to generate fake data",
	version="1.0.0"
)

# Include the routes
app.include_router(router)

# Add a root route
@app.get("/", summary="Root Endpoint", tags=["Root"])
def read_root():
	"""
	Root endpoint to provide basic information about the API.
	"""
	return {"message": "Hello World!! Welcome to the Fake Data Generator API!"}

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="127.0.0.1", port=8000)