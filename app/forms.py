
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    upload = FileField('',validators=[FileRequired('File required for upload'),FileAllowed(['jpg', 'png'], 'Images only!')])