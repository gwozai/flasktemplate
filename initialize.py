from app import app, db
from app.auth.models import User
from app.blog.models import Post

def init_db():
    # 在应用程序上下文中添加初始数据
    with app.app_context():
        # 创建数据库表
        db.create_all()

        # 添加初始用户数据
        if not User.query.first():
            user1 = User(username='user1', email='user1@example.com')
            user2 = User(username='user2', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

        # 添加示例文章数据
        if not Post.query.first():
            post1 = Post(title='First Post', content='This is the content of the first post', user_id=1)
            post2 = Post(title='Second Post', content='This is the content of the second post', user_id=2)
            db.session.add(post1)
            db.session.add(post2)
            db.session.commit()
