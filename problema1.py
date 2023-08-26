import requests

def precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        precio = data["bpi"]["USD"]["rate_float"]
        return precio
    except requests.RequestException:
        print("Error al obtener el precio de Bitcoin")
        return None

n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    
precio = precio_bitcoin()
if precio is not None:
    total = n * precio
    valor= f"${total:,.4f}"
    print(f"El costo actual de {n} Bitcoins es {valor} USD")
