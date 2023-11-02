from fastapi import FastAPI
from views import auth_views, token_views
app = FastAPI()


app.include_router(auth_views.router, prefix="")  # Include auth-related routes
app.include_router(token_views.router, prefix="")  # Include user-related routes


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8003)
