from os import system
from contextlib import closing
import sqlite3

cab1 = f"""\n{'MARK CAMP':^120}
SECRETARIA DE OBRAS PÚBLICAS

LISTA DE OBRAS CADASTRADAS:

{'NÚMERO':<12}{'Nº DE CONTRATAÇÃO':<25}{'NOME':<20}{'ENDEREÇO':<30}"""

cab2 = f"\n{'MARK CAMP':^150}\n\n" + '''OBRA: {a1:<35}GESTOR PUBLICO: {a2:<25}TEL: {a3:<15}EMAIL: {a4:<30}
ENDEREÇO: {a5:<31}GESTOR PRIVADO: {a6:<25}TEL: {a7:<15}EMAIL: {a8:<30}
DATA: {a9:<35}PROCESSO DE CONTRATAÇÃO: {a10:<30}
SITUAÇÃO ATUAL: {a11:25}VALOR ORÇADO: {a12:<30}
PREVISÃO DE TÉRMINO: {a13:<20}VALOR MEDIDO: {a14:<30}
'''

opcMainMenu = f"""
SELECIONE A OPERAÇÃO:
[1] CADASTRAR OBRA
[2] VISUALIZAR OBRA
[3] EXCLUIR OBRA"""

n = 'Lorem ipsum'

obras = []

def iniciarDB():
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS Obras(Contratacao VARCHAR(10) PRIMARY KEY, Obra VARCHAR(25), Endereco VARCHAR(35), Data DATE, Previsao DATE, Situacao VARCHAR(10), Orcado MONEY(15), Medido MONEY(15), GestorPu VARCHAR(35), GestorPr VARCHAR(35))')
            cursor.execute('CREATE TABLE IF NOT EXISTS Visitas(Data DATE, Horario TIME(0), Tempo VARCHAR(10), Servicos VARCHAR(20), Observacoes VARCHAR(20), Contratacao VARCHAR(10), PRIMARY KEY(Data, Horario))')
            cursor.execute('CREATE TABLE IF NOT EXISTS Medicoes(Data DATE, Horario TIME(0), Descricao VARCHAR(20), Observacoes VARCHAR(20), Contratacao VARCHAR(10), PRIMARY KEY(Data, Horario))')
            cursor.execute('CREATE TABLE IF NOT EXISTS GestoresPublicos(Nome VARCHAR(35) PRIMARY KEY, Telefone VARCHAR(20), Email VARCHAR(40), Endereco VARCHAR(40))')
            cursor.execute('CREATE TABLE IF NOT EXISTS GestoresPrivados(Nome VARCHAR(35) PRIMARY KEY, Telefone VARCHAR(20), Email VARCHAR(40), Endereco VARCHAR(40))')
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
    elif escolha == 3:
        id = int(input('Número da obra: '))
        excluirObra(id)

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

def excluirObra(id):
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'DELETE FROM Obras WHERE Contratacao = "{obras[id - 1][0]}"')
            conexao.commit()
    mainMenu()


iniciarDB()








tes = 'Obra: {a:^20} aaaaaaaaa {b}'
