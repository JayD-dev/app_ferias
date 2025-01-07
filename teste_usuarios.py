from database import User, create_database

# Criar uma nova sessão do banco de dados
session = create_database()

# Testar a criação de um usuário
def test_create_user():
    create_user("joao", "senha123")
    user = get_user("joao")
    assert user is not None, "Usuário não foi criado!"
    assert user.username == "joao", "Nome de usuário não está correto!"
    assert user.password == "senha123", "Senha não está correta!"

# Testar a atualização de um usuário
def test_update_user():
    update_user("joao", "nova_senha")
    user = get_user("joao")
    assert user.password == "nova_senha", "Senha não foi atualizada!"

# Testar a exclusão de um usuário
def test_delete_user():
    delete_user("joao")
    user = get_user("joao")
    assert user is None, "Usuário não foi deletado!"

# Executar os testes
if __name__ == "__main__":
    test_create_user()
    test_update_user()
    test_delete_user()
    print("Todos os testes passaram!")