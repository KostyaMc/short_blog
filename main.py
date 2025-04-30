from schemas import BasePost, User, Post
from fastapi import FastAPI


app = FastAPI()

# fake db
posts = []

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