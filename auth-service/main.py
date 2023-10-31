from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# Define endpoints for various microservices
@app.get("/user-service/{path:path}")
async def user_service_pass_through(path: str):
    # This endpoint passes the request to the user service
    return {"message": "User service pass-through", "path": path}

@app.get("/movie-service/{path:path}")
async def movie_service_pass_through(path: str):
    # This endpoint passes the request to the movie service
    print("came here")
    return {"message": "Movie service pass-through", "path": path}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
