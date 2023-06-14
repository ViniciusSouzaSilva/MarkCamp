from os import system
from contextlib import closing
import sqlite3

cab1 = f"""\n{'MARK CAMP':^120}
SECRETARIA DE OBRAS PÚBLICAS

LISTA DE OBRAS CADASTRADAS:

{'NÚMERO':<12}{'Nº DE CONTRATAÇÃO':<25}{'NOME':<20}{'ENDEREÇO':<30}"""

cab2 = f"\n{'MARK CAMP':^120}\n\n" + '''OBRA: {a1:<35}GESTOR PUBLICO: {a2:<25}TEL: {a3:<15}EMAIL: {a4:<30}
ENDEREÇO: {a5:<31}GESTOR PRIVADO: {a6:<25}TEL: {a7:<15}EMAIL: {a8:<30}
DATA: {a9:<35}PROCESSO DE CONTRATAÇÃO: {a10:<30}
SITUAÇÃO ATUAL: {a11:25}VALOR ORÇADO: {a12:<30}
PREVISÃO DE TÉRMINO: {a13:<20}VALOR MEDIDO: {a14:<30}
'''

cab3 = f"""\n{'MARK CAMP':^120}

LISTA DE GESTORES PUBLICOS CADASTRADOS:

{'NÚMERO':<12}{'NOME':<25}{'TELEFONE':<25}{'E-MAIL':<25}"""

opcMainMenu = f"""
SELECIONE A OPERAÇÃO:
[1] CADASTRAR OBRA
[2] VISUALIZAR OBRA
[3] EXCLUIR OBRA
[4] VISUALIZAR GESTORES PÚBLICOS
[5] VISUALIZAR GESTORES PRIVADOS\n"""

opcVisuGestor = f"""
SELECIONE A OPERAÇÃO:
[1] CADASTRAR GESTOR
[2] EDITAR GESTOR
[3] EXCLUIR GESTOR\n"""

opcVisuObra = f"""
SELECIONE A OPERAÇÃO:
[1] DESIGNAR GESTOR PÚBLICO
[2] DESIGNAR GESTOR PRIVADO
[3] VISUALIZAR INFORMAÇÕES DE VISITAS DE OBRA
[4] VISUALIZAR INFORMAÇÕES DE MEDIÇÕES E ADITAMENTOS
[5] INSERIR INFORMAÇÕES DE VISITAS DE OBRA
[6] INSERIR INFORMAÇÕES DE MEDIÇÕES E ADITAMENTOS
[7] EDITAR INFORMAÇÕES DA OBRA
[8] VOLTAR\n"""

n = 'Lorem ipsum'

obras = []
gestpu = []
gestpr = []

def iniciarDB():
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS Obras(Contratacao VARCHAR(10) PRIMARY KEY, Obra VARCHAR(25), Endereco VARCHAR(35), Data DATE, Previsao DATE, Situacao VARCHAR(10), Orcado MONEY(15), Medido MONEY(15) DEFAULT 0, GestorPu VARCHAR(35) DEFAULT "", GestorPr VARCHAR(35) DEFAULT "")')
            cursor.execute('CREATE TABLE IF NOT EXISTS Visitas(Data DATE, Horario TIME(0), Tempo VARCHAR(10), Servicos VARCHAR(20), Observacoes VARCHAR(20), Contratacao VARCHAR(10), PRIMARY KEY(Data, Horario))')
            cursor.execute('CREATE TABLE IF NOT EXISTS Medicoes(Data DATE, Horario TIME(0), Descricao VARCHAR(20), Observacoes VARCHAR(20), Contratacao VARCHAR(10), PRIMARY KEY(Data, Horario))')
            cursor.execute('CREATE TABLE IF NOT EXISTS GestoresPublicos(Nome VARCHAR(35) PRIMARY KEY, Telefone VARCHAR(20), Email VARCHAR(40))')
            cursor.execute('CREATE TABLE IF NOT EXISTS GestoresPrivados(Nome VARCHAR(35) PRIMARY KEY, Telefone VARCHAR(20), Email VARCHAR(40))')
    mainMenu()

def mainMenu():
    system('cls')
    obras.clear()

    print(cab1)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM Obras')

            while True:
                res = cursor.fetchone()
                if res is None:
                    break
                else:
                    obras.append(res)

            for i in obras:
                print(f"{obras.index(i) + 1:<12}{i[0]:<25}{i[1]:<20}{i[2]:<30}")

    print(opcMainMenu)

    escolha = int(input('---> '))

    if escolha == 1:
        cadastrarObra()
    elif escolha == 2:
        id = int(input('Número da obra: '))
        visualizarObra(id)
    elif escolha == 3:
        id = int(input('Número da obra: '))
        excluirObra(id)
    elif escolha == 4:
        visualizarGesPub()
    elif escolha == 5:
        visualizarGesPri()

def cadastrarObra():
    system('cls')

    contratacao = ''
    obra = ''
    endereco = ''
    anoData = ''
    mesData = ''
    diaData = ''
    anoPrev = ''
    mesPrev = ''
    diaPrev = ''
    orcamento = ''
    situacao = ''
    data = ''
    prev = ''

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    contratacao = input('Número de contratação: ')
    system('cls')

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao, a11=situacao, a12=orcamento, a13=prev, a14=''))
    obra = input('Nome da obra: ')
    system('cls')

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    endereco = input('Endereço da obra: ')
    system('cls')

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    anoData = int(input('Ano de início: '))
    mesData = int(input('Mês de início: '))
    diaData = int(input('Dia de início: '))
    data = f"'{anoData}-{mesData}-{diaData}'"
    system('cls')

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    anoPrev = int(input('Ano previsto para término: '))
    mesPrev = int(input('Mês previsto para término: '))
    diaPrev = int(input('Dia previsto para término: '))
    prev = f"'{anoPrev}-{mesPrev}-{diaPrev}'"
    system('cls')

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    orcamento = int(input('Valor orçado: '))
    system('cls')

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    situacao = input('Situação atual: ')
    system('cls')

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'INSERT INTO Obras(Contratacao, Obra, Endereco, Data, Previsao, Situacao, Orcado) VALUES("{contratacao}", "{obra}", "{endereco}", {data}, {prev}, "{situacao}", {orcamento})')
            conexao.commit()

    print(cab2.format(a1=obra, a2='', a3='', a4='', a5=endereco, a6='', a7='', a8='', a9=data, a10=contratacao,a11=situacao, a12=orcamento, a13=prev, a14=''))
    input('Pressione enter para voltar...')
    mainMenu()

def cadastrarGestorPublico():
    nome = input('Nome do novo gestor: ')
    tel = int(input('Telefone do novo gestor: '))
    email = input('E-mail do novo gestor: ')

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'INSERT INTO GestoresPublicos(Nome,Telefone,Email) VALUES("{nome}",{tel},"{email}")')

    visualizarGesPub()

def cadastrarGestorPrivado():
    nome = input('Nome do novo gestor: ')
    tel = int(input('Telefone do novo gestor: '))
    email = input('E-mail do novo gestor: ')

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'INSERT INTO GestoresPrivados(Nome,Telefone,Email) VALUES("{nome}",{tel},"{email}")')

    visualizarGesPri()

def designarGestorPublico(id):
    system('cls')
    print(cab3)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM GestoresPublicos')

            while True:
                res = cursor.fetchone()
                if res == None:
                    break
                else:
                    gestpu.append(res)

    for i in gestpu:
        print(f'{gestpu.index(i) + 1:<12}{i[0]:<25}{i[1]:<25}{i[2]:<25}')

    escolha = int(input("Número do gestor escolhido ---> "))

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'UPDATE Obras SET GestorPu = "{gestpu[escolha - 1][0]}" WHERE Contratacao = "{obras[id - 1][0]}"')
            conexao.commit()

    visualizarObra(id)

def designarGestorPrivado(id):
    system('cls')
    print(cab3)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM GestoresPrivados')

            while True:
                res = cursor.fetchone()
                if res == None:
                    break
                else:
                    gestpr.append(res)

    for i in gestpr:
        print(f'{gestpr.index(i) + 1:<12}{i[0]:<25}{i[1]:<25}{i[2]:<25}')

    escolha = int(input("Número do gestor escolhido ---> "))

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(
                f'UPDATE Obras SET GestorPr = "{gestpr[escolha - 1][0]}" WHERE Contratacao = "{obras[id - 1][0]}"')
            conexao.commit()

    visualizarObra(id)

def visualizarObra(id):
    system('cls')
    locgespu = []
    locgespr = []

    obras.clear()

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM Obras')

            while True:
                res = cursor.fetchone()
                if res is None:
                    break
                else:
                    obras.append(res)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'SELECT Telefone, Email FROM GestoresPublicos WHERE Nome = "{obras[id - 1][8]}"')
            while True:
                res = cursor.fetchone()
                if res == None:
                    break
                else:
                    locgespu.append(res)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'SELECT Telefone, Email FROM GestoresPrivados WHERE Nome = "{obras[id - 1][9]}"')
            while True:
                res = cursor.fetchone()
                if res == None:
                    break
                else:
                    locgespr.append(res)

    if locgespu != [] and locgespr != []:
        print(cab2.format(a1=obras[id - 1][1], a2=obras[id - 1][8], a3=locgespu[0][0], a4=locgespu[0][1],a5=obras[id - 1][2], a6=obras[id - 1][9], a7=locgespr[0][0], a8=locgespr[0][1], a9=obras[id - 1][3], a10=obras[id - 1][0],a11=obras[id - 1][5], a12=obras[id - 1][6], a13=obras[id - 1][4], a14=obras[id - 1][7]))
    elif locgespu != [] and locgespr == []:
        print(cab2.format(a1=obras[id - 1][1], a2=obras[id - 1][8], a3=locgespu[0][0], a4=locgespu[0][1],a5=obras[id - 1][2], a6='', a7='', a8='', a9=obras[id - 1][3], a10=obras[id - 1][0],a11=obras[id - 1][5], a12=obras[id - 1][6], a13=obras[id - 1][4], a14=obras[id - 1][7]))
    elif locgespu == [] and locgespr != []:
        print(cab2.format(a1=obras[id - 1][1], a2=obras[id - 1][8], a3='', a4='',a5=obras[id - 1][2], a6=obras[id - 1][9], a7=locgespr[0][0], a8=locgespr[0][1], a9=obras[id - 1][3], a10=obras[id - 1][0],a11=obras[id - 1][5], a12=obras[id - 1][6], a13=obras[id - 1][4], a14=obras[id - 1][7]))
    else:
        print(cab2.format(a1=obras[id - 1][1], a2=obras[id - 1][8], a3='', a4='',a5=obras[id - 1][2], a6='', a7='', a8='', a9=obras[id - 1][3], a10=obras[id - 1][0],a11=obras[id - 1][5], a12=obras[id - 1][6], a13=obras[id - 1][4], a14=obras[id - 1][7]))

    print(opcVisuObra)
    escolha = int(input('---> '))

    if escolha == 1:
        designarGestorPublico(id)
    if escolha == 2:
        designarGestorPrivado(id)

def visualizarGesPub():
    system('cls')
    print(cab3)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM GestoresPublicos')

            while True:
                res = cursor.fetchone()
                if res == None:
                    break
                else:
                    gestpu.append(res)

    for i in gestpu:
        print(f'{gestpu.index(i) + 1:<12}{i[0]:<25}{i[1]:<25}{i[2]:<25}')

    print(opcVisuGestor)
    escolha = int(input('---> '))

    if escolha == 1:
        cadastrarGestorPublico()

def visualizarGesPri():
    system('cls')
    print(cab3)

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM GestoresPrivados')

            while True:
                res = cursor.fetchone()
                if res == None:
                    break
                else:
                    gestpr.append(res)

    for i in gestpr:
        print(f'{gestpr.index(i) + 1:<12}{i[0]:<25}{i[1]:<25}{i[2]:<25}')

    print(opcVisuGestor)
    escolha = int(input('---> '))

    if escolha == 1:
        cadastrarGestorPrivado()

def excluirObra(id):
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'DELETE FROM Obras WHERE Contratacao = "{obras[id - 1][0]}"')
            conexao.commit()
    mainMenu()

def search():
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('SELECT * FROM Obras')
            res = cursor.fetchone()

            print(res)

#search()
iniciarDB()
