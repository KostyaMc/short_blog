from schemas import BasePost, User, Post
from fastapi import FastAPI, HTTPException
from authx import AuthX, AuthXConfig

app = FastAPI()

config = AuthXConfig()
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = "SECRET_KEY"

security = AuthX(config=config)

# fake db
posts = []


@app.get("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        token = security.create_access_token(uid=username)
        return {"access_token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")



# create a new post
@app.post("/posts")
def create_post(post: BasePost):
    post.id = len(posts) + 1
    posts.append(post)
    return {"message": "was created a new post", "post": post}


# read all posts
@app.get("/")
def read_posts():
    return{"posts": posts}


#get a one post
@app.get("/posts/{post_id}")
def rear_post(post_id: int):
    if post_id <= len(posts):
        for post in posts:
            if post.id == post_id:
                return {"post": post}
    else:
        return {"message": "post not found"}


#delete a post
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    if post_id > len(posts):
        return {"message": "post not found"}
    else:
        for post in posts:
            if post.id == post_id:
                posts.remove(post)
                return {"post": f"{post} was deleted"}