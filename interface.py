from getpass import getpass
import os



def exibir_menu():
    print('''bem vindo ao sistema de login
          [1] cadastrar novo usuario
          [2] fazer login
          [3] sair''')
    
    opcao = str(input('digite a opção: '))
    return opcao

def fazer():
    login = input('digite seu nome: ')
    senha = getpass(prompt='senha: ')
    return login,senha

def buscar(login,senha):
    usuarios = []
    if not os.path.exists('banco.txt'):
            open('banco.txt','w').close()
    with open('banco.txt','r') as arquivos:

               for linha in arquivos:
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
          login,senha = fazer()
          if login == senha:
               print('sua senha deve ser diferente do login')
               senha = getpass('senha: ')
          user = buscar(login,senha)
          if user:
               print('usuario ja existente')
          else:
               with open('banco.txt','+a') as arquivos:
                    arquivos.write(f'{login} {senha}\n')
               print('cadastro aprovado')
               exit()
          
          
     elif opcao == '2':
          login,senha = fazer()
          user = buscar(login,senha)
          if user:
               print('login realizado com sucesso,bem vindo')
               exit()
          else:
               print('acesso negado,voce deve estar digitando nome ou senha errada!TENTE NOVAMENTE!')
     elif opcao == '3':
          print('desligando sistema...')
          break
     else:
          print('voce digito errado,digite de 1 a 3')
          