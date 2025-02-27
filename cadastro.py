import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

clear_console() #tentativa de imitar o "console.clear" do JS 

usuarios = []

def cadastrar_usuario ():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    #verifica se o email já foi cadastrado
    for usuario in usuarios:
        if usuario["email"] == email:
            print("Erro: Email já cadastrado")
            return
    
    usuarios.append({"nome": nome, "email": email, "senha": senha})
    print("Usuário cadastrado com sucesso!")
    


def login_usuario():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            return usuario
    print("Erro: Email ou senha incorretos.")
    clear_console()
    return None



def alterar_senha():
    usuario = login_usuario()  #verifica o usuario
    if usuario:
        nova_senha = input("Digite a nova senha: ")
        usuario["senha"] = nova_senha
        print("Senha alterada com sucesso!")
       
        
def menu():
    while True:
        print("\n--- Sistema de Usuários ---")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Alterar senha")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        clear_console()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login_usuario()
        elif opcao == "3":
            alterar_senha()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()