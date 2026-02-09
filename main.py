from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend 🚀"}

# Additional endpoint
@app.get("/about")
def about():
    return {"project": "DevOps Assignment", "status": "Running Successfully"}

