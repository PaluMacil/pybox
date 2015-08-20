__author__ = 'dan'

import os
from app import create_app, db
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)


def make_shell_context():
    # app.test_request_context().push()
    # print("app request context has been pushed")
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def setup():
    """Run db setup tasks."""
    from app.account.models import Role, User
    from app.blog.models import Post
    # from app.core.models import Settings

    db.create_all()

    # Create Roles
    admin_role = Role(name='Admin', default=False)
    user_role = Role(name='User', default=True)
    db.session.add_all([admin_role, user_role])

    # Create Default User
    user_admin = User(username='admin',
                      email='admin@example.com',
                      password='admin',
                      confirmed=True,
                      name='Admin',
                      location='NA',
                      about_me='This is the default admin account',
                      role=admin_role)
    db.session.add(user_admin)

    # Create sample blog post
    post_text = "This is an example post. Please change default settings before deploying this app."
    post_example = Post(body=post_text, body_html=post_text, author=user_admin)
    db.session.add(post_example)

    # Commit session
    db.session.commit()

if __name__ == '__main__':
    manager.run()
