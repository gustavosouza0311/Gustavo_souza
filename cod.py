import av5
import time

while True:
    print("""|-----------------------------|
|                             |
|       { MENU PRINCIPAL }    |
|                             |
|       [ 1 ] Inserir         |
|       [ 2 ] Listar          |
|       [ 3 ] Excluir         |
|       [ 4 ] Sair            |
|                             |
|-----------------------------|""")
    time.sleep (1)
    resposta = int(input("Escolha o que você quer fazer : "))
    if resposta >4 and resposta>1: 
        while True:
            resposta = int(input("Escolha um número valido: "))
            if resposta >4 and resposta>1: 
                print("Perdeu 67 mil de aura ;-;")

            else: 
                break

