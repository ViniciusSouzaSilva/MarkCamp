from os import system
from contextlib import closing
import sqlite3

cab1 = f"""\n{'MARK CAMP':^100}
SECRETARIA DE OBRAS PÚBLICAS

LISTA DE OBRAS CADASTRADAS:

{'NÚMERO':<12}{'Nº DE CONTRATAÇÃO':<25}{'NOME':<20}{'ENDEREÇO':<30}"""
opcMainMenu = f"""
SELECIONE A OPERAÇÃO:
[1] CADASTRAR OBRA
[2] VISUALIZAR OBRA
[3] EXCLUIR OBRA"""

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

    contratacao = input('Número de contratação: ')
    obra = input('Nome da obra: ')
    endereco = input('Endereço da obra: ')
    anoData = int(input('Ano de início: '))
    mesData = int(input('Mês de início: '))
    diaData = int(input('Dia de início: '))
    anoPrev = int(input('Ano previsto para término: '))
    mesPrev = int(input('Mês previsto para término: '))
    diaPrev = int(input('Dia previsto para término: '))
    orcamento = int(input('Valor orçado: '))
    situacao = input('Situação atual: ')

    data = f"'{anoData}-{mesData}-{diaData}'"
    prev = f"'{anoPrev}-{mesPrev}-{diaPrev}'"

    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'INSERT INTO Obras(Contratacao, Obra, Endereco, Data, Previsao, Situacao, Orcado) VALUES("{contratacao}", "{obra}", "{endereco}", {data}, {prev}, "{situacao}", {orcamento})')
            conexao.commit()

    mainMenu()

def excluirObra(id):
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f'DELETE FROM Obras WHERE Contratacao = "{obras[id - 1][0]}"' )
            conexao.commit()
    mainMenu()


iniciarDB()