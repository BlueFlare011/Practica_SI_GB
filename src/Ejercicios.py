import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

con = sqlite3.connect('../sqlite/PRACTICA1.db')

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

# Ejercicio 3
query = con.execute("SELECT * FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1")
cols = [column[0] for column in query.description]
dAlertsJul1 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT * FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 2")
cols = [column[0] for column in query.description]
dAlertsJul2 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT * FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 3")
cols = [column[0] for column in query.description]
dAlertsJul3 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT * FROM ALERTS WHERE STRFTIME('%m',dateTime) = '08' AND PRIORITY = 1")
cols = [column[0] for column in query.description]
dAlertsAgo1 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT * FROM ALERTS WHERE STRFTIME('%m',dateTime) = '08' AND PRIORITY = 2")
cols = [column[0] for column in query.description]
dAlertsAgo2 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT * FROM ALERTS WHERE STRFTIME('%m',dateTime) = '08' AND PRIORITY = 3")
cols = [column[0] for column in query.description]
dAlertsAgo3 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

    # Numero de observaciones
print("Julio, Grave")
print("Numero de observaciones: ",dAlertsJul1["sid"].count(),"\n")
print("Julio, Media")
print("Numero de observaciones: ",dAlertsJul2["sid"].count(),"\n")
print("Julio, Baja")
print("Numero de observaciones: ",dAlertsJul3["sid"].count(),"\n")
print("Agosto, Grave")
print("Numero de observaciones: ",dAlertsAgo1["sid"].count(),"\n")
print("Agosto, Media")
print("Numero de observaciones: ",dAlertsAgo2["sid"].count(),"\n")
print("Agosto, Baja")
print("Numero de observaciones: ",dAlertsAgo3["sid"].count(),"\n")

