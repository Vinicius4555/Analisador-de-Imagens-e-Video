🔍 Scanner com YOLO & Streamlit
Este repositório contém uma aplicação Proof of Concept (PoC) de visão computacional, desenvolvida para demonstrar a integração entre o framework de detecção de objetos YOLOv8 e a biblioteca de interface de usuário Streamlit. O foco principal é a leveza para deploy em serviços de nuvem como o Render.

🚀 Funcionalidades
Detecção em Tempo Real: Captura e processamento de imagens via webcam diretamente no navegador.

Modelo Otimizado: Utiliza o yolov8n (nano), garantindo baixa latência e baixo consumo de memória RAM.

Interface Reativa: UI minimalista e funcional construída integralmente em Python.

Ready-to-Deploy: Configurações otimizadas para implantação imediata em ambientes Linux/Docker.

🛠️ Tecnologias Utilizadas
Python 3.9+

Streamlit - Interface Web.

Ultralytics YOLOv8 - Processamento de Visão Computacional.

OpenCV/Pillow - Manipulação de imagens.

📋 Pré-requisitos
Antes de começar, você precisará ter o Python instalado em sua máquina. Recomenda-se o uso de um ambiente virtual:

Bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Linux/macOS)
source venv/bin/activate

# Ativar ambiente virtual (Windows)
venv\Scripts\activate
🔧 Instalação e Execução Local
Clone o repositório:

git clone https://github.com/seu-usuario/scanner-yolo-streamlit.git
cd scanner-yolo-streamlit


2.  **Instale as dependências:**
    ```bash
pip install -r requirements.txt
Execute a aplicação:

streamlit run main.py


## ☁️ Deploy no Render

Para hospedar este projeto no [Render](https://render.com), siga estas etapas:

1.  Crie um novo **Web Service**.
2.  Conecte este repositório do GitHub.
3.  **Build Command:** `pip install -r requirements.txt`
4.  **Start Command:** `streamlit run main.py --server.port $PORT --server.address 0.0.0.0`
5.  **Variáveis de Ambiente:** Certifique-se de que o arquivo `packages.txt` esteja na raiz para que o Render instale as dependências de sistema (`libgl1` e `libglib2.0`).

## 📂 Estrutura do Projeto

```text
├── main.py            # Código principal da aplicação Streamlit
├── requirements.txt   # Bibliotecas Python necessárias
├── packages.txt       # Dependências de sistema (Linux)
└── README.md          # Documentação do projeto
📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Dica de Engenharia: Ao realizar o deploy, o primeiro carregamento pode demorar alguns segundos extras devido ao download automático dos pesos do modelo (yolov8n.pt) pelo SDK da Ultralytics.

Deseja que eu adicione alguma seção específica sobre como treinar um modelo customizado ou como configurar os limites de confiança da detecção?
