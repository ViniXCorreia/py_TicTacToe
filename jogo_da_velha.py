class JogoDaVelha(object):
    
    def __init__(self):
        self.jogadas = list(range(0, 9))
        self.tab = [" "] * 9
        self.vez = 'X'
        self.vitorias = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def troca_vez(self):
        self.vez = {
            'X': 'O',
            'O': 'X'
        }[self.vez]

    def imprime_tabuleiro(self):
        print(f" {self.tab[0]} | {self.tab[1]} | {self.tab[2]} " )
        print("-----------")
        print(f" {self.tab[3]} | {self.tab[4]} | {self.tab[5]} " )
        print("-----------")
        print(f" {self.tab[6]} | {self.tab[7]} | {self.tab[8]} " )

    def is_int(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def jogada_valida(self):
        print(f"Jogadas  disponíveis: {self.jogadas}")
        jogada = input(f"Jogada de {self.vez}: ")
        
        if (self.is_int(jogada) and int(jogada) in self.jogadas):
            jogada = int(jogada)
            self.jogadas.remove(jogada)
            self.tab[jogada] = self.vez
            return True
        else:
            print("Jogada inválida, seu animal!")
            return False

    def fim_de_jogo(self):
        for v in self.vitorias:
            if (''.join([self.tab[v[0]], self.tab[v[1]], self.tab[v[2]]]) in ['XXX', 'OOO']):
                return True

        return False            

    def run(self):
        while not self.fim_de_jogo():
            print("")
            self.imprime_tabuleiro()
            self.troca_vez()
            
            while not self.jogada_valida():
                pass
              
        else:
            self.imprime_tabuleiro()
            print(f"Fim de jogo, {self.vez} ganhou!")
            
            
jogo = JogoDaVelha()
jogo.run()