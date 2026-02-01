from fastapi import Depends, FastAPI, Request, Form, UploadFile, File, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes.database import sessionLocal_pg, sessionLocal_sqlite,  Base_sqlite, Base_pg, engine_sqlite, engine_pg, get_db_pg, get_db_sqlite
from routes.models import UserDetails
from routes.schema import UserLogin, Post
from sqlalchemy.orm import Session

Base_sqlite.metadata.create_all(bind=engine_sqlite)
Base_pg.metadata.create_all(bind=engine_pg)

app = FastAPI(title="FastAPI Challenge")

templates =  Jinja2Templates(directory=("templates"))

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("fastapi_practice.html", {"request": request, "title": "FastAPI Challenge"})

#signupFOrm Data
@app.post("/signUp")
async def signUp():
    pass

#Login FOrm Data
@app.post("/login")
async def login():
    pass

#Create Post (Form + File Upload + Background Task)
@app.post("/upload")
async def upload_file(db: Session = Depends(get_db_sqlite),  title: str = Form(...), content: str = Form(...), author: str = Form(...)):
    author = author
    title = title
    content = content
    return {"title": title, "content": content, "author": author}

#View Posts (Pagination + Filtering + Sorting)
@app.get("/posts/{post_id}")
async def read_post():
    pass

#Download Uploaded Image
@app.get("/image/{image_id}")
async def download_image():
    pass