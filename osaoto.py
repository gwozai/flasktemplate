import os
import shutil

def create_project_structure(project_name):
    # 创建项目目录
    os.makedirs(project_name)

    # 创建子目录
    subdirectories = [
        'app',
        'app/auth',
        'app/blog',
        'app/static',
        'app/templates',
        'migrations',
        'tests',
        'venv'
    ]
    for subdir in subdirectories:
        os.makedirs(os.path.join(project_name, subdir))

    # 创建文件
    files = {
        'app/__init__.py': '',
        'app/models.py': '',
        'app/utils.py': '',
        'config.py': '',
        'run.py': ''
    }
    for filepath, content in files.items():
        with open(os.path.join(project_name, filepath), 'w') as f:
            f.write(content)

    # 创建子模块文件
    submodules = {
        'app/auth/__init__.py': '',
        'app/auth/forms.py': '',
        'app/auth/models.py': '',
        'app/auth/routes.py': '',
        'app/blog/__init__.py': '',
        'app/blog/forms.py': '',
        'app/blog/models.py': '',
        'app/blog/routes.py': '',
        'tests/__init__.py': ''
    }
    for filepath, content in submodules.items():
        with open(os.path.join(project_name, filepath), 'w') as f:
            f.write(content)

    print(f"Project structure created successfully for '{project_name}'.")

if __name__ == '__main__':
    project_name = input("Enter project name: ")
    create_project_structure(project_name)
