import logging
import time

from fastapi import FastAPI
from fastapi import Request
from starlette.middleware.cors import CORSMiddleware

# test
# v1
from apis import hello

origins = ["*"]

app = FastAPI(
    title="KickstartGitHubAction Apis",
    description="KickstartGitHubAction Apis",
    debug=False,
    version="0.0.1"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logging.info("Application start")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutdown")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# v1
app.include_router(router=hello.router, prefix="/apis/v1")
