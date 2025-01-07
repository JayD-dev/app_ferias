from database import User, create_database

session = create_database()

def create_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()

def get_user(username):
    return session.query(User).filter_by(username=username).first()

def update_user(username, password):
    user = get_user(username)
    if user:
        user.password = password
        session.commit()

def delete_user(username):
    user = get_user(username)
    if user:
        session.delete(user)
        session.commit()