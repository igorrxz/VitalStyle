import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class PerfilTreino:
    def __init__(self, nome, idade, sexo, historico, metas, restricoes, preferencias, video_library=None, rotinas=None, desempenho=None, premiacoes=None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.historico = historico
        self.metas = metas
        self.restricoes = restricoes
        self.preferencias = preferencias
        self.video_library = video_library or []
        self.rotinas = rotinas or []
        self.desempenho = desempenho or {}
        self.premiacoes = premiacoes or []

    def atualizar_perfil(self, nome=None, idade=None, sexo=None, historico=None, metas=None, restricoes=None, preferencias=None):
        if nome is not None:
            self.nome = nome
        if idade is not None:
            self.idade = idade
        if sexo is not None:
            self.sexo = sexo
        if historico is not None:
            self.historico = historico
        if metas is not None:
            self.metas = metas
        if restricoes is not None:
            self.restricoes = restricoes
        if preferencias is not None:
            self.preferencias = preferencias

    def adicionar_video(self):
        titulo = input("Digite o título do vídeo: ")
        categoria = input("Digite a categoria do vídeo: ")
        link = input("Digite o link do vídeo: ")
        video = {'titulo': titulo, 'categoria': categoria, 'link': link}
        self.video_library.append(video)
        print("Vídeo adicionado à biblioteca!")

    def adicionar_rotina(self, descricao, exercicios):
        rotina = {'descricao': descricao, 'exercicios': exercicios}
        self.rotinas.append(rotina)

    def exibir_rotinas(self):
        print("\nRotinas de Treino:")
        for i, rotina in enumerate(self.rotinas, 1):
            print(f"{i}. Descrição: {rotina['descricao']}")
            print("   Exercícios:")
            for exercicio in rotina['exercicios']:
                print(f"      - {exercicio}")
            print()

    def adaptar_rotina(self, rotina_index, novo_descricao, novo_exercicios):
        if 0 <= rotina_index < len(self.rotinas):
            self.rotinas[rotina_index]['descricao'] = novo_descricao
            self.rotinas[rotina_index]['exercicios'] = novo_exercicios
            print("Rotina adaptada com sucesso.")
        else:
            print("Índice de rotina inválido.")

    def gerar_rotina(self):
        descricao = "Rotina Inicial"
        exercicios = ["Flexões", "Agachamentos", "Abdominais"]
        self.adicionar_rotina(descricao, exercicios)

    def registrar_desempenho(self):
        exercicio = input("Digite o nome do exercício: ")
        carga = int(input("Digite a carga utilizada: "))
        frequencia_cardiaca = int(input("Digite a frequência cardíaca: "))
        outras_metricas = input("Digite outras métricas (opcional): ")

        if exercicio not in self.desempenho:
            self.desempenho[exercicio] = []

        registro = {'carga': carga, 'frequencia_cardiaca': frequencia_cardiaca, 'outras_metricas': outras_metricas}
        self.desempenho[exercicio].append(registro)
        print("Desempenho registrado!")

    def exibir_desempenho(self, exercicio):
        if exercicio in self.desempenho:
            for registro in self.desempenho[exercicio]:
                print(f"Carga: {registro['carga']}")
                print(f"Frequência Cardíaca: {registro['frequencia_cardiaca']}")
                print(f"Outras Métricas: {registro['outras_metricas']}")
                print()
        else:
            print(f"Não há registros de desempenho para o exercício: {exercicio}")

    def plotar_desempenho(self, exercicio):
        if exercicio in self.desempenho:
            cargas = [registro['carga'] for registro in self.desempenho[exercicio]]
            plt.plot(range(1, len(cargas) + 1), cargas, marker='o')
            plt.title(f"Desempenho em {exercicio}")
            plt.xlabel("Número de Sessões")
            plt.ylabel("Carga")
            plt.show()
        else:
            print(f"Não há registros de desempenho para o exercício: {exercicio}")

    def enviar_alerta_treino(self):
        email = input("Digite seu endereço de email para receber um alerta de treino: ")

        subject = "Lembrete de Treino"
        body = f"Olá {self.nome},\n\nEste é um lembrete para o seu treino programado. Não se esqueça de se exercitar hoje!\n\nAtenciosamente,\nSistema de Treino"


        smtp_server = "seu_servidor_smtp"
        smtp_port = 587
        smtp_username = "seu_email"
        smtp_password = "sua_senha"



        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = email

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, email, msg.as_string())
                print(f"Alerta de Treino enviado para {email}.")
        except Exception as e:
            print(f"Erro ao enviar alerta de treino: {e}")

    def fornecer_feedback(self):
        feedback = input("Digite seu feedback sobre os exercícios: ")
        print("Feedback enviado com sucesso!")


    def adicionar_premiacao(self, premiacao):
        self.premiacoes.append(premiacao)
        print("Premiação adicionada!")

    def listar_premiacoes(self):
        print("\nPremiações:")
        for premiacao in self.premiacoes:
            print(f"- {premiacao}")

    def comunicar_com_professor(self):
        mensagem = input("Digite sua mensagem para o professor: ")


        professor_email = "eduardoaguiar@gmail.com"

        subject = "Comunicação com Aluno"
        body = f"Aluno: {self.nome}\n\nMensagem:\n{mensagem}"


        smtp_server = "seu_servidor_smtp"
        smtp_port = 587
        smtp_username = "seu_email"
        smtp_password = "sua_senha"



        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = professor_email

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, professor_email, msg.as_string())
                print(f"Mensagem enviada para o professor.")
        except Exception as e:
            print(f"Erro ao enviar mensagem para o professor: {e}")


nome = input("Digite seu nome: ")
idade = None
while idade is None:
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Por favor, digite uma idade válida.")

sexo = input("Digite seu sexo: ")
historico = input("Digite seu histórico de treino: ")
metas = input("Digite suas metas de condicionamento físico: ")
restricoes = input("Digite suas restrições (se houver): ")
preferencias = input("Digite suas preferências de treino: ")


perfil1 = PerfilTreino(nome, idade, sexo, historico, metas, restricoes, preferencias)


perfil1.adicionar_video()


perfil1.gerar_rotina()


perfil1.registrar_desempenho()


exercicio = input("Digite o nome do exercício para exibir o desempenho: ")
perfil1.exibir_desempenho(exercicio)

if exercicio in perfil1.desempenho:
    perfil1.plotar_desempenho(exercicio)
else:
    print(f"Não há registros de desempenho para o exercício: {exercicio}")

perfil1.enviar_alerta_treino()

perfil1.fornecer_feedback()

perfil1.comunicar_com_professor()