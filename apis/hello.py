from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["Hello"],
    responses={404: {"message": "Not found"}},
)


@router.get("")
async def hello():
    return {"message": "Hello World"}
