from getpass import getpass
import os

def exibir_menu():
    print('''Bem-vindo ao sistema de login
          [1] Cadastrar novo usuário
          [2] Fazer login
          [3] Sair''')
    
    opcao = str(input('Digite a opção: '))
    return opcao

def fazer():
    login = input('Digite seu nome: ')
    senha = getpass(prompt='Senha: ')
    return login, senha

def buscar(login, senha):
    usuarios = []
    if not os.path.exists('banco.txt'):
        open('banco.txt', 'w').close()  # Cria o arquivo se não existir
    with open('banco.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            usuarios.append(linha.split())
        for usuario in usuarios:
            nome = usuario[0]
            password = usuario[1]
            if login == nome and senha == password:
                return True
    return False

while True:
    opcao = exibir_menu()

    if opcao == '1':
        login, senha = fazer()
        if login == senha:
            print('Sua senha deve ser diferente do login')
            senha = getpass('Senha: ')
        user = buscar(login, senha)
        if user:
            print('Usuário já existente')
        else:
            with open('banco.txt', 'a') as arquivos:
                arquivos.write(f'{login} {senha}\n')
            print('Cadastro aprovado')
            exit()
    elif opcao == '2':
        login, senha = fazer()
        user = buscar(login, senha)
        if user:
            print('Login realizado com sucesso, bem-vindo')
            exit()
        else:
            print('Acesso negado, você deve estar digitando nome ou senha errada! TENTE NOVAMENTE!')
    elif opcao == '3':
        print('Desligando sistema...')
        break
    else:
        print('Você digitou errado, digite de 1 a 3')
