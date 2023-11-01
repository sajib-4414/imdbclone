from fastapi import FastAPI, Response
import uvicorn
import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

# # # Define endpoints for various microservices
# # @app.get("/user-service/{path:path}")
# # async def user_service_pass_through(path: str):
# #     # This endpoint passes the request to the user service
# #     return {"message": "User service pass-through", "path": path}

# # @app.get("/movie-service/{path:path}")
# # async def movie_service_pass_through(path: str):
# #     # This endpoint passes the request to the movie service
# #     print("came here")
# #     return {"message": "Movie service pass-through", "path": path}

# @app.get("/new")
# async def user_service_pass_through():
#     # This endpoint passes the request to the user service
#     return {"hi": "User service pass-through"}

# @app.get("/movie-service/{path:path}")
# async def tile_request(path: str, response: Response):
#     async with httpx.AsyncClient() as client:
#         proxy = await client.get(f"http://movie-service:8001/{path}")
#     response.body = proxy.content
#     response.status_code = proxy.status_code
#     return response

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8003)
