import os
from secrets import token_hex
from PIL import Image
from flask import current_app, url_for
from flask_mail import Message
from flask_blog import mail


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "A request to reset your password",
        sender="noreply@demo.com",
        recipients=[user.email],
    )
    msg.body = f"""
    To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}.
    If you didn't make this request then simply ignore this email and no changes will be made.
    """
    mail.send(msg)


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
