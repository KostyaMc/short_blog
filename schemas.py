from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError


class BasePost(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=2, max_length= 50)
    review: str = Field(..., max_length= 500)


class User(BasePost):
    user_name: str = Field(..., min_length=2, max_length=50)   

    @field_validator("user_name")
    def name_cannot_be_empty(cls, name):
        if name == "":
            raise ValidationError("name cannot be empty")
        else:
            return name
        
    email: EmailStr


class Post(BasePost):
    author: User