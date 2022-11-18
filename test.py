from fastapi import APIRouter
import boto3


router = APIRouter()

@router.get("/category/all", tags=["categories"])
async def get_all_categories_from_dynamodb():
    client = boto3.resource("dynamodb")
    table = client.Table("Category")
    response = table.scan()
    categories = response['Items']
    return categories

@router.get("/category/{id}", tags=["categories"])
async def get_category_by_id(id: int):
    return {"Category with id: {}".format(id)}
