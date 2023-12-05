import time

class Produto:
    def __init__(self, descricao, preco, tamanhos_disponiveis, cores_disponiveis, estilo, imagem):
        self.descricao = descricao
        self.preco = preco
        self.tamanhos_disponiveis = tamanhos_disponiveis
        self.cores_disponiveis = cores_disponiveis
        self.estilo = estilo
        self.imagem = imagem
        self.avaliacoes = []

    def adicionar_avaliacao(self, aluno, nota, comentario):
        avaliacao = {'aluno': aluno, 'nota': nota, 'comentario': comentario}
        self.avaliacoes.append(avaliacao)
        print(f"Avaliação de {aluno} para {self.descricao} adicionada!")

    def exibir_avaliacoes(self):
        print(f"\nAvaliações para {self.descricao}:")
        if not self.avaliacoes:
            print("Ainda não há avaliações para este produto.")
        else:
            for avaliacao in self.avaliacoes:
                print(f"\n- Aluno: {avaliacao['aluno']}")
                print(f"  Nota: {avaliacao['nota']}")
                print(f"  Comentário: {avaliacao['comentario']}")

class PerfilCompraAluno:
    def __init__(self, aluno_nome):
        self.aluno_nome = aluno_nome
        self.historico_compras = []
        self.preferencias = {
            'estilo': None,
            'tamanhos': [],
            'cores_favoritas': []
        }
        self.lista_desejos = ListaDesejos()
        self.notificacoes = NotificacaoNovosProdutos()
        self.promocoes_personalizadas = PromocaoPersonalizada()
        self.pontos_fidelidade = 50  # Adicionando pontos de fidelidade inicial

    def adicionar_compra(self, produto, quantidade):
        compra = {'produto': produto, 'quantidade': quantidade}
        self.historico_compras.append(compra)
        self.atualizar_perfil()

    def atualizar_perfil(self):
        estilos = [compra['produto'].estilo for compra in self.historico_compras if compra['produto'].estilo]
        tamanhos = [tamanho for compra in self.historico_compras for tamanho in compra['produto'].tamanhos_disponiveis]
        cores = [cor for compra in self.historico_compras for cor in compra['produto'].cores_disponiveis]

        # Atualizar preferências
        if estilos:
            estilo_mais_frequente = max(set(estilos), key=estilos.count)
            self.preferencias['estilo'] = estilo_mais_frequente

        self.preferencias['tamanhos'] = list(set(tamanhos))
        self.preferencias['cores_favoritas'] = list(set(cores))

        # Atualizar lista de desejos
        self.lista_desejos.verificar_promocao(self.historico_compras)

        # Verificar notificações de novos produtos
        self.notificacoes.verificar_novos_produtos(self.preferencias['estilo'])

        # Atualizar promoções personalizadas
        self.promocoes_personalizadas.gerar_promocoes(self.preferencias)

        # Atualizar pontos de fidelidade
        pontos_novos = sum(compra['produto'].preco * compra['quantidade'] // 10 for compra in self.historico_compras)
        self.pontos_fidelidade += pontos_novos

    def exibir_perfil(self):
        print(f"\nPerfil de Compra de {self.aluno_nome}:")
        if not self.historico_compras:
            print("Ainda não há compras registradas para este perfil.")
        else:
            print("Histórico de Compras:")
            for compra in self.historico_compras:
                print(f"- {compra['quantidade']}x {compra['produto'].descricao}")

            print("\nPreferências:")
            print(f"Estilo: {self.preferencias['estilo']}")
            print(f"Tamanhos Favoritos: {', '.join(self.preferencias['tamanhos'])}")
            print(f"Cores Favoritas: {', '.join(self.preferencias['cores_favoritas'])}")

            print("\nPontos de Fidelidade: {}".format(self.pontos_fidelidade))

        # Exibir lista de desejos
        self.lista_desejos.exibir_lista()

        # Exibir promoções personalizadas
        self.promocoes_personalizadas.exibir_promocoes()

    def adicionar_lista_desejos(self, produto):
        self.lista_desejos.adicionar_produto(produto)
        print(f"Produto '{produto.descricao}' adicionado à lista de desejos!")

    def escolher_notificacao(self):
        opcao_notificacao = input("Escolha o método de notificação (1. E-mail, 2. Aplicativo): ")
        if opcao_notificacao == "1":
            self.notificacoes.set_notificacao_email()
        elif opcao_notificacao == "2":
            self.notificacoes.set_notificacao_aplicativo()
        else:
            print("Opção inválida. Usando notificação padrão.")

    def adicionar_avaliacao(self, produto, nota, comentario):
        produto.adicionar_avaliacao(self.aluno_nome, nota, comentario)

class CadastroProdutos:
    TAMANHOS_LOJA = ["P", "M", "G", "GG"]

    def __init__(self):
        self.produtos = []

    def cadastrar_produto_interativo(self):
        descricao = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))

        print("Tamanhos disponíveis na loja:", ", ".join(self.TAMANHOS_LOJA))
        while True:
            tamanhos_disponiveis = input("Digite os tamanhos disponíveis (separados por vírgula): ").split(",")
            tamanhos_validos = [tamanho.strip().upper() for tamanho in tamanhos_disponiveis]
            tamanhos_invalidos = [tamanho for tamanho in tamanhos_validos if tamanho not in self.TAMANHOS_LOJA]

            if not tamanhos_invalidos:
                break
            else:
                print("Atenção: Os seguintes tamanhos não são válidos para a loja:", ", ".join(tamanhos_invalidos))

        cores_disponiveis = input("Digite as cores disponíveis (separadas por vírgula): ").split(",")
        estilo = input("Digite o estilo do produto: ")
        imagem = input("Digite o nome do arquivo de imagem: ")

        produto = Produto(descricao, preco, tamanhos_validos, cores_disponiveis, estilo, imagem)
        self.produtos.append(produto)
        print(f"Produto '{produto.descricao}' cadastrado com sucesso!")

    def listar_produtos(self):
        print("\nProdutos Cadastrados:")
        for produto in self.produtos:
            print(f"- {produto.descricao} - Preço: {produto.preco} - Tamanhos Disponíveis: {', '.join(produto.tamanhos_disponiveis)}")

    def escolher_produto(self):
        if not self.produtos:
            print("Não há produtos cadastrados.")
            return None

        print("\nEscolha um produto para avaliação:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto.descricao}")

        while True:
            escolha = input("Digite o número do produto: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(self.produtos):
                return self.produtos[int(escolha) - 1]
            else:
                print("Escolha inválida. Tente novamente.")

    def exibir_menu(self):
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Acessar Perfil de Compra do Aluno")
        print("3. Ver Promoções Personalizadas")
        print("4. Gerenciar Lista de Desejos")
        print("5. Escolher Método de Notificação")
        print("6. Sistema De Pagamento")
        print("7. Acompanhar Entrega")
        print("8. Programa de Fidelidade")
        print("9. Avaliar Produto")
        print("0. Sair")

class ListaDesejos:
    def __init__(self):
        self.produtos_desejados = []

    def adicionar_produto(self, produto):
        self.produtos_desejados.append(produto)

    def verificar_promocao(self, historico_compras):
        for produto_desejado in self.produtos_desejados:
            for compra in historico_compras:
                if compra['produto'] == produto_desejado:
                    print(f"O produto '{produto_desejado.descricao}' da sua lista de desejos está em promoção!")

    def exibir_lista(self):
        print("\nLista de Desejos:")
        if not self.produtos_desejados:
            print("Ainda não há produtos na lista de desejos.")
        else:
            for produto in self.produtos_desejados:
                print(f"- {produto.descricao}")

class NotificacaoNovosProdutos:
    def __init__(self):
        self.metodo_notificacao = "Padrão"  # Pode ser "E-mail", "Aplicativo" ou "Padrão"

    def set_notificacao_email(self):
        self.metodo_notificacao = "E-mail"
        print("Notificações por e-mail ativadas.")

    def set_notificacao_aplicativo(self):
        self.metodo_notificacao = "Aplicativo"
        print("Notificações no aplicativo ativadas.")

    def verificar_novos_produtos(self, estilo_preferido):
        if self.metodo_notificacao != "Padrão" and estilo_preferido:
            print(f"Novos produtos do estilo '{estilo_preferido}' foram adicionados!")
            print(f"Você será notificado por {self.metodo_notificacao}.")

class PromocaoPersonalizada:
    def __init__(self):
        self.promocoes = []

    def gerar_promocoes(self, preferencias):
        estilo_preferido = preferencias['estilo']
        tamanhos_preferidos = preferencias['tamanhos']
        cores_preferidas = preferencias['cores_favoritas']

        # Exemplo: Promoção de 20% de desconto em produtos do estilo preferido
        if estilo_preferido:
            promocao_estilo = f"20% de desconto em produtos do estilo '{estilo_preferido}'"
            self.promocoes.append(promocao_estilo)

        # Exemplo: Promoção de frete grátis para tamanhos preferidos
        if tamanhos_preferidos:
            promocao_tamanhos = f"Frete grátis para tamanhos '{', '.join(tamanhos_preferidos)}'"
            self.promocoes.append(promocao_tamanhos)

        # Exemplo: Promoção de brinde para compras com cores favoritas
        if cores_preferidas:
            promocao_cores = f"Receba um brinde nas compras com cores '{', '.join(cores_preferidas)}'"
            self.promocoes.append(promocao_cores)

    def exibir_promocoes(self):
        print("\nPromoções Personalizadas:")
        for promocao in self.promocoes:
            print(f"- {promocao}")

class SistemaPagamento:
    @staticmethod
    def realizar_pagamento(perfil_aluno):
        valor_total = sum(compra['produto'].preco * compra['quantidade'] for compra in perfil_aluno.historico_compras)

        print(f"\nResumo da Compra:")
        for compra in perfil_aluno.historico_compras:
            print(f"- {compra['quantidade']}x {compra['produto'].descricao} - Preço Unitário: {compra['produto'].preco}")

        print(f"\nValor Total da Compra: {valor_total:.2f}")

        opcao_pagamento = input("Escolha o método de pagamento (1. Cartão de Crédito, 2. Boleto): ")
        if opcao_pagamento == "1":
            print("Pagamento com Cartão de Crédito realizado com sucesso!")
        elif opcao_pagamento == "2":
            print("Boleto gerado. Realize o pagamento até a data de vencimento.")
        else:
            print("Opção de pagamento inválida. Tente novamente.")

class AcompanhamentoEntrega:
    @staticmethod
    def iniciar_entrega(historico_compras):
        print("\nA entrega está em andamento. Acompanhe o status em tempo real:")

        for compra in historico_compras:
            print(f"\nStatus para '{compra['produto'].descricao}':")
            status_atual = "Pedido recebido. Preparando para envio."
            print(status_atual)
            time.sleep(1)  # Simula o tempo de preparação para envio

            status_atual = "Enviado para o centro de distribuição."
            print(status_atual)
            time.sleep(1)  # Simula o tempo de envio para o centro de distribuição

            status_atual = "Em trânsito para o endereço de entrega."
            print(status_atual)
            time.sleep(1)  # Simula o tempo de trânsito

            status_atual = "Entrega realizada com sucesso!"
            print(status_atual)


# Função principal
if __name__ == "__main__":
    # Criando produtos de exemplo
    produto1 = Produto("Camiseta Fitness", 29.99, ["P", "M", "G", "GG"], ["Preto", "Branco", "Azul"], "Casual", "imagem_camiseta.jpg")
    produto2 = Produto("Legging Estampada", 39.99, ["P", "M", "G"], ["Estampado", "Preto"], "Esportivo", "imagem_legging.jpg")

    # Criando um perfil de compra para o aluno Igor com algumas compras fictícias
    perfil_igor = PerfilCompraAluno("Igor")
    perfil_igor.adicionar_compra(produto1, 2)
    perfil_igor.adicionar_compra(produto2, 1)

    # Criando o cadastro de produtos, o módulo de promoções personalizadas, as promoções para Igor
    # e a lista de desejos e notificações para o perfil Igor
    cadastro_produtos = CadastroProdutos()
    promocoes_igor = PromocaoPersonalizada()

    

    while True:
        cadastro_produtos.exibir_menu()
        opcao = input("Escolha uma opção (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): ")

        if opcao == "0":
            break
        elif opcao == "1":
            cadastro_produtos.cadastrar_produto_interativo()
        elif opcao == "2":
            nome_perfil = input("Digite o nome do aluno: ")
            if nome_perfil.lower() == "igor":
                perfil_aluno = perfil_igor
            else:
                perfil_aluno = PerfilCompraAluno(nome_perfil)
            perfil_aluno.exibir_perfil()
        elif opcao == "3":
            nome_perfil = input("Digite o nome do aluno para ver as promoções: ")
            if nome_perfil.lower() == "igor":
                promocoes_igor.gerar_promocoes(perfil_igor.preferencias)
                promocoes_igor.exibir_promocoes()
            else:
                print("Ainda não há compras registradas para este perfil.")
        elif opcao == "4":
            nome_perfil = input("Digite o nome do aluno para gerenciar a lista de desejos: ")
            if nome_perfil.lower() == "igor":
                perfil_igor.lista_desejos.exibir_lista()
            else:
                print("Ainda não há produtos na lista de desejos para este perfil.")
        elif opcao == "5":
            nome_perfil = input("Digite o nome do aluno para escolher o método de notificação: ")
            if nome_perfil.lower() == "igor":
                perfil_igor.escolher_notificacao()
            else:
                print("Esse perfil não existe.")
        elif opcao == "6":
            nome_perfil = input("Digite o nome do aluno para realizar o pagamento: ")
            if nome_perfil.lower() == "igor":
                SistemaPagamento.realizar_pagamento(perfil_igor)
            else:
                print("Ainda não há compras registradas para este perfil.")
        elif opcao == "7":
            nome_perfil = input("Digite o nome do aluno para iniciar o acompanhamento da entrega: ")
            if nome_perfil.lower() == "igor":
                AcompanhamentoEntrega.iniciar_entrega(perfil_igor.historico_compras)
            else:
                print("Ainda não há compras registradas para este perfil.")
        elif opcao == "8":
            nome_perfil = input("Digite o nome do aluno para verificar os pontos de fidelidade: ")
            if nome_perfil.lower() == "igor":
                print(f"Pontos de Fidelidade para {perfil_igor.aluno_nome}: {perfil_igor.pontos_fidelidade}")
            else:
                print("Ainda não há compras registradas para este perfil.")
        elif opcao == "9":
            produto_avaliacao = cadastro_produtos.escolher_produto()
            nome_perfil = input("Digite o nome do aluno para deixar uma avaliação: ")
            if nome_perfil.lower() == "igor":
                if produto_avaliacao:
                    nota_avaliacao = int(input("Digite a nota (1 a 5): "))
                    comentario_avaliacao = input("Digite o comentário: ")
                    perfil_igor.adicionar_avaliacao(produto_avaliacao, nota_avaliacao, comentario_avaliacao)
            else:
                print("Ainda não há compras registradas para este perfil.")
        else:
            print("Opção inválida. Tente novamente.")
