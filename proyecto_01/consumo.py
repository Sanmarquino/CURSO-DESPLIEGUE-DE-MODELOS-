# Probar el consumo de api con codigo de python
import requests  

url = 'http://127.0.0.1:8000'

r = requests.get("http://127.0.0.1:8000/")
print(r.json())

paciente = {
  "sbp": 160,
  "Tabaco": 12,
  "ldl": 5.73,
  "Adiposidad": 23.11,
  "Familia": "Presente",
  "Tipo": 49,
  "Obesidad": 25.3,
  "Alcohol": 97.2,
  "Edad": 52
}

r = requests.post("http://127.0.0.1:8000/predecir", json=paciente)
print(r.json())

