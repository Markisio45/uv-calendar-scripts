import json
from ics import Calendar, Event
from datetime import datetime

# Leer el archivo JSON
with open('calendario.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Crear un calendario
calendar = Calendar()

# Iterar sobre los eventos en el JSON
for event in data:
    e = Event()
    e.name = event.get('nombre_asignatura', 'Sin nombre')
    e.begin = event['inicio']
    e.end = event['fin']
    e.location = event.get('nombre_lugar', 'Sin lugar')
    e.description = f"Actividad: {event.get('nombre_actividad', 'Sin actividad')}\nProfesor: {event['profesores'][0]['nombre_profesor'] if event.get('profesores') else 'Sin profesor'}"
    
    # AÃ±adir el evento al calendario
    calendar.events.add(e)

# Guardar el calendario en un archivo .ics
with open('calendario.ics', 'w', encoding='utf-8') as file:
    file.writelines(calendar)