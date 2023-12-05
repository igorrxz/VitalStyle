class SistemaNutricional:
    pass

class Menu:
    def __init__(self, sistema_nutricional):
        self.sistema = sistema_nutricional
        self.nome = ""
        self.idade = 0
        self.peso = 0.0
        self.altura = 0.0
        self.habitos_alimentares = ""
        self.restricoes_alimentares = ""
        self.objetivos_peso = 0.0
        self.preferencias_alimentares = ""
        self.dieta_diaria = []
        self.orientacoes_nutricionais_lista = []
        self.consumo_agua_suplementos = {'agua': 0, 'suplementos': []}
        self.alimentos_saudaveis = {}

    def exibir_menu(self):
        print("\n------ Bem vindos à VitalFit ------")
        print("1. Questionário Inicial")
        print("2. Perfil Nutricional Individual")
        print("3. Registro de Dieta Diário")
        print("4. Orientações Nutricionais Personalizadas")
        print("5. Acompanhamento do Consumo de Água e Suplementos")
        print("6. Alertas de Metas Nutricionais")
        print("7. Registro de alimentos saudavéis")
        print("8. Feedback e Comunicação com Nutricionista")
        print("9. Sair")

    def executar_opcao(self, opcao):
        if opcao == 1:
            self.questionario_inicial()

        elif opcao == 2:
            self.perfil_nutricional()

        elif opcao == 3:
            self.registro_dieta_diario()

        elif opcao == 4:
            self.perguntar_objetivo_paciente()
            self.exibir_opcoes_alimentares()
            self.escolher_opcao_alimentar()

        elif opcao == 5:
            self.acompanha_consumo_agua_suplementos()

        elif opcao == 6:
            self.alertas_metas_nutricionais()

        elif opcao == 7:
            self.registro_alimentos_saudaveis()

        elif opcao == 8:
            self.feedback_comunicacao_nutricionista()

        elif opcao == 9:
            print("Obrigado. Até logo!")
            return True

        else:
            print("Opção inválida. Tente novamente.")
        return False

    def questionario_inicial(self):
        self.nome = input("Digite seu nome: ")
        self.idade = int(input("Digite sua idade: "))
        self.peso = float(input("Digite seu peso (em kg): "))
        self.altura = float(input("Digite sua altura (em cm): "))

    def perfil_nutricional(self):
        self.habitos_alimentares = input("Digite os hábitos alimentares do paciente: ")
        self.restricoes_alimentares = input("Digite as restrições alimentares do paciente: ")
        self.objetivos_peso = float(input("Digite o peso que o paciente deseja atingir (em kg): "))
        self.exibir_opcoes_alimentares()
        self.escolher_opcao_alimentar()

    def registro_dieta_diario(self):
        refeicao = input("Digite a dieta alimentar diária do paciente: ")
        self.dieta_diaria.append(refeicao)

    def perguntar_objetivo_paciente(self):
        self.objetivos_peso = input("Digite o objetivo do paciente: ")

    def orientacoes_nutricionais(self):
        orientacoes = []

        if 'vegetariano' in self.preferencias_alimentares:
            print("Considerar fontes alternativas de proteína, como leguminosas e produtos à base de soja.")
        else:
            print("Considerar fontes de proteína comuns, como frango na airfryer, carne vermelha.")

        if self.dieta_diaria:
            total_calorias = sum(refeicao.get('calorias', 0) for refeicao in self.dieta_diaria)

            if 'ganhar_massa_muscular' in self.objetivos_peso and total_calorias > self.calorias_gastas:
                orientacoes.append("Aumentar a ingestão calórica para promover o ganho de massa muscular.")
            elif 'perder_gordura' in self.objetivos_peso and total_calorias < self.calorias_gastas:
                orientacoes.append("Reduzir a ingestão calórica para promover a perda de gordura.")
            else:
                orientacoes.append("Manter um equilíbrio calórico para atingir os objetivos desejados.")

        self.orientacoes_nutricionais_lista.extend(orientacoes)

    def exibir_opcoes_alimentares(self):
        print("\nEscolha uma opção alimentar:")
        print("1. Vegano")
        print("2. Vegetariano")
        print("3. Intolerante à lactose")
        print("4. Intolerante a glúten")

    def escolher_opcao_alimentar(self):
        opcao_alimentar = int(input("Escolha a opção alimentar desejada: "))

        if opcao_alimentar == 1:
            self.orientacoes_nutricionais_vegano()

        elif opcao_alimentar == 2:
            self.orientacoes_nutricionais_vegetariano()

        elif opcao_alimentar == 3:
            self.orientacoes_nutricionais_lactose()

        elif opcao_alimentar == 4:
            self.orientacoes_nutricionais_gluten()

        else:
            print("Opção inválida. Tente novamente.")

    def orientacoes_nutricionais_vegano(self):
        self.orientacoes_nutricionais_vegano = input("Orientações para dieta vegana = ")
        self.orientacoes_nutricionais_lista.append("Considerar fontes alternativas de proteína, como leguminosas e produtos à base de soja.")

    def orientacoes_nutricionais_vegetariano(self):
        self.orientacoes_nutricionais_vegetariano = input("Orientações para dieta vegetariana = ")
        self.orientacoes_nutricionais_lista.append("Considerar fontes de proteína de derivação animal.")

    def orientacoes_nutricionais_lactose(self):
        self.orientacoes_nutricionais_lactose = input("Orientações para dieta 0 lactose = ")
        self.orientacoes_nutricionais_lista.append("Considerar alimentos sem lactose.")

    def orientacoes_nutricionais_gluten(self):
        self.orientacoes_nutricionais_gluten = input("Orientações para dieta sem glúten = ")
        self.orientacoes_nutricionais_lista.append("Considerar alimentos sem glúten.")

    def acompanha_consumo_agua_suplementos(self):
        agua = float(input("Digite a quantidade de água consumida (em Litros): "))
        suplementos = input("Digite os suplementos consumidos (separados por vírgula): ").split(',')
        suplementos = input("Digite a quantidade dos suplementos consumidos (em Gramas e separados por vírgula): ").split(',')
        self.consumo_agua_suplementos['agua'] += agua
        self.consumo_agua_suplementos['suplementos'].extend(suplementos)

    def alertas_metas_nutricionais(self):
        peso = float(input("Digite o peso do paciente (em KG): "))
        mililitros_desejados = peso * 35
        print(f"Recomendação: {mililitros_desejados:.2f} mililitros por dia.")

        consumo_agua = float(input("Digite quantos mililitros de água o paciente toma por dia: "))

        if consumo_agua < mililitros_desejados:
            print("Alerta: O paciente está ingerindo menos água do que o recomendado.")

        elif consumo_agua > mililitros_desejados:
            print("Alerta: O paciente está ingerindo mais água do que o recomendado.")

        else:
            print("O consumo de água está dentro da faixa recomendada.")

        whey = float(input("Digite a quantidade de Whey que o paciente ingere diariamente (em gramas): "))
        creatina = float(input("Digite a quantidade de Creatina que o paciente ingere diariamente (em gramas): "))

        if whey != 30 or creatina != 5:
            print("Alerta: A quantidade recomendada de Whey é 30g e de Creatina é 5g por dia. Verifique o consumo.")

    def registro_alimentos_saudaveis(self):
        def adicionar_alimento_saudavel(nome, categoria, calorias):
            self.alimentos_saudaveis[nome] = {'Categoria': categoria, 'Calorias': calorias}

        def exibir_tabela():
            print("\nTabela de Alimentos Saudáveis:")
            print("{:<20} {:<20} {:<20}".format("Nome", "Categoria", "Calorias"))
            print("-" * 60)
            for alimento, info in self.alimentos_saudaveis.items():
                print("{:<20} {:<20} {:<20}".format(alimento, info['Categoria'], info['Calorias']))

        while True:
            print("\nEscolha uma opção:")
            print("1. Adicionar Alimento Saudável")
            print("2. Exibir Tabela de Alimentos Saudáveis")
            print("3. Sair")

            opcao = int(input("Digite o número da opção desejada: "))

            if opcao == 1:
                nome = input("Digite o nome do alimento: ")
                categoria = input("Digite a categoria do alimento: ")
                calorias = float(input("Digite a quantidade de calorias: "))
                adicionar_alimento_saudavel(nome, categoria, calorias)

            elif opcao == 2:
                exibir_tabela()

            elif opcao == 3:
                print("Obrigado. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")
       
    def feedback_comunicacao_nutricionista(self):
        input("O que você achou do atendimento? ")
        print("Obrigado pelo feedback. Nos vemos em Breve! ")
        pass


sistema_nutricional = SistemaNutricional()
menu = Menu(sistema_nutricional)

while True:
    menu.exibir_menu()
    opcao = int(input("Escolha uma opção: "))
    if menu.executar_opcao(opcao):
        break