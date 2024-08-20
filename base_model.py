from pydantic import BaseModel
from typing import List


class UpdateUserDTO(BaseModel):
    other_names: List[str] = None
    age: int = None