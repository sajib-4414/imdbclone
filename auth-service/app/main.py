from fastapi import FastAPI, HTTPException
from views import auth_views, token_views
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
app = FastAPI()

#overrriding the default http exception format
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"errors": exc.detail},
    )
    
# Custom exception handler for validation errors
async def validation_exception_handler(request, exc):
    errors = []
    for error in exc.errors():
        print("detail error is")
        print(error)
        error_info = {
            "error_code": error["type"],
            # "field_name": ".".join(error["loc"]),  # Get the field name from the loc attribute
            "error_details": error["loc"][-1] + " " +error["msg"],
        }
        errors.append(error_info)

    response_content = {"errors": errors}
    return JSONResponse(content=response_content, status_code=400)  # Set a custom status code

# Register the custom exception handler
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(auth_views.router, prefix="")  # Include auth-related routes
app.include_router(token_views.router, prefix="")  # Include user-related routes


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8003)
