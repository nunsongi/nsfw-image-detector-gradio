import gradio as gr
from transformers import pipeline
from PIL import Image

# 1. INICIALIZAR EL MODELO
# Esto se ejecuta una sola vez cuando arranca la app
print("Cargando modelo...")
classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")

# 2. DEFINIR LA FUNCIÓN LÓGICA
# Esta función recibe la imagen que sube el usuario
def predecir(imagen):
    if imagen is None:
        return None
    
    # El modelo analiza la imagen
    resultados = classifier(imagen)
    
    # Gradio necesita que le devolvamos un diccionario {'etiqueta': probabilidad}
    # Convertimos la lista que ya conoces a ese formato:
    diccionario_resultados = {}
    for resultado in resultados:
        diccionario_resultados[resultado['label']] = resultado['score']
        
    return diccionario_resultados

# 3. CREAR LA INTERFAZ (Gradio)
interfaz = gr.Interface(
    fn=predecir,  # ¿Qué función ejecutamos?
    inputs=gr.Image(type="pil", label="Sube tu imagen"), # ¿Qué entra?
    outputs=gr.Label(num_top_classes=2, label="Predicción"), # ¿Qué sale?
    title="🛡️ Detector de Contenido Seguro",
    description="Sube una imagen para analizar si contiene material explícito o es segura (Normal).",
    
)

# 4. LANZAR
if __name__ == "__main__":
    interfaz.launch()