from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional


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

    print("TUDO CERTO!")
