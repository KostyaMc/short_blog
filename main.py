from pydantic import BaseModel, Field
from fastapi import FastAPI


class Post(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=2, max_length= 50)
    review: str = Field(..., max_length= 500)


app = FastAPI()

# fake db
posts = []

# create a new post
@app.post("/posts")
def create_post(post: Post):
    post.id = len(posts) + 1
    posts.append(post)
    return {"message": "was created a new post", "post": post}


# read all posts
@app.get("/")
def read_posts():
    return{"posts": posts}


#delete a post
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    if post_id <= len(posts):
        for post in posts:
            if post.id == post_id:
                posts.remove(post)
                return {"message":f"{post.title} was deleted"}
            else:
                return {"message": "post not found"}
    else:
        return {"message": "post not found"}