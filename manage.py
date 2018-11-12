from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from qa_app import app
from db import db
from models import User, Question, Answer

# 执行下列命令时需要在虚拟环境中的manage.py的目录下
# python manage.py db init：初始化一个迁移脚本的环境，只需要执行一次。
# python manage.py db migrate：将模型生成迁移文件，只要模型更改了，就需要执行一遍这个命令。
# python manage.py db upgrade：将迁移文件真正的映射到数据库中。每次运行了 migrate 命令后，就记得要运行这个命令。

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
