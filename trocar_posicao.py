class trocar_posicao:
    def __init__(self):
        # Inicializações ou configurações podem ser feitas aqui
        self.conteudo = []
        self.palavras_chaves = ["posicao_x1", "posicao_x2", "posicao_y1", "posicao_y2", "posicao_z1", "posicao_z2", "nome_arquivo", "'nome_arquivo.'"]
        self.correspondencias = ["4", "4", "0", "0.1","0","0.1", "duto3m"+"OpenFOAM", "duto3m"+".OpenFOAM"] 

    def load_file(self):
        with open("modelo_alterar_posicao_plot.py", 'r') as arquivo:
            self.conteudo = arquivo.readlines()
    
    def write_file(self):
        with open("novo_nome.py", 'w+') as arquivo_out:
            for frase in self.conteudo:
                palavras = frase.split(" ")
                for palavra in palavras:
                    if palavra in self.palavras_chaves:
                        arquivo_out.write(
                            self.correspondencias[self.palavras_chaves.index(palavra)]
                            )
                        print(self.correspondencias[self.palavras_chaves.index(palavra)])
                    else:
                        posicao = palavras.index(palavra)
                        if posicao == 0:
                            arquivo_out.write(palavra)
                        else:
                            arquivo_out.write(" "+palavra)

def main():
    # Cria uma instância da classe
    meu_programa = trocar_posicao()

    # Chama a função da classe
    meu_programa.load_file()
    meu_programa.write_file()

if __name__ == "__main__":
    main()
