from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base_pg, Base_sqlite
from sqlalchemy.orm import relationship

class UserDetails(Base_pg):
    __tablename__ = "user_details"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)


class posts_old(Base_pg):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    author = Column(String, index=True)
    

class posts(Base_sqlite):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    author = Column(String, index=True)
    fileName = Column(String, index=True)

    image = relationship("images", back_populates="post", uselist=False, cascade="all, delete-orphan")



class images(Base_sqlite):
    __tablename__ = "image_info"

    id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    file_path = Column(String, nullable=False, index=True)
    mime_type = Column(String, nullable=False, index=True)

    posts = relationship("post", back_populates="image") 