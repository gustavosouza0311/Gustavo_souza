import av5
import time
import mysql.connector
import sqlite3
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional
import os
from dotenv import load_dotenv


while True:
    print("""|===============================|
|                               |
|        {  DATABASE  }         |
|                               |
|        [ 1 ] SQL LITE         |
|        [ 2 ] MY SQL           |
|        [ 3 ] SAIR             |
|                               |
|===============================|""")
    time.sleep (1)
    resposta1 = int(input("Escolha o que você quer fazer : "))
    if resposta1 >3 or resposta1 <1: 
        while True:
            resposta = int(input("Escolha um número valido: "))
            if resposta1 >3 or resposta1 <1: 
                print("Perdeu 67 mil de aura ;-;")
                break
            else: 
                break
    if resposta1 == 1:
        class Base(DeclarativeBase):
            pass
        
        
        class Pessoa(Base):
            
            __tablename__ = "jogo"
        
            id: Mapped[int] = mapped_column(primary_key=True)
            nome: Mapped[str] = mapped_column(String(250))
            empresa: Mapped[str] = mapped_column(String(250))
            quantidade: Mapped[str] = mapped_column(String(250))
            lancamento: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
         
        engine = create_engine("sqlite:///jogo.db")
        
        
        Base.metadata.create_all(engine)
        
        with Session(engine) as session:
        
            p = Pessoa(nome="NOME DO JOGO", 
                       empresa="NOME DA EMPRESA",
                       quantidade="QUANTIDADE DE MUSICAS NESSE JOGO",
                       lancamento="DATA DE LANCAMENTO DESSE JOGO")
        
            session.add(p)
                
            session.commit()
        
            print("TUDO CERTO")
        
        
        class Base(DeclarativeBase):
            pass
        
        
        class Pessoa02(Base):
            
            __tablename__ = "musicas"
        
            id: Mapped[int] = mapped_column(primary_key=True)
            bandas: Mapped[str] = mapped_column(String(250))
            cantores: Mapped[str] = mapped_column(String(250))
            quantidade: Mapped[str] = mapped_column(String(250))
            tempo: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
        
        engine = create_engine("sqlite:///jogo.db")
        
        
        Base.metadata.create_all(engine)
        
        with Session(engine) as session:
        
            p = Pessoa02(bandas="NOME DAS BANDAS", 
                         cantores="NOME DOS CANTORES",
                         quantidade="QUANTIDADE DE MUSICAS NESSE JOGO",
                         tempo="TEMPO DE MUSICA DESSE JOGO(AO TOTAL)")
        
            session.add(p)
                
            session.commit()
            conexao = sqlite3.connect("jogo.db")
        
        load_dotenv()

        # buscando as variáveis de ambiente
meus dados estao no meu env.



        print("Conectado ao MySQL!")

        print("""|-----------------------------|
|                             |
|      { MENU DE OPÇÕES  }    |
|                             |
|       [ 1 ] Inserir         |
|       [ 2 ] Listar          |
|       [ 3 ] Excluir         |
|       [ 4 ] Sair            |
|                             |
|-----------------------------|""")
        time.sleep (1)
        resposta2 = int(input("Escolha o que você quer fazer : "))
        if resposta2 >4 or resposta2<1: 
            while True:
                resposta2 = int(input("Escolha um número valido: "))
                if resposta2 >4 or resposta2<1: 
                    print("Perdeu 67 mil de aura ;-;")
                    break
                else: 
                    break
            if resposta2 == 1:
                sql = "INSERT INTO pessoas (nome, idade) VALUES (%s, %s)"

                dados = ("João", 25)

                sqlite3.Cursor.execute(sql, dados)

                conexao.commit()
            if resposta2 == 2:
                print ("o curso")
            if resposta2 == 3:
                print ("urso sem o curso")
            if resposta2 == 4:
                conexao.close()
                break
    if resposta1 == 2:
       vai estar junto com o env.
        
        
        conexao = mysql.connector.connect(engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
        )

        )
            
        print("""|-----------------------------|
        |                             |
        |      { MENU DE OPÇÕES  }    |
        |                             |     
        |       [ 1 ] Inserir         |
        |       [ 2 ] Listar          |
        |       [ 3 ] Excluir         |
        |       [ 4 ] Sair            |
        |                             |
        |-----------------------------|""")

        time.sleep (1)
        resposta2 = int(input("Escolha o que você quer fazer : "))
        if resposta2 >4 or resposta2<1: 
            while True:
                resposta2 = int(input("Escolha um número valido: "))
                if resposta2 >4 or resposta2<1: 
                    print("Perdeu 67 mil de aura ;-;")
                    break
        
        else: 
            break
        if resposta2 == 1:
            print ("clubex")
        if resposta2 == 2:
            print ("o curso")
        if resposta2 == 3:
           print ("urso sem o curso")
        if resposta2 == 4:
                break
    if resposta1 == 3:
        break

