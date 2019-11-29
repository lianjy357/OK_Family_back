from okf import create_app, db
from flask_script import Manager # 管理命令对象
from flask_migrate import Migrate, MigrateCommand # 导入迁移执行者 和 迁移人员

if __name__ == '__main__':
    app = create_app("develop")

    # 数据库迁移插件
    manager = Manager(app)
    Migrate(app, db)
    manager.add_command("db", MigrateCommand)

    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True, host='0.0.0.0')