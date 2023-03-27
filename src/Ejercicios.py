import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

con = sqlite3.connect('./sqlite-tools-win32-x86-3410000/PRACTICA1.db')

# Ejercicio 2
query = con.execute("SELECT * FROM DEVICES")
cols = [column[0] for column in query.description]
dDevices = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT COUNT(PORT) AS ports FROM PORTS_DEVICE GROUP BY RTB_DEVICE")
cols = [column[0] for column in query.description]
dPortsDevice = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * FROM ALERTS")
cols = [column[0] for column in query.description]
dAlerts = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

    # Numero de dispositivos y campos missing o none
print("Numero de dispositivos: ",dDevices["id"].count(),"\n")
    # Numero de alertas
print("Numero de alertas: ",dAlerts["sid"].count(),"\n")
    # Media y DE del total de puertos abiertos
print("Puertos abiertos")
print("Media: ",dPortsDevice["ports"].mean())
print("Desviacion: ",dPortsDevice["ports"].std(),"\n")
    # Media y DE del numero de servicios inseguros detectados
print("Servicios inseguros")
print("Media: ",dDevices["insecures"].mean())
print("Desviacion: ",dDevices["insecures"].std(),"\n")
    # Media y DE del del numero de vulnerabilidades detectadas
print("Vulnerabilidades")
print("Media: ",dDevices["vulnerabilities"].mean())
print("Desviacion: ",dDevices["vulnerabilities"].std(),"\n")
    # Valor minimo y maximo del total de puertos abiertos
print("Puertos abiertos")
print("Minimo: ",dPortsDevice["ports"].min())
print("Maximo: ",dPortsDevice["ports"].max(),"\n")
    # Valor minimo y maximo del numero de vulnerabilidades detectadas
print("Vulnerabilidades detectadas")
print("Minimo: ",dDevices["vulnerabilities"].min())
print("Maximo: ",dDevices["vulnerabilities"].max(),"\n")
