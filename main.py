import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Configuração inicial da página do Streamlit
st.set_page_config(
    page_title="Scanner com Yolo",
    layout="centered"
)

# Inicialização do modelo YOLO (utilizando o cache do Streamlit para otimizar o carregamento)
@st.cache_resource
def load_yolo_model():
    # Carrega a versão nano do YOLOv8, ideal para deploy leve no Render
    return YOLO("yolov8n.pt")

model = load_yolo_model()

# Interface do usuário: Título principal
st.title("Scanner com YOLOv8")
st.write("Abra a câmera para detectar objetos em tempo real via imagem.")

# Inicialização do estado da câmera no Streamlit session_state
if "run_camera" not in st.session_state:
    st.session_state.run_camera = False

# Botão para alternar o estado de ativação da câmera
if st.button("Ligar / Desligar Câmera"):
    st.session_state.run_camera = not st.session_state.run_camera

# Bloco lógico de captura e processamento da imagem
if st.session_state.run_camera:
    # Acessa o input de câmera nativo do Streamlit
    picture = st.camera_input("Posicione o objeto em frente à câmera")
    
    if picture:
        # Conversão da imagem capturada para o formato compatível com o OpenCV/Pillow
        img = Image.open(picture)
        img_array = np.array(img)
        
        # Execução da inferência do YOLO no frame capturado
        results = model(img_array)
        
        # Renderização dos resultados (boxes e labels) na imagem original
        annotated_frame = results[0].plot()
        
        # Exibição do resultado final processado na tela
        st.subheader("Resultado da Detecção:")
        st.image(annotated_frame, channels="RGB", use_column_width=True)
else:
    st.info("Clique no botão acima para ativar a câmera do dispositivo.")