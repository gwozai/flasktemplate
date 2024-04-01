from app import app
from .models import User
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    # 查询所有用户
    users = User.query.all()

    # 提取用户名和邮箱
    user_info = [(user.username, user.email) for user in users]

    return 'Users: {}'.format(user_info)


