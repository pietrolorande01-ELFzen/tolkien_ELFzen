contas =[]
import os

def home():
    print("""


██████╗░░█████╗░███╗░░██╗██╗░░██╗░░░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗████╗░██║██║░██╔╝░░░██╔══██╗╚██╗░██╔╝
██████╦╝███████║██╔██╗██║█████═╝░░░░██████╔╝░╚████╔╝░
██╔══██╗██╔══██║██║╚████║██╔═██╗░░░░██╔═══╝░░░╚██╔╝░░
██████╦╝██║░░██║██║░╚███║██║░╚██╗██╗██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░""")


def exibir_opcoes():

    print('\n\n1. cadastrar Conta BancÃ¡ria\n')
    print('2. Listar contas cadastradas\n')
    print('3. Ativar contas\n')
    print('4. sair do App\n')


# SISTEMA DE PERGUNTA PARA SEGUIR PARA O MENU OU NÃƒO

def pergunta_final():
    print('Por favor confirme seus dados antes de prosseguir')
    confirmacao = str(input('\n\nPor favor digite s = sim / n = não:  '))
    if confirmacao == "s" :
        main()

    else:
        print('te redicionaremos ao menu para que possa refazer seu cadastro')
        exibir_opcoes()
        escolher_opcao()

def exibir_subtitulo(texto):

    os.system('cls')
    print(texto)
    print()
    print()


def cadastro_nova_conta():
    exibir_subtitulo('Cdastro de novas contas')
    print('\nResponda por favor o teste para avanÃ§ar no cadastro !\n')  #SISTEMA DE VERIFICAÃ‡ÃƒO DE IDADE

    idade = int(input('Por favor digite a sua idade: '))

    if 0 < idade <= 17:
        print('De acordo com as nossas diretrizes você nÃo está apto a colaborar com uma conta em nossa organização ')
        opcao_invalida()
    else:
        nome_da_conta = str(input('\n\nDigite o nome do titular da conta: \n'))
        numero_do_cpf = input('\n\nDigite um CPF válido -  11 Dí­gitos: \n')

        conta = {

             'nome': nome_da_conta,
             'cpf': numero_do_cpf
        }

        contas.append(conta)
        print(f'\n\nPor favor confirme seus dados {conta}')
        pergunta_final()


def opcao_invalida():
    print('Opção Inválida\n\n')
    input('por favor digite qualquer tecla para voltar a home : \n\n')
    main()


def listando_contas():
    exibir_subtitulo('Listando Contas')

    for conta in contas:
        print(f"CPF: {conta['cpf']}")
        print(f"Nome: {conta['nome']}")
        print("----------------------")

    pergunta_final()


def escolher_opcao():

    try:
        opcao_escolhida = int(input('\nPor favor digite o número do menu que gostaria de acessar:\n\n\n '))

        if opcao_escolhida == 1 :
            print('Bem vindo ao Banco da terra media\n vamos dar inicio em seu cadastro\n')
            cadastro_nova_conta()

        elif opcao_escolhida == 2 :
            listando_contas()

        elif opcao_escolhida == 3 :
            print('Ativar conta ')
            main()

        elif opcao_escolhida == 4 :
            print('Finalizando o App')

        else:
            opcao_invalida()

    except:
        print('Oção Inválida')

def main():
    os.system('cls')
    home()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()