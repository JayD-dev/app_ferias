from database import User, create_database

session = create_database()

def create_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    print(f"Usuário criado: {new_user.username}")  # Adicione esta linha

def get_user(username):
    user = session.query(User).filter_by(username=username).first()
    print(f"Usuário recuperado: {user.username if user else 'Nenhum usuário encontrado'}")  # Adicione esta linha
    return user

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