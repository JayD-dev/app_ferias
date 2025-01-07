import streamlit as st
from crud import get_user, create_user, update_user, delete_user
import datetime

# Criando tela de login do WebApp
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = get_user(username)
        if user and user.password == password:
            st.success("Login bem-sucedido!")
            return username  # Retorna o username para uso posterior
        else:
            st.error("Usuário ou senha incorretos.")
    return None

# Criando, modificando e deletando usuários através do WebApp
def manage_users():
    st.title("Gerenciar Usuários")
    action = st.selectbox("Escolha uma ação", ["Criar", "Modificar", "Deletar"])

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if username:  # Verifica se o username não está vazio
        if action == "Criar" and st.button("Criar Usuário"):
            create_user(username, password)
            st.success("Usuário criado com sucesso!")

        elif action == "Modificar" and st.button("Modificar Usuário"):
            update_user(username, password)
            st.success("Usuário modificado com sucesso!")

        elif action == "Deletar" and st.button("Deletar Usuário"):
            delete_user(username)
            st.success("Usuário deletado com sucesso!")

# Criando um calendário no Streamlit
def show_calendar(username):
    st.title("Calendário de Férias")
    start_date = st.date_input("Data de Início", datetime.date.today())
    end_date = st.date_input("Data de Fim", datetime.date.today() + datetime.timedelta(days=30))

    if st.button("Confirmar Férias"):
        request_vacation(username, start_date, end_date)

# Adicionando férias para um usuário
def request_vacation(username, start_date, end_date):
    user = get_user(username)
    if user:
        if user.vacation_days >= (end_date - start_date).days:
            user.vacation_days -= (end_date - start_date).days
            session.commit()  # Certifique-se de que 'session' está definido
            st.success("Férias solicitadas com sucesso!")
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
    
    if st.button("Ver Saldo "):
        view_vacation_days(username)

if __name__ == "__main__":
    username = login()
    if username:  # Verifica se o login foi bem-sucedido
        manage_users()
        show_calendar(username)
        show_vacation_balance()