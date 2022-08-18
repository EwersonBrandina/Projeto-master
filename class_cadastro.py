from msvcrt import kbhit
from re import L
from tkinter import messagebox
import mysql.connector
from class_usuario import*
class Cadastro:

    def __init__(self, dolar, euro, libra, bitcoin, ethereum):
        self.dolar = dolar
        self.euro = euro
        self.libra = libra
        self.bitcoin = bitcoin
        self.ethereum = ethereum
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='92337155Thule03@1', database='investimentos')
        self.mycursor = self.conexao.cursor() 

    def cadastro(self,cpf_cnpj, nome, dataNasc, telefone, senha):
        cpf_cnpj = cpf_cnpj
        nome = nome
        dataNasc = dataNasc
        telefone = telefone
        senha = senha
        comando_sql = f'select * from Usuarios'
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        contador=0
        for i in lista:
            if cpf_cnpj == i[0]:
                contador=1
                messagebox.showinfo('', 'User já cadastrado')
                break
        if contador == 0:
            obj_cadastros = Usuario(cpf_cnpj, nome, dataNasc, telefone, senha)
            comando_sql = f"insert into Usuarios (cpf_cnpj, nome, dataNasc, telefone, senha) value ('{obj_cadastros.cpf_cnpj}','{obj_cadastros.nome}','{obj_cadastros.dataNasc}','{obj_cadastros.telefone}', '{obj_cadastros.senha}')"
            self.mycursor.execute(comando_sql)
            self.conexao.commit()
            messagebox.showinfo('', 'User foi cadastrado')
    
    #Inserção de moeda
    def cadastro_movimentacao(self, cod, nome_atk, nome_moeda, capital, meses, montante):
        self.cod = cod
        self.nome_atk = nome_atk
        self.nome_moeda = nome_moeda
        self.capital = capital 
        self.meses = meses
        self.montante = montante
        comando_sql = f'insert into Movimentacoes (cod, nome_atk, nome_moeda, capital, meses, montante) value ("{self.cod}", "{self.nome_atk}", "{self.nome_moeda}", "{self.capital}", "{self.meses}", "{self.montante}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        messagebox.showinfo('', 'Movimentação foi cadastrada')

    #Venda de moeda
    def cadastro_movimentacoes_n(self, cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n):
        self.cod_n = cod_n
        self.nome_atk_n = nome_atk_n
        self.nome_moeda_n = nome_moeda_n
        self.capital_n = capital_n
        self.montante_n = montante_n
        comando_sql = f'insert into Movimentacoes_n (cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n) value ("{self.cod_n}", "{self.nome_atk_n}", "{self.nome_moeda_n}", "{self.capital_n}", "{self.montante_n}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        messagebox.showinfo('', 'Movimentação foi cadastrada')

    def saldo_conta(self, user):
        comando_sql = f'select sum(montante) from movimentacoes where (nome_moeda = "DOLAR" or nome_moeda = "DÓLAR") and nome_atk = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        a = lista[0]
        comando_sql = f'select sum(montante_n) from movimentacoes_n where (nome_moeda_n = "DOLAR" or nome_moeda_n = "DÓLAR") and nome_atk_n = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        b = lista[0]
        if a[0] == None and b[0] != None:
            self.dolar=(b[0])
        elif a[0] != None and b[0] == None:
            self.dolar=(a[0])
        elif a[0] == None and b[0] == None:
            self.dolar=0.0
        elif a[0] != None and b[0] != None:
            self.dolar=(a[0])-(b[0])
        else:
            pass
        
        comando_sql = f'select sum(montante) from movimentacoes where nome_moeda = "EURO" and nome_atk = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        c = lista[0]
        comando_sql = f'select sum(montante_n) from movimentacoes_n where nome_moeda_n = "EURO" and nome_atk_n = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        d = lista[0]
        if c[0] == None and d[0] != None:
            self.euro=(d[0])
        elif c[0] != None and d[0] == None:
            self.euro=(c[0])
        elif c[0] == None and d[0] == None:
            self.euro=0.0
        elif c[0] != None and d[0] != None:
            self.euro=(c[0])-(d[0])
        else:
            pass

        comando_sql = f'select sum(montante) from movimentacoes where nome_moeda = "LIBRA" and nome_atk = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        e = lista[0]
        comando_sql = f'select sum(montante_n) from movimentacoes_n where nome_moeda_n = "LIBRA" and nome_atk_n = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        f = lista[0]
        if e[0] == None and f[0] != None:
            self.libra=(f[0])
        elif e[0] != None and f[0] == None:
            self.libra=(e[0])
        elif e[0] == None and f[0] == None:
            self.libra=0.0
        elif e[0] != None and f[0] != None:
            self.libra=(e[0])-(f[0])
        else:
            pass

        comando_sql = f'select sum(montante) from movimentacoes where nome_moeda = "BITCOIN" and nome_atk = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        g = lista[0]
        comando_sql = f'select sum(montante_n) from movimentacoes_n where nome_moeda_n = "BITCOIN" and nome_atk_n = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        h = lista[0]
        if g[0] == None and h[0] != None:
            self.bitcoin=(h[0])
        elif g[0] != None and h[0] == None:
            self.bitcoin=(g[0])
        elif g[0] == None and h[0] == None:
            self.bitcoin=0.0
        elif g[0] != None and h[0] != None:
            self.bitcoin=(g[0])-(h[0])
        else:
            pass

        comando_sql = f'select sum(montante) from movimentacoes where nome_moeda = "ETHEREUM" and nome_atk = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        i = lista[0]
        comando_sql = f'select sum(montante_n) from movimentacoes_n where nome_moeda_n = "ETHEREUM" and nome_atk_n = "{user}"';
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        j = lista[0]
        if i[0] == None and j[0] != None:
            self.ethereum=(j[0])
        elif i[0] != None and j[0] == None:
            self.ethereum=(i[0])
        elif i[0] == None and j[0] == None:
            self.ethereum=0.0
        elif i[0] != None and j[0] != None:
            self.ethereum=(i[0])-(j[0])
        else:
            pass
        #comando_sql = f'select sum(montante) from movimentacoes where nome_moeda = "DOLAR" or nome_moeda = "DÓLAR"';
        # 
        #self.euro = 
        #self.libra = 
        #self.bitcoin = 
        #self.ethereum = 