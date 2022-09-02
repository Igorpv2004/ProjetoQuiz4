import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao() # abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar()
        self.con = self.db_connection.cursor()#navegacao no banco de dados

    def inserir(self, nome, pontuacao, tema):
        try:
            sql = "insert into Cadastro(codigo, nome, pontuacao,tema) " \
                  "values ('' , '{}' , '{}' , '{}')".format(nome, pontuacao, tema)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha(s) afestada(s).".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def excluir(self, cod):
        try:
            sql = "delete from Cadastro where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "select * from Cadastro"
            self.con.execute(sql)
            msg = ""

            for (codigo, nome, pontuacao, tema) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Pontuação: {}, Tema: {}".format(codigo, nome, pontuacao, tema)

            return msg
        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update Cadastro set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro