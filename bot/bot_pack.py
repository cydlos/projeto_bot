class Bot_pack:
    def bot(self):
        lista = []
        arquivo = "bot.txt"
        with open(arquivo) as obj:
            conteudos = obj.readlines()
        for x in conteudos:
            lista.append(x)
        return lista


if __name__ == "__main__":
    # Não existe a função __init__, é preciso inicializar com Bot_pack()
    testando = Bot_pack().bot()
    if "Brasil" in testando:
        print("br")
    else:
        print(testando)