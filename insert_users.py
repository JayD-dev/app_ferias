from crud import create_user

# Lista de usuários fictícios para inserir
fake_users = [
    ("Lucas Silva", "123456"),
    ("Mariana Oliveira", "234567"),
    ("Gabriel Santos", "345678"),
    ("Ana Costa", "456789"),
    ("Felipe Almeida", "567890"),
    ("Juliana Pereira", "678901"),
    ("Ricardo Lima", "789012"),
    ("Fernanda Rocha", "890123"),
    ("Thiago Martins", "901234"),
    ("Camila Ferreira", "012345"),
    ("Eduardo Gomes", "135792"),
    ("Patrícia Mendes", "246803"),
    ("Roberto Dias", "357914"),
    ("Aline Nascimento", "468025"),
    ("Bruno Cardoso", "579136"),
    ("Sofia Ribeiro", "680247"),
    ("Vinícius Pires", "791358"),
    ("Isabela Teixeira", "802469"),
    ("André Souza", "913570"),
    ("Larissa Martins", "024681"),
]

# Inserindo usuários no banco de dados
for username, password in fake_users:
    create_user(username, password)
    print(f"Usuário '{username}' criado com sucesso!")