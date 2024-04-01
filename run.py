from app import app
from initialize import init_db

if __name__ == '__main__':
    # 在应用程序上下文中初始化数据库
    with app.app_context():
        init_db()

    # 启动 Flask 应用程序
    app.run(debug=True)
