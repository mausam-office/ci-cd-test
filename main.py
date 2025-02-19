from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(title="Demo Ci CD")


@app.get("/")
def home():
    return {"message": "Home page"}


@app.get("/json-test")
def json_test():
    return JSONResponse({"message": "JSON TEST"}, 201)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
