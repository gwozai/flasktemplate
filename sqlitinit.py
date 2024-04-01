import sqlite3

# 创建 SQLite 数据库连接
conn = sqlite3.connect('example.db')

# 创建游标对象
cur = conn.cursor()

# 创建用户表
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER,
        gender TEXT
    )
''')

# 提交事务
conn.commit()

# 插入用户数据
users_data = [
    ('user1', 'user1@example.com', 25, 'male'),
    ('user2', 'user2@example.com', 30, 'female'),
    ('user3', 'user3@example.com', None, None)
]

cur.executemany('''
    INSERT INTO users (username, email, age, gender) VALUES (?, ?, ?, ?)
''', users_data)

# 提交事务
conn.commit()

# 关闭游标和连接
cur.close()
conn.close()
