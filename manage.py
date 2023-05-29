def deploy():
    from app.webapp import create_app,db
    from flask_migrate import init

    app = create_app()
    db.create_all()

    init()

deploy()
