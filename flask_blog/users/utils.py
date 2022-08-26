import os
from secrets import token_hex
from PIL import Image
from flask import current_app


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path, "static\\pfps", picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn