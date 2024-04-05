from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField

# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# TODO: Create a RegisterForm to register new users
class RegisterAccForm(FlaskForm):
    username = StringField("Your Username", validators=[DataRequired()])
    email = EmailField("Your Email", validators=[DataRequired(), Email(message="invalid email address") ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="password must be 8 charachters")])
    register = SubmitField("REGISTER")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Your Email", validators=[DataRequired(), Email(message="invalid email address") ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="password must be 8 charachters")])
    register = SubmitField("LOGIN")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("ADD COMMENT")
