from decouple import config
import os

file_path = os.path.abspath(os.getcwd()) + "\\flask_blog\\site.db"


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path
    SECRET_KEY = config("SECRET_KEY")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")
