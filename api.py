from fastapi import Body, HTTPException
from typing import List

from main import app
from model import User
from base_model import UpdateUserDTO


@app.post("/api/v1/create-user", response_model=User)
async def insert_user(user: User):
    result = await app.db["User"].insert_one(user.dict())
    inserted_user = await app.db["User"].find_one({"_id": result.inserted_id})
    return inserted_user

@app.get("/api/v1/read-all-users", response_model=List[User])
async def read_users():
    users = await app.db["User"].find().to_list(None)
    return users

# Read one user by email_address
@app.get("/api/v1/read-user/{email_address}", response_model=User)
async def read_user_by_email(email_address: str):
    user = await app.db["User"].find_one({"email_address": email_address})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

    
@app.put("/api/v1/update-user/{email_address}", response_model=User)
async def update_user(email_address: str, user_update: UpdateUserDTO):
    updated_result = await app.db["User"].update_one(
        {"email_address": email_address}, {"$set": user_update.dict(exclude_unset=True)})
    if updated_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no update needed")
    updated_user = await app.db["User"].find_one({"email_address": email_address})
    return updated_user


@app.delete("/api/v1/delete-user/{email_address}", response_model=dict)
async def delete_user_by_email(email_address: str):
    delete_result = await app.db["User"].delete_one({"email_address": email_address})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}