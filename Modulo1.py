import random

alunos = []
professores = []
mensagens = []

def exibir_menu_boas_vindas():
    print("=" * 68)
    print("VitalFit: Transformando vidas a partir de um estilo de vida saudável")
    print("=" * 68)

    print()
    print("1. Aluno(a)")
    print("2. Professor(a)")
    print("3. Sair")

def exibir_menu_aluno():
    print()
    print("=" * 13)
    print("Menu do Aluno")
    print("=" * 13)
    print()
    print("1. Cadastrar Aluno")
    print("2. Registrar Progresso")
    print("3. Visualizar Cadastro")
    print("4. Agendar Treino com Professor")
    print("5. Mensagens")
    print("6. Voltar ao Menu Principal")

def cadastrar_aluno():
    print()
    print("=" * 17)
    print("Cadastro de Aluno")
    print("=" * 17)
    print()
    nome = input("Nome: ")
    idade = input("Idade: ")
    peso = input("Peso (em kg): ")
    altura = input("Altura (em m): ")
    condicao_medica = input("Condição Médica: ")

    print("\nMetas de Condicionamento Físico\n")
    print("1. Perda de Peso")
    print("2. Ganho de Massa Muscular")
    print("3. Melhoria na Resistência")
    print("4. Melhoria na Saúde")

    metas_selecionadas = input("\n-> Selecione as metas desejadas (separadas por vírgula): ")

    aluno = {
        'Nome': nome,
        'Idade': idade,
        'Peso': peso,
        'Altura': altura,
        'Condição Médica': condicao_medica,
        'Metas': metas_selecionadas.split(','),
        'Progressos': [],
        'Mensagens': []
    }

    alunos.append(aluno)

    print("\nAluno(a) cadastrado com sucesso!")

def exibir_informacoes_aluno(nome_aluno):
    for aluno in alunos:
        if aluno['Nome'].lower() == nome_aluno.lower():
            print("\nInformações do Aluno", aluno['Nome'])
            print("Nome:", aluno['Nome'])
            print("Idade:", aluno['Idade'])
            print("Peso:", aluno['Peso'])
            print("Altura:", aluno['Altura'])
            print("Condição Médica:", aluno['Condição Médica'])
            print("Metas:", ', '.join(aluno['Metas']))
            return True

    print("\nAluno", nome_aluno, "não encontrado.")
    return False

def registrar_progresso(nome_aluno):
    for aluno in alunos:
        if aluno['Nome'].lower() == nome_aluno.lower():
            print("\nRegistro de Progresso para", aluno['Nome'])

            if not aluno['Metas']:
                print("O aluno não selecionou metas. Por favor, selecione metas antes de registrar o progresso.")
                return True

            progresso = {
                'Nome': aluno['Nome'],
                'Metas': [],
                'Progresso': {}
            }

            print("\nMetas Selecionadas\n")
            for i, meta in enumerate(aluno['Metas'], start=1):
                nome_meta = ""
                if meta == "1":
                    nome_meta = "Perda de Peso"
                elif meta == "2":
                    nome_meta = "Ganho de Massa Muscular"
                elif meta == "3":
                    nome_meta = "Melhoria na Resistência"
                elif meta == "4":
                    nome_meta = "Melhoria na Saúde"
                print(f"{i}. {nome_meta}")

                progresso['Metas'].append(nome_meta)

            for meta in progresso['Metas']:
                valor_progresso = input(f"\n-> Informe o progresso para a meta '{meta}': ")
                progresso['Progresso'][meta] = valor_progresso

            aluno['Progressos'].append(progresso)
            print("\nProgresso registrado com sucesso!")
            return True

    print("\nAluno", nome_aluno, "não encontrado!")
    return False

def exibir_informacoes_alunos():
    if not alunos:
        print("\nNenhum aluno registrado!")
    else:
        print()
        print("=" * 24)
        print("Vizualização de Cadastro")
        print("=" * 24)

        nome_aluno = input("\n-> Digite o nome do aluno para visualizar seu cadastro (ou deixe em branco para voltar): ").strip()

        if nome_aluno:
            aluno_encontrado = exibir_informacoes_aluno(nome_aluno)
            while not aluno_encontrado:
                nome_aluno = input("\n-> Digite o nome do aluno para visualizar seu cadastro (ou deixe em branco para voltar): ").strip()
                if not nome_aluno:
                    break
                aluno_encontrado = exibir_informacoes_aluno(nome_aluno)

def agendar_treino_com_professor(nome_aluno):
    if not professores:
        print("\nNão há professores registrados. Cadastre um professor antes de agendar um treino.")
        return False

    print()
    print("=" * 22)
    print("Agendamento de Treinos")
    print("=" * 22)

    print("\nProfessores Disponíveis:\n")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. {professor['Nome']} - {professor['Especialidade']}")

    opcao_professor = input("\n-> Selecione o número do professor desejado: ")
    try:
        opcao_professor = int(opcao_professor)
        if 1 <= opcao_professor <= len(professores):
            professor_selecionado = professores[opcao_professor - 1]

            if professor_selecionado.get('Agenda'):
                print("\nDatas Disponíveis para Treino:\n")
                for i, data in enumerate(professor_selecionado['Agenda'], start=1):
                    print(f"{i}. {data}")

                opcao_data = input("\n-> Selecione o número da data desejada: ")
                try:
                    opcao_data = int(opcao_data)
                    if 1 <= opcao_data <= len(professor_selecionado['Agenda']):
                        data_selecionada = professor_selecionado['Agenda'].pop(opcao_data - 1)

                        aluno_agendamento = {
                            'Nome': nome_aluno,
                            'Data': data_selecionada,
                            'Professor': professor_selecionado['Nome']
                        }

                        professor_selecionado.setdefault('TreinosAgendados', []).append(aluno_agendamento)
                        print(f"\nTreino agendado com sucesso para o professor {professor_selecionado['Nome']} "
                              f"na data {data_selecionada}.\n")
                        return True
                    else:
                        print("\nOpção de data inválida. Tente novamente.")
                        return agendar_treino_com_professor(nome_aluno)

                except ValueError:
                    print("\nOpção de data inválida. Tente novamente.")
                    return agendar_treino_com_professor(nome_aluno)
            else:
                print("\nNão há datas disponíveis na agenda deste professor.")
                return False

        else:
            print("\nOpção de professor inválida. Tente novamente.")
            return agendar_treino_com_professor(nome_aluno)

    except ValueError:
        print("\nOpção de professor inválida. Tente novamente.")
        return agendar_treino_com_professor(nome_aluno)

def exibir_progresso_aluno(nome_aluno):
    for aluno in alunos:
        if aluno['Nome'].lower() == nome_aluno.lower():
            if 'Progressos' in aluno and aluno['Progressos']:
                print()
                print("=" * 38)
                print("Progresso do Aluno", aluno['Nome'])
                print("=" * 38)
                for progresso in aluno['Progressos']:
                    for meta, valor in progresso['Progresso'].items():
                        print(f"{meta}: {valor}")
            else:
                print("\nNenhum progresso registrado para o aluno", aluno['Nome'])
            return True

    print("\nAluno", nome_aluno, "não encontrado.")
    return False

def exibir_menu_professor():
    print()
    print("=" * 17)
    print("Menu do Professor")
    print("=" * 17)
    print()
    print("1. Cadastrar Professor")
    print("2. Visualizar Progresso dos Alunos")
    print("3. Avaliação de Aluno")
    print("4. Mensagens")
    print("5. Voltar ao Menu Principal")

def cadastrar_professor():
    print()
    print("=" * 21)
    print("Cadastro de Professor")
    print("=" * 21)
    print()
    nome = input("Nome: ")
    idade = input("Idade: ")
    especialidade = input("Especialidade: ")
    experiencia = input("Experiência (em anos): ")

    datas_disponiveis = input("\nInforme as datas disponíveis para treinos (separadas por vírgula): ")
    agenda_professor = datas_disponiveis.split(',')

    professor = {
        'Nome': nome,
        'Idade': idade,
        'Especialidade': especialidade,
        'Experiência': experiencia,
        'Agenda': agenda_professor,
        'Mensagens': []
    }

    professores.append(professor)

    print("\nProfessor cadastrado com sucesso!")

def realizar_avaliacao_aluno(nome_aluno):
    for aluno in alunos:
        if aluno['Nome'].lower() == nome_aluno.lower():
            if 'Progressos' in aluno and aluno['Progressos']:
                print("\nAvaliação do Aluno", aluno['Nome'])
                for progresso in aluno['Progressos']:
                    print("\nData do Progresso:", progresso.get('Data', 'N/A'))
                    for meta, valor in progresso['Progresso'].items():
                        print(f"{meta}: {valor}")
                return True
            else:
                print("\nNenhum progresso registrado para o aluno", aluno['Nome'])
                return False

    print("\nAluno", nome_aluno, "não encontrado.")
    return False

def menu_avaliacao_professor():
    print()
    print("=" * 19)
    print("Avaliação de Aluno")
    print("=" * 19)
    nome_aluno = input("\n-> Digite o nome do aluno para avaliação (ou deixe em branco para voltar): ").strip()

    if nome_aluno:
        return realizar_avaliacao_aluno(nome_aluno)
    else:
        return False

def enviar_mensagem_usuario(remetente, tipo_destinatario, destinatario):
    mensagem = input("\nEscreva a sua mensagem: ")
    nova_mensagem = {
        'Remetente': remetente['Nome'],
        'TipoDestinatario': tipo_destinatario,
        'Destinatario': destinatario['Nome'],
        'Mensagem': mensagem
    }
    destinatario['Mensagens'].append(nova_mensagem)
    mensagens.append(nova_mensagem)
    print("\nMensagem enviada com sucesso!")

def exibir_caixa_entrada(usuario):
    print()
    print("=" * 17)
    print("Caixa de Entrada")
    print("=" * 17)

    if usuario['Mensagens']:
        for i, mensagem in enumerate(usuario['Mensagens'], start=1):
            print(f"{i}. De: {mensagem['Remetente']}")
            print(f"   Mensagem: {mensagem['Mensagem']}")
    else:
        print("\nCaixa de entrada vazia.")

def lógica_aluno():
    while True:
        exibir_menu_aluno()
        opcao_aluno = input("\n-> Digite o número da opção desejada: ")

        if opcao_aluno == "1":
            cadastrar_aluno()
        elif opcao_aluno == "2":
            print()
            print("=" * 21)
            print("Registro de Progresso")
            print("=" * 21)
            nome_aluno = input("\n-> Digite o nome do aluno para registrar progresso: ").strip()
            registrar_progresso(nome_aluno)
        elif opcao_aluno == "3":
            exibir_informacoes_alunos()
        elif opcao_aluno == "4":
            print()
            print("=" * 21)
            print("Agendamento de Treino")
            print("=" * 21)
            nome_aluno = input("\n-> Digite o nome do aluno para agendar treino: ").strip()
            agendar_treino_com_professor(nome_aluno)
        elif opcao_aluno == "5":
            print()
            print("=" * 9)
            print("Mensagens")
            print("=" * 9)
            nome_aluno = input("\n-> Digite o seu nome para acessar as mensagens: ").strip()
            aluno_logado = None

            for aluno in alunos:
                if aluno['Nome'].lower() == nome_aluno.lower():
                    aluno_logado = aluno
                    break

            if aluno_logado:
                while True:
                    print()
                    print("=" * 17)
                    print("Menu de Mensagens")
                    print("=" * 17)
                    print()
                    print("1. Escrever Mensagem")
                    print("2. Caixa de Entrada")
                    print("3. Voltar ao Menu Aluno")
                    opcao_mensagens = input("\n-> Digite o número da opção desejada: ")

                    if opcao_mensagens == "1":
                        destinatario = input("\nDigite o nome do destinatário: ").strip()
                        tipo_destinatario = None
                        destinatario_encontrado = None

                        for aluno in alunos:
                            if aluno['Nome'].lower() == destinatario.lower():
                                tipo_destinatario = 'aluno'
                                destinatario_encontrado = aluno
                                break

                        if not destinatario_encontrado:
                            for professor in professores:
                                if professor['Nome'].lower() == destinatario.lower():
                                    tipo_destinatario = 'professor'
                                    destinatario_encontrado = professor
                                    break

                        if destinatario_encontrado:
                            enviar_mensagem_usuario(aluno_logado, tipo_destinatario, destinatario_encontrado)
                        else:
                            print("\nDestinatário não encontrado. Mensagem não enviada.")

                    elif opcao_mensagens == "2":
                        exibir_caixa_entrada(aluno_logado)

                    elif opcao_mensagens == "3":
                        break

                    else:
                        print("\nOpção inválida. Por favor, escolha uma opção válida.")

        elif opcao_aluno == "6":
            print()
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

def realizar_avaliacao_aluno(nome_aluno):
    for aluno in alunos:
        if aluno['Nome'].lower() == nome_aluno.lower():
            if 'Progressos' in aluno and aluno['Progressos']:
                print("\nAvaliação do Aluno", aluno['Nome'])
                for progresso in aluno['Progressos']:
                    print("\nData do Progresso:", progresso.get('Data', 'N/A'))
                    for meta, valor in progresso['Progresso'].items():
                        print(f"{meta}: {valor}")
                return True
            else:
                print("\nNenhum progresso registrado para o aluno", aluno['Nome'])
                return False

    print("\nAluno", nome_aluno, "não encontrado.")
    return False

def menu_avaliacao_professor():
    print()
    print("=" * 19)
    print("Avaliação de Aluno")
    print("=" * 19)
    nome_aluno = input("\n-> Digite o nome do aluno para avaliação (ou deixe em branco para voltar): ").strip()

    if nome_aluno:
        return realizar_avaliacao_aluno(nome_aluno)
    else:
        return False

def lógica_professor():
    while True:
        exibir_menu_professor()
        opcao_professor = input("\n-> Digite o número da opção desejada: ")

        if opcao_professor == "1":
            cadastrar_professor()
        elif opcao_professor == "2":
            visualizar_progresso_alunos_professor()
        elif opcao_professor == "3":
            menu_avaliacao_professor()
        elif opcao_professor == "4":
            print()
            print("=" * 9)
            print("Mensagens")
            print("=" * 9)
            nome_professor = input("\n-> Digite o seu nome para acessar as mensagens: ").strip()
            professor_logado = None

            for professor in professores:
                if professor['Nome'].lower() == nome_professor.lower():
                    professor_logado = professor
                    break

            if professor_logado:
                while True:
                    print()
                    print("=" * 17)
                    print("Menu de Mensagens")
                    print("=" * 17)
                    print()
                    print("1. Escrever Mensagem")
                    print("2. Caixa de Entrada")
                    print("3. Voltar ao Menu Professor")
                    opcao_mensagens = input("\n-> Digite o número da opção desejada: ")

                    if opcao_mensagens == "1":
                        destinatario = input("\nDigite o nome do destinatário: ").strip()
                        tipo_destinatario = None
                        destinatario_encontrado = None

                        for aluno in alunos:
                            if aluno['Nome'].lower() == destinatario.lower():
                                tipo_destinatario = 'aluno'
                                destinatario_encontrado = aluno
                                break

                        if not destinatario_encontrado:
                            for professor in professores:
                                if professor['Nome'].lower() == destinatario.lower():
                                    tipo_destinatario = 'professor'
                                    destinatario_encontrado = professor
                                    break

                        if destinatario_encontrado:
                            enviar_mensagem_usuario(professor_logado, tipo_destinatario, destinatario_encontrado)
                        else:
                            print("\nDestinatário não encontrado. Mensagem não enviada.")

                    elif opcao_mensagens == "2":
                        exibir_caixa_entrada(professor_logado)

                    elif opcao_mensagens == "3":
                        break

                    else:
                        print("\nOpção inválida. Por favor, escolha uma opção válida.")

        elif opcao_professor == "5":
            print()
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

def visualizar_progresso_alunos_professor():
    if not professores:
        print("\nNão há professores registrados. Cadastre um professor antes de visualizar o progresso dos alunos.")
        return

    print()
    print("=" * 32)
    print("Visualização de Progresso Alunos")
    print("=" * 32)

    print("\nProfessores Disponíveis:\n")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. {professor['Nome']} - {professor['Especialidade']}")

    opcao_professor = input("\n-> Selecione o número do professor desejado: ")
    try:
        opcao_professor = int(opcao_professor)
        if 1 <= opcao_professor <= len(professores):
            professor_selecionado = professores[opcao_professor - 1]

            if professor_selecionado.get('TreinosAgendados'):
                print("\nAlunos com Treinos Agendados:")
                for treino_agendado in professor_selecionado['TreinosAgendados']:
                    nome_aluno = treino_agendado['Nome']
                    progresso_disponivel = exibir_progresso_aluno(nome_aluno)

                    if not progresso_disponivel:
                        print(f"\nNenhum progresso registrado para o aluno {nome_aluno}.")

            else:
                print("\nNão há alunos com treinos agendados para este professor.")
        else:
            print("\nOpção de professor inválida. Tente novamente.")

    except ValueError:
        print("\nOpção de professor inválida. Tente novamente.")

def main():
    while True:
        exibir_menu_boas_vindas()
        opcao_usuario = input("\n-> Digite o número da opção desejada: ")

        if opcao_usuario == "1":
            lógica_aluno()

        elif opcao_usuario == "2":
            lógica_professor()

        elif opcao_usuario == "3":
            print("\nAté mais! Obrigado por usar o VitalFit.")
            break

        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.\n")

if __name__ == "__main__":
    main()
