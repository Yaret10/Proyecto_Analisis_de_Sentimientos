import pandas as pd
import random
from datetime import datetime, timedelta

comentarios = [
    "La habitación estaba muy limpia y el personal fue amable.",
    "El aire acondicionado no funcionaba y nadie me ayudó.",
    "El desayuno estuvo bien, pero podría tener más variedad.",
    "Excelente ubicación y muy buena atención.",
    "La cama era incómoda y había mucho ruido por la noche.",
    "Todo estuvo correcto durante mi estadía.",
    "El baño estaba sucio cuando llegamos.",
    "Muy buena experiencia, volvería otra vez.",
    "La recepción demoró demasiado en atendernos.",
    "El hotel cumplió con lo esperado."
]

fuentes = ["Google Reviews", "Booking", "TripAdvisor", "Encuesta interna", "WhatsApp"]

data = []

for i in range(1, 501):
    fecha = datetime.today() - timedelta(days=random.randint(0, 180))

    data.append({
        "comentario_id": i,
        "cliente_id": random.randint(1000, 9999),
        "hotel_id": random.choice(["HOTEL_001", "HOTEL_002", "HOTEL_003"]),
        "fecha": fecha.strftime("%Y-%m-%d"),
        "texto": random.choice(comentarios),
        "fuente": random.choice(fuentes)
    })

df = pd.DataFrame(data)

df.to_csv("data/processed/comentarios_hoteles_sintetico.csv", index=False, encoding="utf-8")

print("CSV generado correctamente")
