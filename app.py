import streamlit as st
from crud import get_user, create_user, update_user, delete_user, session
import datetime

# Função para criar um usuário administrador
def create_admin_user():
    admin_username = "admin"
    admin_password = "admin123"

    if not get_user(admin_username):
        create_user(admin_username, admin_password)
        print(f"Usuário administrador '{admin_username}' criado com sucesso!")
    else:
        print(f"Usuário administrador '{admin_username}' já existe.")

# Criando tela de login do WebApp
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = get_user(username)
        if user and user.password == password:
            st.session_state.username = username
            st.session_state.is_admin = (user.username == "admin")  # Verifica se é admin
            st.success("Login bem-sucedido!")
            return True
        else:
            st.error("Usuário ou senha incorretos.")
    return False

# Criando, modificando e deletando usuários através do WebApp
def manage_users():
    st.title("Gerenciar Usuários")
    
    action = st.selectbox("Escolha uma ação", ["Criar", "Modificar", "Deletar"])
    
    username = st.text_input("Username", key="manage_username")
    password = st.text_input("Password", type='password', key="manage_password")

    if action == "Criar" and st.button("Criar Usuário"):
        if username and password:
            create_user(username, password)
            st.success("Usuário criado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    elif action == "Modificar" and st.button("Modificar Usuário"):
        if username and password:
            update_user(username, password)
            st.success("Usuário modificado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    elif action == "Deletar" and st.button("Deletar Usuário"):
        if username:
            delete_user(username)
            st.success("Usuário deletado com sucesso!")
        else:
            st.error("Por favor, insira um username para deletar.")

# Criando um calendário no Streamlit
def show_calendar():
    st.title("Calendário de Férias")
    start_date = st.date_input("Data de Início", datetime.date.today())
    end_date = st.date_input("Data de Fim", datetime.date.today() + datetime.timedelta(days=30))

    if st.button("Confirmar Férias"):
        request_vacation(st.session_state.username, start_date, end_date)

# Adicionando férias para um usuário
def request_vacation(username, start_date, end_date):
    user = get_user(username)
    if user:
        if user.vacation_days >= (end_date - start_date).days:
            user.vacation_days -= (end_date - start_date).days
            session.commit()
            st.success(f"Férias solicitadas com sucesso de {start_date} até {end_date}!")
        else:
            st.error("Dias de férias insuficientes.")
    else:
        st.error("Usuário não encontrado.")

# Visualizando quantos dias cada usuário tem para solicitar de férias
def view_vacation_days(username):
    user = get_user(username)
    if user:
        st.write(f"{user.username} tem {user.vacation_days} dias de férias disponíveis.")
    else:
        st.error("Usuário não encontrado.")

def show_vacation_balance():
    st.title("Saldo de Férias")
    username = st.text_input("Username")
    
    if st.button("Ver Saldo"):
        view_vacation_days(username)

def logout():
    st.session_state.clear()  # Limpa todas as informações do session_state
    st.success("Você saiu com sucesso!")
    st.experimental_rerun()  # Redireciona para a tela de login

# Função principal do aplicativo
def main():
    if "username" not in st.session_state:
        if login():
            st.session_state.is_admin = (st.session_state.username == "admin")  # Verifica se é admin
    else:
        if st.session_state.is_admin:
            menu_options = ["Gerenciar Usuários", "Calendário de Férias", "Saldo de Férias", "Sair"]
        else:
            menu_options = ["Calendário de Férias", "Saldo de Férias", "Sair"]

        choice = st.sidebar.selectbox("Escolha uma opção", menu_options)

        if choice == "Gerenciar Usuários":
            manage_users()
        elif choice == "Calendário de Férias":
            show_calendar()
        elif choice == "Saldo de Férias":
            show_vacation_balance()
        elif choice == "Sair":
            logout()

if __name__ == "__main__":
    create_admin_user()  # Cria o usuário admin se não existir
    main()  # Executa a função principal do aplicativo
# Certifique-se de que a função de login é chamada corretamente após o logout
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = get_user(username)
        if user and user.password == password:
            st.session_state.username = username
            st.session_state.is_admin = (user.username == "admin")  # Verifica se é admin
            st.success("Login bem-sucedido!")
            return True
        else:
            st.error("Usuário ou senha incorretos.")
    return False