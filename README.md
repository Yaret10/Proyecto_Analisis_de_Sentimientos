# Proyecto de Analisis de Sentimientos

Aplicacion web para analizar sentimientos en comentarios de hoteles. El proyecto permite comparar un modelo base de Hugging Face con un modelo fine-tuned local usando una API desarrollada con FastAPI y una interfaz web hecha con HTML, CSS y JavaScript.

## Caracteristicas

- Login simple con token de autenticacion.
- Interfaz web para ingresar comentarios.
- Prediccion con modelo base.
- Prediccion con modelo fine-tuned.
- Comparacion entre ambos modelos.
- Generacion de data sintetica de comentarios hoteleros.
- Prediccion masiva sobre archivos CSV.
- API documentada automaticamente con Swagger UI.

## Tecnologias Usadas

- Python
- FastAPI
- Uvicorn
- Pandas
- Transformers
- PyTorch
- Pydantic
- Scikit-learn
- Hugging Face
- HTML, CSS y JavaScript

## Estructura del Proyecto

```txt
Proyecto_Analisis_de_Sentimientos/
|-- api/
|   |-- auth.py
|   |-- main.py
|   |-- model_service.py
|   `-- schemas.py
|-- data/
|   `-- processed/
|-- models/
|   `-- robertuito_finetuned/
|-- notebooks/
|-- src/
|   |-- batch_predict.py
|   `-- generar_data_sintetica.py
|-- web/
|   |-- app.js
|   |-- index.html
|   |-- login.html
|   `-- styles.css
|-- .gitignore
|-- README.md
`-- requirements.txt
```

## Modelos Utilizados

El proyecto usa dos modelos:

```txt
Modelo base:
pysentimiento/robertuito-sentiment-analysis
```

```txt
Modelo fine-tuned local:
models/robertuito_finetuned
```

Importante: la carpeta `models/` esta ignorada por Git porque normalmente contiene archivos pesados. Si otra persona clona el repositorio, debera colocar el modelo fine-tuned en:

```txt
models/robertuito_finetuned
```

Si no se coloca ese modelo, la API puede fallar al iniciar porque `api/model_service.py` intenta cargarlo.

## Requisitos Previos

Antes de ejecutar el proyecto necesitas tener instalado:

- Python 3.10 o superior
- pip
- Git

Opcional:

- ngrok, si quieres compartir la app con otros dispositivos usando un link publico.

## Configuracion del Proyecto

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd Proyecto_Analisis_de_Sentimientos
```

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

En macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Verificar el modelo fine-tuned

El modelo fine-tuned debe existir en:

```txt
models/robertuito_finetuned
```

Dentro de esa carpeta deben estar los archivos del modelo y tokenizer, por ejemplo archivos como:

```txt
config.json
tokenizer.json
model.safetensors
```

Los nombres exactos pueden variar segun como se haya guardado el modelo.

## Ejecucion Local

Ejecuta la API desde la raiz del proyecto:

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Luego abre en el navegador:

```txt
http://127.0.0.1:8000
```

La aplicacion mostrara la pantalla de login.

Credenciales de prueba:

```txt
Usuario: admin
Contrasena: 123456
```

## Documentacion de la API

FastAPI genera documentacion automatica. Con el servidor ejecutandose, abre:

```txt
http://127.0.0.1:8000/docs
```

Tambien puedes usar:

```txt
http://127.0.0.1:8000/redoc
```

## Endpoints Principales

### Login

```txt
POST /login
```

Body:

```json
{
  "username": "admin",
  "password": "123456"
}
```

Respuesta:

```json
{
  "access_token": "mi_token_secreto",
  "token_type": "bearer"
}
```

### Prediccion con modelo base

```txt
POST /predict/base
```

### Prediccion con modelo fine-tuned

```txt
POST /predict/finetuned
```

### Comparacion de modelos

```txt
POST /predict/compare
```

Body para predicciones:

```json
{
  "text": "La habitacion estaba limpia y el personal fue amable."
}
```

Los endpoints de prediccion requieren el token en el header:

```txt
Authorization: Bearer mi_token_secreto
```

## Uso con ngrok

Este proyecto esta configurado para que FastAPI sirva tanto la interfaz web como la API. Por eso solo necesitas un tunel.

Primero ejecuta la API:

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Luego, en otra terminal:

```bash
ngrok http 8000
```

Ngrok generara una URL publica parecida a:

```txt
https://nombre-ngrok.ngrok-free.dev
```

Abre esa URL desde tu telefono u otro dispositivo.

## Scripts Auxiliares

### Generar data sintetica

Este script crea un CSV con comentarios simulados de hoteles:

```bash
python src/generar_data_sintetica.py
```

Salida esperada:

```txt
data/processed/comentarios_hoteles_sintetico.csv
```

### Prediccion por lote

Este script lee un CSV, aplica el modelo fine-tuned y genera un archivo con predicciones:

```bash
python src/batch_predict.py
```

Entrada:

```txt
data/processed/comentarios_hoteles_sintetico.csv
```

Salida:

```txt
data/processed/comentarios_hoteles_predicho.csv
```

## Notas Importantes para GitHub

- No subir entornos virtuales como `.venv/`.
- No subir archivos pesados de modelos.
- No subir datasets grandes.
- No subir archivos `.env` con secretos.
- La carpeta `models/` esta ignorada en `.gitignore`.
- Los archivos CSV tambien estan ignorados para evitar subir datos generados o pesados.

Si el modelo fine-tuned es necesario para ejecutar el proyecto, se recomienda documentar de donde descargarlo o subirlo a un servicio externo como Hugging Face Hub, Google Drive o similar.

## Problemas Comunes

### La API no inicia

Puede ocurrir si falta el modelo fine-tuned en:

```txt
models/robertuito_finetuned
```

Verifica que la carpeta exista y contenga los archivos del modelo.

### El login no funciona desde el telefono

Verifica que estes usando:

```bash
ngrok http 8000
```

No uses:

```bash
python -m http.server 5500
```

En esta version, FastAPI sirve la web y la API desde el mismo puerto.

### La pagina no carga estilos o JavaScript

Verifica que en los HTML se usen las rutas:

```html
<link rel="stylesheet" href="/static/styles.css" />
<script src="/static/app.js"></script>
```

## Autor

Proyecto desarrollado como parte del curso de Aprendizaje Automatico.
