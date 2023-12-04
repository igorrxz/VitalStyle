class Produto:
    def __init__(self, descricao, preco, tamanhos_disponiveis, imagem):
        self.descricao = descricao
        self.preco = preco
        self.tamanhos_disponiveis = tamanhos_disponiveis
        self.imagem = imagem

class CadastroProdutos:
    TAMANHOS_LOJA = ["P", "M", "G", "GG"]  # Tamanhos que a loja aceita

    def __init__(self):
        self.produtos = []

    def cadastrar_produto_interativo(self):
        descricao = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        
        # Mostrar os tamanhos que a loja aceita
        print("Tamanhos disponíveis na loja:", ", ".join(self.TAMANHOS_LOJA))
        
        while True:
            tamanhos_disponiveis = input("Digite os tamanhos disponíveis (separados por vírgula): ").split(",")
            
            # Verificar se os tamanhos informados são válidos
            tamanhos_validos = [tamanho.strip().upper() for tamanho in tamanhos_disponiveis]
            tamanhos_invalidos = [tamanho for tamanho in tamanhos_validos if tamanho not in self.TAMANHOS_LOJA]

            if not tamanhos_invalidos:
                break
            else:
                print("Atenção: Os seguintes tamanhos não são válidos para a loja:", ", ".join(tamanhos_invalidos))
        
        imagem = input("Digite o nome do arquivo de imagem: ")

        produto = Produto(descricao, preco, tamanhos_validos, imagem)
        self.produtos.append(produto)
        print(f"Produto '{produto.descricao}' cadastrado com sucesso!")

    def listar_produtos(self):
        print("\nProdutos Cadastrados:")
        for produto in self.produtos:
            print(f"- {produto.descricao} - Preço: {produto.preco} - Tamanhos Disponíveis: {', '.join(produto.tamanhos_disponiveis)}")

# Exemplo de uso:
if __name__ == "__main__":
    cadastro = CadastroProdutos()

    while True:
        cadastrar = input("Deseja cadastrar um novo produto? (S/N): ").upper()
        if cadastrar != 'S':
            break

        cadastro.cadastrar_produto_interativo()

    cadastro.listar_produtos()
