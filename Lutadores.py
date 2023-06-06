from abc import ABC, abstractmethod
import random


class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.vivo = True
        self.stack = 0
        self.queimado = False
        self.envenenado = False
        self.dano = 5
        self.chance = 0

    def verificarVivo(self, inimigo):
        if inimigo.vida <= 0:
            inimigo.vivo = False
            return True
        else:
            return False


    @abstractmethod
    def socar(self, inimigo):
        pass

    @abstractmethod
    def especial(self, inimigo):
        pass



class Fogo(Personagem):
    def socar(self, inimigo):
        self.dano = 8

        if inimigo.queimado:
            inimigo.vida = inimigo.vida - self.dano - 3
            print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')

        else:
            inimigo.vida = inimigo.vida - self.dano
            print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')
            inimigo.chance = random.randint(0, 100)
            print(inimigo.chance)
            print(self.stack)

            if inimigo.chance == 50:
                print(f'{inimigo.nome} está queimado!!')
                inimigo.queimado = True

            if self.verificarVivo(inimigo):
                print(f'{inimigo.nome} não aguentou o soco e papocou!!')

            if self.stack == 3:
                print('O golpe especial está pronto!!')
            else:
                self.stack += 1

        self.verificarVivo(inimigo)
        print(self.vivo)

    def especial(self, inimigo):
        self.dano = 12


        if self.stack == 3:
            if inimigo.queimado:
                inimigo.vida = inimigo.vida - self.dano - 3
                print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')

            else:
                inimigo.vida = inimigo.vida - self.dano
                print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')
                inimigo.chance = random.randint(0, 100)


                if inimigo.chance > 50:
                    print(f'{inimigo.nome} está queimado!!')
                    inimigo.queimado = True

                if self.verificarVivo(inimigo):
                    print(f'{inimigo.nome} não aguentou o especial e papocou!!')


                else:
                    self.stack = 0

        else:
            print('O especial não está pronto')

        self.verificarVivo(inimigo)
        print(self.vivo)


class Veneno(Personagem):
    def socar(self, inimigo):
        self.dano = 8

        if inimigo.envenenado:
            inimigo.vida = inimigo.vida - self.dano - 3
            print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')

        else:
            inimigo.vida = inimigo.vida - self.dano
            print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')
            inimigo.chance = random.randint(0, 100)
            print(inimigo.chance)
            print(self.stack)

            if inimigo.chance == 50:
                print(f'{inimigo.nome} está envenenado!!')
                inimigo.envenenado = True

            if self.verificarVivo(inimigo):
                print(f'{inimigo.nome} não aguentou o soco e papocou!!')

            if self.stack == 3:
                print('O golpe especial está pronto!!')
            else:
                self.stack += 1

        self.verificarVivo(inimigo)
        print(self.vivo)

    def especial(self, inimigo):
        self.dano = 12


        if self.stack == 3:
            if inimigo.envenenado:
                inimigo.vida = inimigo.vida - self.dano - 3
                print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')

            else:
                inimigo.vida = inimigo.vida - self.dano
                print(f'{inimigo.nome} sofreu {self.dano} de dano e está com {inimigo.vida} de vida')
                inimigo.chance = random.randint(0, 100)

                if inimigo.chance > 30:
                    print(f'{inimigo.nome} está envenenado!!')
                    inimigo.envenenado = True

                if self.verificarVivo(inimigo):
                    print(f'{inimigo.nome} não aguentou o especial e papocou!!')

                else:
                    self.stack = 0


        else:
            print('O especial não está pronto')

        self.verificarVivo(inimigo)
        print(self.vivo)


def criarPersonagem(nome, tipo):
    if tipo == 'fogo':
        player = Fogo(nome)
        return player

    else:
        player = Veneno(nome)
        return player



nome = input('Informe o nome do personagem: ')
tipo = input('Informe o tipo do personagem: ')
player1 = criarPersonagem(nome, tipo)

nome = input('Informe o nome do personagem: ')
tipo = input('Informe o tipo do personagem: ')
player2 = criarPersonagem(nome, tipo)

while True:
    print('---- Turno player 1 ----')
    opcao = int(input('Como deseja atacar? \n'
                      '1 - Soco \n'
                      '2 - Especial: '))

    if opcao == 1:
        player1.socar(player2)
        if not player2.vivo:
            print(f'Fim do jogo!! Vencedor: {player1.nome}')
            break

    if opcao == 2:
        player1.especial(player2)
        if not player2.vivo:
            print(f'Fim do jogo!! Vencedor {player1.nome}')
            break

    print('---- Turno player 2 ----')
    opcao = int(input('Como deseja atacar? \n'
                      '1 - Soco \n'
                      '2 - Especial: '))

    if opcao == 1:
        player2.socar(player1)
        if not player1.vivo:
            print(f'Fim do jogo!! Vencedor: {player2.nome}')
            break

    if opcao == 2:
        player2.especial(player1)
        if not player1.vivo:
            print(f'Fim do jogo!! Vencedor {player2.nome}')
            break