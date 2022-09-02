from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()
        self.opcao1 = 0

    def getOpcao1(self):
        return self.opcao1

    def setOpcao1(self, opcao1):
        self.opcao1 = opcao1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\nEscolha uma das alternativas abaixo: "
              "\n0. Sair"  +
              "\n1. Jogar" +
              "\n2. Consultar"+
              "\n3. Atualizar Nome" +
              "\n4. Excluir")
        self.setOpcao(int(input()))

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo nome")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))

    def excluir(self):
        print("Informe o código do dado que deseja excluir: ")
        cod = int(input())
        print(self.modelo.excluir(cod))

    def menuTema(self):
        print("Escolha o tema em qual deseja jogar: \n"
              "\n1.Futebol" +
              "\n2.Animais" +
              "\n3.Tecnologia" +
              "\n4.Geografia" +
              "\n5.Conhecimentos Gerais" +
              "\n6.História do Brasil")
        self.setOpcao1(int(input()))


    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
                break
            elif self.getOpcao() == 1:
                self.menuTema()
                if self.getOpcao1() == 1:
                    self.jogo()
                elif self.getOpcao1() == 2:
                    self.jogo1()
                elif self.getOpcao1() == 3:
                    self.jogoTI()
                elif self.getOpcao1() == 4:
                    self.jogo2()
                elif self.getOpcao1() == 5:
                    self.jogo0()
                elif self.getOpcao1() == 6:
                    self.jogo3()
                else:
                    print("Opção inválida!!!")
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                self.atualizarNome()

            elif self.getOpcao() == 4:
                self.excluir()

        else:
            print("Opção inválida.")



    def jogo0(self):
        tema = "Conhecimentos Gerais"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print(
            "1. Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue? \n"
            "\n1. Tem entre 2 a 4 litros. São retirados 450 mililitros" +
            "\n2. Tem entre 4 a 6 litros. São retirados 450 mililitros" +
            "\n3. Tem 10 litros. São retirados 2 litros" +
            "\n4. Tem 7 litros. São retirados 1,5 litros")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print(
                "1. Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue? \n"
                "\n1. Tem entre 2 a 4 litros. São retirados 450 mililitros" +
                "\n2. Tem entre 4 a 6 litros. São retirados 450 mililitros" +
                "\n3. Tem 10 litros. São retirados 2 litros" +
                "\n4. Tem 7 litros. São retirados 1,5 litros")
            resposta = int(input())
        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta errada!")

        print("2.De quem é a famosa frase “Penso, logo existo”? \n"
              "\n1. Platão" +
              "\n2. Galileu Galilei" +
              "\n3. Descartes" +
              "\n4. Sócrates")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.De quem é a famosa frase “Penso, logo existo”? \n"
                  "\n1. Platão" +
                  "\n2. Galileu Galilei" +
                  "\n3. Descartes" +
                  "\n4. Sócrates")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta errada!")
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 4:
            print("Resposta errada!")

        print("3.De onde é a invenção do chuveiro elétrico? \n" +
              "\n1. França " +
              "\n2. Inglaterra " +
              "\n3. Brasil " +
              "\n4. Austrália")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.De onde é a invenção do chuveiro elétrico? \n" +
                  "\n1. França " +
                  "\n2. Inglaterra " +
                  "\n3. Brasil " +
                  "\n4. Austrália")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta3 == 4:
            print("Resposta errada!")
        print("4.Quais o menor e o maior país do mundo? \n"
              "\n1. Vaticano e Rússia" +
              "\n2. Nauru e China" +
              "\n3. Mônaco e Canadá" +
              "\n4. Malta e Estados Unidos")
        resposta4 = int(input())
        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Quais o menor e o maior país do mundo? \n"
                  "\n1. Vaticano e Rússia" +
                  "\n2. Nauru e China" +
                  "\n3. Mônaco e Canadá" +
                  "\n4. Malta e Estados Unidos")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 2:
            print("Resposta errada!")
        elif resposta4 == 3:
            print("Resposta errada!")
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5. Qual o nome do presidente do Brasil que ficou conhecido como Jango? \n"
              "\n1. Jânio Quadros" +
              "\n2. Jacinto Anjos" +
              "\n3. Getúlio Vargas" +
              "\n4. João Goulart")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5. Qual o nome do presidente do Brasil que ficou conhecido como Jango? \n"
                  "\n1. Jânio Quadros" +
                  "\n2. Jacinto Anjos" +
                  "\n3. Getúlio Vargas" +
                  "\n4. João Goulart")
            resposta5 = int(input())
        if resposta5 == 1:
            print("Resposta errada!")
        elif resposta5 == 2:
            print("Resposta Errada!")
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("6.Qual o grupo em que todas as palavras foram escritas corretamente? \n"
              "\n1. Asterístico, beneficiente, meteorologia, entertido" +
              "\n2. Asterisco, beneficente, meteorologia, entretido" +
              "\n3. Asterisco, beneficente, metereologia, entretido" +
              "\n4. Asterístico, beneficiente, metereologia, entretido")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Qual o grupo em que todas as palavras foram escritas corretamente? \n"
                  "\n1. Asterístico, beneficiente, meteorologia, entertido" +
                  "\n2. Asterisco, beneficente, meteorologia, entretido" +
                  "\n3. Asterisco, beneficente, metereologia, entretido" +
                  "\n4. Asterístico, beneficiente, metereologia, entretido")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 3:
            print("Resposta errada!")
        elif resposta6 == 4:
            print("Resposta errada!")

        print("7.Qual o livro mais vendido no mundo a seguir à Bíblia? \n"
              "\n1. O Senhor dos Anéis" +
              "\n2. Dom Quixote" +
              "\n3. O Pequeno Príncipe" +
              "\n4. Ela, a Feiticeira")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Qual o livro mais vendido no mundo a seguir à Bíblia? \n"
                  "\n1. O Senhor dos Anéis" +
                  "\n2. Dom Quixote" +
                  "\n3. O Pequeno Príncipe" +
                  "\n4. Ela, a Feiticeira")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Quantas casas decimais tem o número pi? \n"
              "\n1. Duas" +
              "\n2. Centenas" +
              "\n3. Infinitas" +
              "\n4. Vinte")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Quantas casas decimais tem o número pi? \n"
                  "\n1. Duas" +
                  "\n2. Centenas" +
                  "\n3. Infinitas" +
                  "\n4. Vinte")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta8 == 4:
            print("Resposta errada!")

        print("9.Atualmente, quantos elementos químicos a tabela periódica possui? \n"
              "\n1. 113" +
              "\n2. 109" +
              "\n3. 108" +
              "\n4. 118")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Atualmente, quantos elementos químicos a tabela periódica possui? \n"
                  "\n1. 113" +
                  "\n2. 109" +
                  "\n3. 108" +
                  "\n4. 118")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta correta!")
            contador = contador + 1
        print("10.Quais os países que têm a maior e a menor expectativa de vida do mundo? \n"
              "\n1. Japão e Serra Leoa" +
              "\n2. Austrália e Afeganistão" +
              "\n3. Itália e Chade" +
              "\n4. Brasil e Congo")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Quais os países que têm a maior e a menor expectativa de vida do mundo? \n"
                  "\n1. Japão e Serra Leoa" +
                  "\n2. Austrália e Afeganistão" +
                  "\n3. Itália e Chade" +
                  "\n4. Brasil e Congo")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 2:
            print("Resposta errada!")
        elif resposta10 == 3:
            print("Resposta errada!")
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)

    def jogo2(self):
        tema = "Geografia"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1. A capital do Brasil é: \n"
              "\n1. Rio De Janeiro " +
              "\n2. Brasília" +
              "\n3. São Paulo" +
              "\n4. Brazilia")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1. A capital do Brasil é: \n"
                  "\n1. Rio De Janeiro " +
                  "\n2. Brasília" +
                  "\n3. São Paulo" +
                  "\n4. Brazilia")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta errada!")

        # ---------------------------------------------------------------------------------------------------------------

        print("2.A capital da russia é ? \n"
              "\n1. Moscou" +
              "\n2. Kiev" +
              "\n3. Texas" +
              "\n4. Caracas")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.A capital da russia é ? \n"
                  "\n1. Moscou" +
                  "\n2. Kiev" +
                  "\n3. Texas" +
                  "\n4. Caracas")
            resposta2 = int(input())

        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta errada!")
        elif resposta2 == 4:
            print("Resposta errada!")

        # -----------------------------------------------------------------------------------------------------------------

        print("3.O estado do Brasil que tem maior números de habitantes é? \n" +
              "\n1. Ceará" +
              "\n2. Brasília" +
              "\n3. Amazonas" +
              "\n4. São Paulo")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.O estado do Brasil que tem maior números de habitantes é? \n" +
                  "\n1. Ceará " +
                  "\n2. Brasília" +
                  "\n3. Amazonas" +
                  "\n4. São Paulo")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta errada!")
        elif resposta3 == 4:
            print("Resposta correta!")
            contador = contador + 1
        # ------------------------------------------------------------------------------------------------------------------------

        print("4.A frança fica no ? \n"
              "\n1. Hemisfério Sul" +
              "\n2. Hemisfério Norte" +
              "\n3. Hemisfério Leste" +
              "\n4. Hemisfério Oeste")
        resposta4 = int(input())

        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.A frança fica no ? \n"
                  "\n1. Hemisfério Sul" +
                  "\n2. Hemisfério Norte" +
                  "\n3. Hemisfério Leste" +
                  "\n4. Hemisfério Oeste")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 3:
            print("Resposta errada!")
        elif resposta4 == 4:
            print("Resposta errada!")

        # ----------------------------------------------------------------------------------------------------------------------------

        print("5.A nação mais rica no mundo é? \n"
              "\n1. Brasil" +
              "\n2. Estados Unidos" +
              "\n3. China" +
              "\n4. Rússia")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.A nação mais rica no mundo é? \n"
                  "\n1. Brasil" +
                  "\n2. Estados Unidos" +
                  "\n3. China" +
                  "\n4. Rússia")
            resposta5 = int(input())

        if resposta5 == 1:
            print("Resposta Errada!")
        elif resposta5 == 2:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta Errada!")

        # ------------------------------------------------------------------------------------------------------------------

        print("6.O clima do estado do amazonas é? \n"
              "\n1. Semi Árido" +
              "\n2. Sub Tropical" +
              "\n3. Tropical" +
              "\n4. Desértico")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.O clima do estado do amazonas é? \n"
                  "\n1. Semi Árido" +
                  "\n2. Sub Tropical" +
                  "\n3. Tropical" +
                  "\n4. Desértico")
            resposta6 = int(input())

        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 4:
            print("Resposta errada!")

        # -------------------------------------------------------------------------------------------------------------------------

        print("7.A África é ? \n"
              "\n1. País" +
              "\n2. Planeta" +
              "\n3. Estado" +
              "\n4. Continente")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.A África é ? \n"
                  "\n1. País" +
                  "\n2. Planeta" +
                  "\n3. Estado" +
                  "\n4. Continente")
            resposta7 = int(input())

        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta errada!")
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta correta!")
            contador = contador + 1

        # ----------------------------------------------------------------------------------------------------------------------

        print("8.O bioma predominante no ceará é? \n"
              "\n1. Cerrado" +
              "\n2. Caatinga" +
              "\n3. Mata Atlântica" +
              "\n4. Amazônia")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.O bioma predominante no ceará é? \n"
                  "\n1. Cerrado" +
                  "\n2. Caatinga" +
                  "\n3. Mata Atlântica" +
                  "\n4. Amazônia")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta errada!")

        # -------------------------------------------------------------------------------------------------------

        print("9.Qual o país mais populoso do hemisfério sul? \n"
              "\n1. Indonésia" +
              "\n2. Austrália" +
              "\n3. Brasil " +
              "\n4. África do Sul")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Qual o país mais populoso do hemisfério sul? \n"
                  "\n1. Indonésia" +
                  "\n2. Austrália" +
                  "\n3. Brasil " +
                  "\n4. África do Sul")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta errada!")

        # --------------------------------------------------------------------------------------------------------------------

        print("10.Qual é o maior país do mundo ? \n"
              "\n1. Brasil" +
              "\n2. Rússia" +
              "\n3. Estados Unidos" +
              "\n4. Inglaterra")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Qual é o maior país do mundo ? \n"
                  "\n1. Brasil" +
                  "\n2. Rússia" +
                  "\n3. Estados Unidos" +
                  "\n4. Inglaterra")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta errada!")
        elif resposta10 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 3:
            print("Resposta correta!")
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)
        # ----------------------------------------------------------------------------------------------------------------------

    def jogo1(self):
        tema = "Animais"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Qual o maior animal do planeta? \n"
              "\n1. Tubarão Branco" +
              "\n2. Baleia Azul" +
              "\n3. Girafa" +
              "\n4. Rinoceronte")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Qual o maior animal do planeta? \n"
                  "\n1. Tubarão Branco" +
                  "\n2. Baleia Azul" +
                  "\n3. Girafa" +
                  "\n4. Rinoceronte")
            resposta = int(input())
        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta errada!")

        print("2.Qual o animal mais rápido do mundo? \n"
              "\n1. Tigre" +
              "\n2. Leão" +
              "\n3. Guepardo" +
              "\n4. Cavalo")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.Qual o animal mais rápido do mundo? \n"
                  "\n1. Tigre" +
                  "\n2. Leão" +
                  "\n3. Guepardo" +
                  "\n4. Cavalo")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta errada!")
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 4:
            print("Resposta errada!")

        print("3.Qual é o animal mais alto do mundo? \n" +
              "\n1. Elefante africano " +
              "\n2. Baleia Azul" +
              "\n3. Lula colossal" +
              "\n4. Girafa")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Qual é o animal mais alto do mundo? \n" +
                  "\n1. Elefante africano "
                  "\n2. Baleia Azul"
                  "\n3. Lula colossal"
                  "\n4. Girafa")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta errada!")
        elif resposta3 == 4:
            print("Resposta correta!")
            contador = contador + 1
        print("4.Qual é o tempo médio de vida de um cão? \n"
              "\n1. 3-5 anos" +
              "\n2. 10-13 anos" +
              "\n3. 14-20 anos" +
              "\n4. 20-25 anos")
        resposta4 = int(input())
        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual é o tempo médio de vida de um cão? \n"
                  "\n1. 3-5 anos" +
                  "\n2. 10-13 anos" +
                  "\n3. 14-20 anos" +
                  "\n4. 20-25 anos")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 3:
            print("Resposta errada!")
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5.Qual o mecanismo de defesa de um gambá? \n"
              "\n1. Peidos com cheiro fétido" +
              "\n2. Mordidas Fatais" +
              "\n3. Saliva venenosa" +
              "\n4. Garras afiada")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.Qual o mecanismo de defesa de um gambá? \n"
                  "\n1. Peidos com cheiro fétido" +
                  "\n2. Mordidas Fatais" +
                  "\n3. Saliva venenosa" +
                  "\n4. Garras afiada")
            resposta5 = int(input())
        if resposta5 == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta5 == 2:
            print("Resposta Errada!")
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta Errada!")

        print("6.Que animal pode viver por semanas sem cabeça ou cérebro? \n"
              "\n1. Aranha" +
              "\n2. Formigas" +
              "\n3. Barata" +
              "\n4. Gafanhoto")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Que animal pode viver por semanas sem cabeça ou cérebro? \n"
                  "\n1. Aranha" +
                  "\n2. Formigas" +
                  "\n3. Barata" +
                  "\n4. Gafanhoto")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 4:
            print("Resposta errada!")

        print("7.Que animal não precisa beber água a vida inteira? \n"
              "\n1. Camelo" +
              "\n2. Pequeno rato canguru" +
              "\n3. Coruja" +
              "\n4. Elefante")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Que animal não precisa beber água a vida inteira? \n"
                  "\n1. Camelo" +
                  "\n2. Pequeno rato canguru" +
                  "\n3. Coruja" +
                  "\n4. Elefante")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Que animal é o único que não consegue saltar? \n"
              "\n1. Suínos" +
              "\n2. Baleias" +
              "\n3. Girafas" +
              "\n4. Elefantes")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Que animal é o único que não consegue saltar? \n"
                  "\n1. Suínos" +
                  "\n2. Baleias" +
                  "\n3. Girafas" +
                  "\n4. Elefantes")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("9.Onde está o coração do camarão? \n"
              "\n1. Em seu peito" +
              "\n2. Em sua cabeça" +
              "\n3. Em suas caudas" +
              "\n4. Em suas pernas")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Onde está o coração do camarão? \n"
                  "\n1. Em seu peito" +
                  "\n2. Em sua cabeça" +
                  "\n3. Em suas caudas" +
                  "\n4. Em suas pernas")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta errada!")

        print("10.Qual dos seguintes animais pode voar ? \n"
              "\n1. Pinguins" +
              "\n2. Patos" +
              "\n3. Coruja" +
              "\n4. Foca")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Qual dos seguintes animais pode voar ? \n"
                  "\n1. Pinguins" +
                  "\n2. Patos" +
                  "\n3. Coruja" +
                  "\n4. Foca")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta errada!")
        elif resposta10 == 2:
            print("Resposta errada!")
        elif resposta10 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)

    def jogoTI(self):
        tema = "Tecnologia"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Qual destes passwords foi o mais usado na internet? \n"
              "\n1. senha123" +
              "\n2. a1b2c3" +
              "\n3. abcdef" +
              "\n4. 123456")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Qual destes passwords foi o mais usado na internet? \n"
                  "\n1. senha123" +
                  "\n2. a1b2c3" +
                  "\n3. abcdef" +
                  "\n4. 123456")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta errada!")
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta correta!")
            contador = contador + 1


        print("2.O que significa a sigla “WWW” na internet? \n"
              "\n1. World wide web" +
              "\n2. Web world wide" +
              "\n3. Web wide world" +
              "\n4. Wide web world")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.O que significa a sigla “WWW” na internet? \n"
                  "\n1. World wide web" +
                  "\n2. Web world wide" +
                  "\n3. Web wide world" +
                  "\n4. Wide web world")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta errada!")
        elif resposta2 == 4:
            print("Resposta errada!")

        print("3.Qual foi o primeiro tweet da história? \n" +
              "\n1. Olá, Mundo! " +
              "\n2. Olá, Twitter!" +
              "\n3. Estou Preparando meu Twitter" +
              "\n4. Olá, Humanos!")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Qual foi o primeiro tweet da história? \n" +
                  "\n1. Olá, Mundo! " +
                  "\n2. Olá, Twitter!" +
                  "\n3. Estou Preparando meu Twitter" +
                  "\n4. Olá, Humanos!")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta3 == 4:
            print("Resposta errada!")

        print("4.Qual foi a duração do primeiro vídeo do Youtube? \n"
              "\n1. 3 minutos"+
              "\n2. 1 minutos"+
              "\n3. 18 segundos"+
              "\n4. 2 minutos")
        resposta4 = int(input())
        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual foi a duração do primeiro vídeo do Youtube? \n"
                  "\n1. 3 minutos" +
                  "\n2. 1 minutos" +
                  "\n3. 18 segundos" +
                  "\n4. 2 minutos")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta errada!")
        elif resposta4 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5.Em média, quantas pesquisas totalmente novas são feitas no Google por dia? \n"
              "\n1. 450 milhôes" +
              "\n2. 1 bilhão" +
              "\n3. 300 milhôes"+
              "\n4. 500 mil")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.Em média, quantas pesquisas totalmente novas são feitas no Google por dia? \n"
                  "\n1. 450 milhôes" +
                  "\n2. 1 bilhão" +
                  "\n3. 300 milhôes" +
                  "\n4. 500 mil")
            resposta5 = int(input())
        if resposta5 == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta5 == 2:
            print("Resposta Errada!")
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta Errada!")

        print("6.Qual foi a primeira rede social da história da internet? \n"
              "\n1. Youtube" +
              "\n2. Orkut" +
              "\n3. Facebook" +
              "\n4. Classmate")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Qual foi a primeira rede social da história da internet? \n"
                  "\n1. Youtube" +
                  "\n2. Orkut" +
                  "\n3. Facebook" +
                  "\n4. Classmate")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta errada!")
        elif resposta6 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("7.Quando foi criado o primeiro smartphone da história? \n"
              "\n1. 2000" +
              "\n2. 1994" +
              "\n3. 1999" +
              "\n4. 1990")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Quando foi criado o primeiro smartphone da história? \n"
                  "\n1. 2000" +
                  "\n2. 1994" +
                  "\n3. 1999" +
                  "\n4. 1990")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Qual o nome do ataque cibernético que atingiu computadores no mundo todo este ano? \n"
              "\n1. WannaSpy" +
              "\n2. WannaFly" +
              "\n3. WannaCry" +
              "\n4. Anonymous")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Qual o nome do ataque cibernético que atingiu computadores no mundo todo este ano? \n"
                  "\n1. WannaSpy" +
                  "\n2. WannaFly" +
                  "\n3. WannaCry" +
                  "\n4. Anonymous")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta8 == 4:
            print("Resposta errada!")

        print("9.Qual a resolução de uma imagem Full HD? \n"
              "\n1. 1920 x 1080" +
              "\n2. 1280 x 720" +
              "\n3. 2560 x 1440" +
              "\n4. 1080 x 700")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Qual a resolução de uma imagem Full HD? \n"
                  "\n1. 1920 x 1080" +
                  "\n2. 1280 x 720" +
                  "\n3. 2560 x 1440" +
                  "\n4. 1080 x 700")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta errada!")

        print("10.Quantos bits cabem em um byte? \n"
              "\n1. 12 bits" +
              "\n2. 1024 bits" +
              "\n3. 8 bits" +
              "\n4. 1 bit")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Quantos bits cabem em um byte? \n"
                  "\n1. 12 bits" +
                  "\n2. 1024 bits" +
                  "\n3. 8 bits" +
                  "\n4. 1 bit")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta errada!")
        elif resposta10 == 2:
            print("Resposta errada!")
        elif resposta10 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)


    def jogo1(self):
        tema = "Animais"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Qual o maior animal do planeta? \n"
              "\n1. Tubarão Branco" +
              "\n2. Baleia Azul" +
              "\n3. Girafa" +
              "\n4. Rinoceronte")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Qual o maior animal do planeta? \n"
                  "\n1. Tubarão Branco" +
                  "\n2. Baleia Azul" +
                  "\n3. Girafa" +
                  "\n4. Rinoceronte")
            resposta = int(input())
        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta errada!")


        print("2.Qual o animal mais rápido do mundo? \n"
              "\n1. Tigre" +
              "\n2. Leão" +
              "\n3. Guepardo" +
              "\n4. Cavalo")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.Qual o animal mais rápido do mundo? \n"
                  "\n1. Tigre" +
                  "\n2. Leão" +
                  "\n3. Guepardo" +
                  "\n4. Cavalo")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta errada!")
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 4:
            print("Resposta errada!")

        print("3.Qual é o animal mais alto do mundo? \n" +
              "\n1. Elefante africano " +
              "\n2. Baleia Azul" +
              "\n3. Lula colossal" +
              "\n4. Girafa")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Qual é o animal mais alto do mundo? \n" +
                  "\n1. Elefante africano "
                  "\n2. Baleia Azul"
                  "\n3. Lula colossal"
                  "\n4. Girafa")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta errada!")
        elif resposta3 == 4:
            print("Resposta correta!")
            contador = contador + 1
        print("4.Qual é o tempo médio de vida de um cão? \n"
              "\n1. 3-5 anos"+
              "\n2. 10-13 anos"+
              "\n3. 14-20 anos"+
              "\n4. 20-25 anos")
        resposta4 = int(input())
        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual é o tempo médio de vida de um cão? \n"
                  "\n1. 3-5 anos" +
                  "\n2. 10-13 anos" +
                  "\n3. 14-20 anos"+
                  "\n4. 20-25 anos")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 3:
            print("Resposta errada!")
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5.Qual o mecanismo de defesa de um gambá? \n"
              "\n1. Peidos com cheiro fétido" +
              "\n2. Mordidas Fatais" +
              "\n3. Saliva venenosa"+
              "\n4. Garras afiada")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.Qual o mecanismo de defesa de um gambá? \n"
                  "\n1. Peidos com cheiro fétido" +
                  "\n2. Mordidas Fatais" +
                  "\n3. Saliva venenosa" +
                  "\n4. Garras afiada")
            resposta5 = int(input())
        if resposta5 == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta5 == 2:
            print("Resposta Errada!")
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta Errada!")

        print("6.Que animal pode viver por semanas sem cabeça ou cérebro? \n"
              "\n1. Aranha" +
              "\n2. Formigas" +
              "\n3. Barata" +
              "\n4. Gafanhoto")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Que animal pode viver por semanas sem cabeça ou cérebro? \n"
                  "\n1. Aranha" +
                  "\n2. Formigas" +
                  "\n3. Barata" +
                  "\n4. Gafanhoto")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 4:
            print("Resposta errada!")

        print("7.Que animal não precisa beber água a vida inteira? \n"
              "\n1. Camelo" +
              "\n2. Pequeno rato canguru" +
              "\n3. Coruja" +
              "\n4. Elefante")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Que animal não precisa beber água a vida inteira? \n"
                  "\n1. Camelo" +
                  "\n2. Pequeno rato canguru" +
                  "\n3. Coruja" +
                  "\n4. Elefante")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Que animal é o único que não consegue saltar? \n"
              "\n1. Suínos" +
              "\n2. Baleias" +
              "\n3. Girafas" +
              "\n4. Elefantes")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Que animal é o único que não consegue saltar? \n"
                  "\n1. Suínos" +
                  "\n2. Baleias" +
                  "\n3. Girafas" +
                  "\n4. Elefantes")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("9.Onde está o coração do camarão? \n"
              "\n1. Em seu peito" +
              "\n2. Em sua cabeça" +
              "\n3. Em suas caudas" +
              "\n4. Em suas pernas")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Onde está o coração do camarão? \n"
                  "\n1. Em seu peito" +
                  "\n2. Em sua cabeça" +
                  "\n3. Em suas caudas" +
                  "\n4. Em suas pernas")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta errada!")

        print("10.Qual dos seguintes animais pode voar ? \n"
              "\n1. Pinguins" +
              "\n2. Patos" +
              "\n3. Coruja" +
              "\n4. Foca")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Qual dos seguintes animais pode voar ? \n"
                  "\n1. Pinguins" +
                  "\n2. Patos" +
                  "\n3. Coruja" +
                  "\n4. Foca")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta errada!")
        elif resposta10 == 2:
            print("Resposta errada!")
        elif resposta10 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)



    def jogo(self):
        tema = "Futebol"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Em que ano nasceu o Corinthians?\n"
              "\n1. 1910"
              "\n2. 1934"
              "\n3. 1951"
              "\n4. 1850")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Em que ano nasceu o Corinthians?\n"
                  "\n1. 1910" +
                  "\n2. 1934" +
                  "\n3. 1951" +
                  "\n4. 1850")
            resposta = int(input())
        if resposta == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta == 2:
            print("Resposta Errada!")
        elif resposta == 3:
            print("Resposta Errada!")
        elif resposta == 4:
            print("Resposta Errada!")

        print("2.Quantos Mundiais o Palmeiras tem?\n" +
              "\n1. Nenhum" +
              "\n2. Um" +
              "\n3. Dois" +
              "\n4. Cinco")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.Quantos Mundiais o Palmeiras tem?\n" +
                  "\n1. Nenhum" +
                  "\n2. Um" +
                  "\n3. Dois" +
                  "\n4. Cinco")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta Errada!")
        elif resposta2 == 3:
            print("Resposta Errada!")
        elif resposta2 == 4:
            print("Resposta Errada!")

        print("3.Quantas copas do mundo o Brasil conquistou? \n" +
              "\n1. Três" +
              "\n2. Duas" +
              "\n3. Cinco" +
              "\n4. Nenhuma")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Quantas copas do mundo o Brasil conquistou? \n" +
                  "\n1. Três" +
                  "\n2. Duas" +
                  "\n3. Cinco" +
                  "\n4. Nenhuma")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta3 == 4:
            print("Resposta errada!")

        print("4.Qual foi o ano em que foi em que o Brasil conquistou a última copa do mundo? \n" +
              "\n1. 1994" +
              "\n2. 1998" +
              "\n3. 2002" +
              "\n4. 2010")
        resposta4 = int(input())

        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual foi o ano em que foi em que o Brasil conquistou a última copa do mundo? \n" +
                  "\n1. 1994" +
                  "\n2. 1998" +
                  "\n3. 2002" +
                  "\n4. 2010")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta errada!")
        elif resposta4 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5. Quem foi o jogador mais jovem a ganhar uma copa do mundo: \n"
              "\n1. Cristiano Ronaldo" +
              "\n2. Pelé" +
              "\n3. Messi" +
              "\n4. Neymar")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5. Quem foi o jogador mais jovem a ganhar uma copa do mundo? \n"
                  "\n1. Cristiano Ronaldo" +
                  "\n2. Pelé" +
                  "\n3. Messi" +
                  "\n4. Neymar")
            resposta5 = int(input())

        if resposta5 == 1:
            print("Resposta errada!")
        elif resposta5 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta5 == 3:
            print("Resposta errada!")
        elif resposta5 == 4:
            print("Resposta errada!")

        print("6.Qual a maior torcida do Brasil? \n" 
              "\n1. Corinthians" +
              "\n2. Palmeiras" +
              "\n3. São Paulo" +
              "\n4. Flamengo")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Qual a maior torcida do Brasil? \n"
                  "\n1. Corinthians" +
                  "\n2. Palmeiras" +
                  "\n3. São Paulo" +
                  "\n4. Flamengo")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta errada!")
        elif resposta6 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("7.Aonde foi disputada a última copa do mundo? \n"
              "\n1. França" +
              "\n2. Rússia" +
              "\n3. Japão" +
              "\n4. Espanha")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Aonde foi disputada a última copa do mundo? \n"
                  "\n1. França" +
                  "\n2. Rússia" +
                  "\n3. Japão" +
                  "\n4. Espanha")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Qual país conquistou a última copa do mundo? \n"
              "\n1. Brasil" +
              "\n2. Alemanha" +
              "\n3. Portugal" +
              "\n4. França")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Qual país conquistou a última copa do mundo? \n"
                  "\n1. Brasil" +
                  "\n2. Alemanha" +
                  "\n3. Portugal" +
                  "\n4. França")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("9.A copa do mundo é disputada a cada quantos anos? \n"
              "\n1. Três Anos" +
              "\n2. Dois Anos" +
              "\n3. Quatro Anos" +
              "\n4. Um Ano")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.A copa do mundo é disputada a cada quantos anos? \n"
                  "\n1. Três Anos" +
                  "\n2. Dois Anos" +
                  "\n3. Quatro Anos" +
                  "\n4. Um Ano")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 4:
            print("Resposta errada!")

        print("10.Quais desses jogadores ainda não conquistaram a bola  de ouro\n"
              "(prêmio de jogador do ano)\n"
              "\n1. Neymar" +
              "\n2. Kaká" +
              "\n3. Ronaldinho Gaúcho" +
              "\n4. Ronaldo Fenômeno")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Quais desses jogadores ainda não conquistaram a bola  de ouro\n"
                  "(prêmio de jogador do ano)\n"
                  "\n1. Neymar" +
                  "\n2. Kaká" +
                  "\n3. Ronaldinho Gaúcho" +
                  "\n4. Ronaldo Fenômeno")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta10 == 2:
            print("Resposta Errada!")
        elif resposta10 == 3:
            print("Resposta Errada!")
        elif resposta10 == 4:
            print("Resposta Errada!")

        print("sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)

    def jogo3(self):
        tema = "História Do Brasil"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.O Tratado de Tordesilhas foi um acordo entre os reinos de Portugal e ...\n"
                "\n1. Grécia"
                "\n2. Alemanha"
                "\n3. Espanha"
                "\n4. Rússia")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.O Tratado de Tordesilhas foi um acordo entre os reinos de Portugal e ...\n"
                    "\n1. Grécia"
                    "\n2. Alemanha"
                    "\n3. Espanha"
                    "\n4. Rússia")
            resposta = int(input())

        if resposta == 1:
            print("Resposta Errada!")
        elif resposta == 2:
            print("Resposta Errada!")
        elif resposta == 3:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta == 4:
            print("Resposta Errada!")
        # ----------------------------------------------------------------------------------------------------------------------------------------
        print("2.O Descobrimento do Brasil foi marcada exatamente no dia 22 de abril de 1500, "
                "com achegada dos portugueses, através de uma expedição liderada por...?\n" +
                "\n1. Pedro Alvarés Cabral " +
                "\n2. Dom Pedro I" +
                "\n3. Pedro Álvares Carvalho" +
                "\n4. Cristovão Colombo")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.O Descobrimento do Brasil foi marcada exatamente no dia 22 de abril de 1500, "
                    "com achegada dos portugueses, através de uma expedição liderada por...?\n" +
                    "\n1. Pedro Alvarés Cabral " +
                    "\n2. Dom Pedro I" +
                    "\n3. Pedro Álvares Carvalho" +
                    "\n4. Cristovão Colombo")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta Errada!")
        elif resposta2 == 3:
            print("Resposta Errada!")
        elif resposta2 == 4:
            print("Resposta Errada!")
        # -------------------------------------------------------------------------------------------------------------------------------------
        print("3.Em que ano a escravidão foi implantada no Brasil? \n" +
                "\n1. 1500" +
                "\n2. 1888" +
                "\n3. 1530" +
                "\n4. 1450")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Em que ano a escravidão foi implantada no Brasil? \n" +
                    "\n1. 1500" +
                    "\n2. 1888" +
                    "\n3. 1530" +
                    "\n4. 1450")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta3 == 4:
            print("Resposta errada!")

        # -----------------------------------------------------------------------------------------------------------------------

        print(
            "4.As Capitanias Hereditárias foram a ___ tentativa da Coroa Portuguesa em ocupar o território brasileiro. \n" +
            "\n1. Primeira" +
            "\n2. Segunda" +
            "\n3. Terceira" +
            "\n4. Oitava")
        resposta4 = int(input())

        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print(
                "4.As Capitanias Hereditárias foram a ___ tentativa da Coroa Portuguesa em ocupar o território brasileiro. \n" +
                "\n1. Primeira" +
                "\n2. Segunda" +
                "\n3. Terceira" +
                "\n4. Oitava")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 2:
            print("Resposta errada!")
        elif resposta4 == 3:
            print("Resposta errada!")

        elif resposta4 == 4:
            print("Resposta errada!")

            # -------------------------------------------------------------------------------------------------------------

        print("5.A primeira capital do Brasil foi ... \n"
                "\n1. São Paulo" +
                "\n2. Rio de Janeiro" +
                "\n3. Brasília" +
                "\n4. Minas Gerais")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.A primeira capital do Brasil foi ... \n"
                      "\n1. São Paulo" +
                      "\n2. Salvador" +
                      "\n3. Brasília" +
                      "\n4. Rio de janeiro")
            resposta5 = int(input())

        if resposta5 == 1:
            print("Resposta errada!")
        elif resposta5 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta5 == 3:
            print("Resposta errada!")
        elif resposta5 == 4:
            print("Resposta errada!")

            # --------------------------------------------------------------------------------------------------------

        print("6.A França Antártica representou uma colônia francesa no "
                  "período do Brasil colonial durante 1555 a 1560, no local que atualmente corresponde a cidade ... \n"
                  "\n1. Do Rio De Janeiro" +
                  "\n2. De Curitiba" +
                  "\n3. De São Paulo" +
                  "\n4. De Salvador")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.A França Antártica representou uma colônia francesa no "
                      "período do Brasil colonial durante 1555 a 1560, no local que atualmente corresponde a cidade ... \n"
                      "\n1. Do Rio De Janeiro" +
                      "\n2. De Curitiba" +
                      "\n3. De São Paulo" +
                      "\n4. De Salvador")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta errada!")
        elif resposta6 == 4:
            print("Resposta errada!")

            # -------------------------------------------------------------------------------------------------------------------

        print("7.A fundação da cidade do Rio de Janeiro aconteceu no ano de ...? \n"
                  "\n1. 1675" +
                  "\n2. 1575" +
                  "\n3. 1665" +
                  "\n4. 1565")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.A fundação da cidade do Rio de Janeiro aconteceu no ano de ...? \n"
                      "\n1. 1675" +
                      "\n2. 1575" +
                      "\n3. 1665" +
                      "\n4. 1565")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta errada!")
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta correta!")
            contador = contador + 1
            # ---------------------------------------------------------------------------------------------------------------------------------------

        print("8.O confronto no período do Brasil colonial entre tropas constituídas por portugueses e "
                  "índios contra franceses e tamoios que teve como motivo expulsar os "
                  "franceses e terminou com a vitória de Portugal tem o nome de...? \n"
                  "\n1. Guerra de Cabo Frio" +
                  "\n2. Guerra dos Cabos" +
                  "\n3. Confronto de Portugal" +
                  "\n4. Guerra de Portugal")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.O confronto no período do Brasil colonial entre tropas constituídas por portugueses e "
                      "índios contra franceses e tamoios que teve como motivo expulsar os "
                      "franceses e terminou com a vitória de Portugal tem o nome de...? \n"
                      "\n1. Guerra de Cabo Frio" +
                      "\n2. Guerra dos Cabos" +
                      "\n3. Confronto de Portugal" +
                      "\n4. Guerra de Portugal")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta errada!")

            # ---------------------------------------------------------------------------------------------------------

        print("9.A União Ibérica é o período da história de Portugal e da colonização do "
                  "Brasil que as coroas portuguesa e ___ se uniram e formaram um único reino dominado pela ___. \n"
                  "\n1. Coroas Portuguesas ... Dominado pela Coreia" +
                  "\n2. Coroas Portuguesas e Holandesa ... Dominado pela Holanda " +
                  "\n3. Coroas Portuguesas e africana .... Dominada pela África" +
                  "\n4. Coroas Portuguesas e espanhola ....Dominada pela Espanha ")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.A União Ibérica é o período da história de Portugal e da colonização do "
                      "Brasil que as coroas portuguesa e ___ se uniram e formaram um único reino dominado pela ___. \n"
                      "\n1. Coroas Portuguesas e coreana ... Dominado pela Coreia" +
                      "\n2. Coroas Portuguesas e Holandesa ... Dominado pela Holanda " +
                      "\n3. Coroas Portuguesas e africana .... Dominada pela África" +
                      "\n4. Coroas Portuguesas e espanhola ....Dominada pela Espanha ")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta correta!")
            contador = contador + 1

            # -------------------------------------------------------------------------------------------------

        print("10.A França ___ representou a segunda tentativa dos franceses de se fixarem no Brasil.\n"
                  "\n1. Equatorial" +
                  "\n2. Equinocial" +
                  "\n3. Americana" +
                  "\n4. Antártica")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.A França ___ representou a segunda tentativa dos franceses de se fixarem no Brasil.\n"
                      "\n1. Equatorial" +
                      "\n2. Equinocial" +
                      "\n3. Americana" +
                      "\n4. Antártica")

            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta Errada!")

        elif resposta10 == 2:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta10 == 3:
            print("Resposta Errada!")
        elif resposta10 == 4:
            print("Resposta Errada!")

        print("sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)




