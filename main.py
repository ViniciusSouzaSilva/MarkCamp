from os import system
from contextlib import closing
import sqlite3

cab1 = f"""\n{'MARK CAMP':^100}
SECRETARIA DE OBRAS PÚBLICAS

LISTA DE OBRAS CADASTRADAS:

{'NÚMERO':<12}{'Nº DE CONTRATAÇÃO':<25}{'NOME':<20}{'ENDEREÇO':<30}"""

def iniciarDB():
    with sqlite3.connect('Obras.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS Obras(Contratacao VARCHAR(10) PRIMARY KEY, Obra VARCHAR(25), Endereco VARCHAR(35), Data DATE, Previsao DATE, Situacao VARCHAR(10), Orcado MONEY(15), Medido MONEY(15))')
            cursor.execute('CREATE TABLE IF NOT EXISTS Visitas(Data DATE, Horario TIME(0), Tempo VARCHAR(10), Servicos VARCHAR(20), Observacoes VARCHAR(20), PRIMARY KEY(Data, Horario))')
            cursor.execute('CREATE TABLE IF NOT EXISTS Medicoes(Data DATE, Horario TIME(0), Descricao VARCHAR(20), Observacoes VARCHAR(20), PRIMARY KEY(Data, Horario))')
            cursor.execute('CREATE TABLE IF NOT EXISTS GestoresPublicos(Nome VARCHAR(35) PRIMARY KEY, Telefone VARCHAR(20), Email VARCHAR(40), Endereco VARCHAR(40))')
            cursor.execute('CREATE TABLE IF NOT EXISTS GestoresPrivados(Nome VARCHAR(35) PRIMARY KEY, Telefone VARCHAR(20), Email VARCHAR(40), Endereco VARCHAR(40))')
    mainMenu()

def mainMenu():
    print(cab1)

    obras = []

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

iniciarDB()