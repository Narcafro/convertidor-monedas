import requests

API_KEY = "144e3a03db7906e1051c86ed"

def convertir(moneda_origen, moneda_destino, cantidad):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{moneda_origen}/{moneda_destino}/{cantidad}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    print("DEBUG - Respuesta de la API")
    print(datos)

    if datos.get("result") == "success":
        return datos["conversion_result"]
    else:
        print("❌ Error en la conversión.")
        return None

print("=== Convertidor de Monedas ===")
moneda_origen = input("Moneda origen (ej: EUR): ").upper()
moneda_destino = input("Moneda destino (ej: USD): ").upper()
try:
    cantidad = float(input("Cantidad: "))
    resultado = convertir(moneda_origen, moneda_destino, cantidad)

    if resultado is not None:
        print(f"{cantidad} {moneda_origen} = {float(resultado):.2f} {moneda_destino}")
    else:
        print("No se pudo realizar la conversión.")

except ValueError:
    print("Error: la cantidad debe ser un número.")

