from app.blog.models import Post
from flask import Blueprint, jsonify

blog_bp = Blueprint('blog_bp', __name__)


@blog_bp.route('/')
def index():
    # 查询所有文章
    posts = Post.query.all()

    # 构造文章数据列表
    post_data = []
    for post in posts:
        post_data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id
        })

    # 返回文章数据
    return jsonify({'posts': post_data})
