import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

con = sqlite3.connect('../sqlite/PRACTICA1.db')

# Ejercicio 2
query = con.execute("SELECT * FROM DEVICES")
cols = [column[0] for column in query.description]
dDevices = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute(
    "select sum(case when ip = 'None' then 1 else 0 end + case when localization = 'None' then 1 else 0 end + case when services = 'None' then 1 else 0 end + case when insecures = 'None' then 1 else 0 end + case when vulnerabilities = 'None' then 1 else 0 end) as camposNone from devices;")
cols = [column[0] for column in query.description]
dDevicesNone = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT COUNT(PORT) AS ports FROM PORTS_DEVICE GROUP BY RTB_DEVICE")
cols = [column[0] for column in query.description]
dPortsDevice = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT * FROM ALERTS")
cols = [column[0] for column in query.description]
dAlerts = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

# Numero de dispositivos
print("Numero de dispositivos: ", dDevices["id"].count(), "\n")
# Numero de campos missing o none
print("Numero de campos missing: ", dDevicesNone["camposNone"].max(), "\n")
# Numero de alertas
print("Numero de alertas: ", dAlerts["sid"].count(), "\n")
# Media y DE del total de puertos abiertos
print("Puertos abiertos")
print("Media: ", dPortsDevice["ports"].mean())
print("Desviacion: ", dPortsDevice["ports"].std(), "\n")
# Media y DE del numero de servicios inseguros detectados
print("Servicios inseguros")
print("Media: ", dDevices["insecures"].mean())
print("Desviacion: ", dDevices["insecures"].std(), "\n")
# Media y DE del del numero de vulnerabilidades detectadas
print("Vulnerabilidades")
print("Media: ", dDevices["vulnerabilities"].mean())
print("Desviacion: ", dDevices["vulnerabilities"].std(), "\n")
# Valor minimo y maximo del total de puertos abiertos
print("Puertos abiertos")
print("Minimo: ", dPortsDevice["ports"].min())
print("Maximo: ", dPortsDevice["ports"].max(), "\n")
# Valor minimo y maximo del numero de vulnerabilidades detectadas
print("Vulnerabilidades detectadas")
print("Minimo: ", dDevices["vulnerabilities"].min())
print("Maximo: ", dDevices["vulnerabilities"].max(), "\n")

# Ejercicio 3
query = con.execute("SELECT vulnerabilities FROM DEVICES WHERE IP IN (SELECT ORIGIN FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1) OR  IP IN (SELECT DESTINATION FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1)")
cols = [column[0] for column in query.description]
dAlertsJul1 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT vulnerabilities FROM DEVICES WHERE IP IN (SELECT ORIGIN FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1) OR  IP IN (SELECT DESTINATION FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 2)")
cols = [column[0] for column in query.description]
dAlertsJul2 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT vulnerabilities FROM DEVICES WHERE IP IN (SELECT ORIGIN FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1) OR  IP IN (SELECT DESTINATION FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 3)")
cols = [column[0] for column in query.description]
dAlertsJul3 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT vulnerabilities FROM DEVICES WHERE IP IN (SELECT ORIGIN FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1) OR  IP IN (SELECT DESTINATION FROM ALERTS WHERE STRFTIME('%m',dateTime) = '08' AND PRIORITY = 1)")
cols = [column[0] for column in query.description]
dAlertsAgo1 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT vulnerabilities FROM DEVICES WHERE IP IN (SELECT ORIGIN FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1) OR  IP IN (SELECT DESTINATION FROM ALERTS WHERE STRFTIME('%m',dateTime) = '08' AND PRIORITY = 2)")
cols = [column[0] for column in query.description]
dAlertsAgo2 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

query = con.execute("SELECT vulnerabilities FROM DEVICES WHERE IP IN (SELECT ORIGIN FROM ALERTS WHERE STRFTIME('%m',dateTime) = '07' AND PRIORITY = 1) OR  IP IN (SELECT DESTINATION FROM ALERTS WHERE STRFTIME('%m',dateTime) = '08' AND PRIORITY = 3)")
cols = [column[0] for column in query.description]
dAlertsAgo3 = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

# Numero de observaciones
print("Julio, Grave")
print("Numero de observaciones: ", dAlertsJul1["vulnerabilities"].count(), "\n")
print("Julio, Media")
print("Numero de observaciones: ", dAlertsJul2["vulnerabilities"].count(), "\n")
print("Julio, Baja")
print("Numero de observaciones: ", dAlertsJul3["vulnerabilities"].count(), "\n")
print("Agosto, Grave")
print("Numero de observaciones: ", dAlertsAgo1["vulnerabilities"].count(), "\n")
print("Agosto, Media")
print("Numero de observaciones: ", dAlertsAgo2["vulnerabilities"].count(), "\n")
print("Agosto, Baja")
print("Numero de observaciones: ", dAlertsAgo3["vulnerabilities"].count(), "\n")
# Numero de valores ausentes
# Mediana
print("Julio, Grave")
print("Mediana: ", dAlertsJul1["vulnerabilities"].median(), "\n")
print("Julio, Media")
print("Mediana: ", dAlertsJul2["vulnerabilities"].median(), "\n")
print("Julio, Baja")
print("Mediana: ", dAlertsJul3["vulnerabilities"].median(), "\n")
print("Agosto, Grave")
print("Mediana: ", dAlertsAgo1["vulnerabilities"].median(), "\n")
print("Agosto, Media")
print("Mediana: ", dAlertsAgo2["vulnerabilities"].median(), "\n")
print("Agosto, Baja")
print("Mediana: ", dAlertsAgo3["vulnerabilities"].median(), "\n")
# Media
print("Julio, Grave")
print("Media: ", dAlertsJul1["vulnerabilities"].mean(), "\n")
print("Julio, Media")
print("Media: ", dAlertsJul2["vulnerabilities"].mean(), "\n")
print("Julio, Baja")
print("Media: ", dAlertsJul3["vulnerabilities"].mean(), "\n")
print("Agosto, Grave")
print("Media: ", dAlertsAgo1["vulnerabilities"].mean(), "\n")
print("Agosto, Media")
print("Media: ", dAlertsAgo2["vulnerabilities"].mean(), "\n")
print("Agosto, Baja")
print("Media: ", dAlertsAgo3["vulnerabilities"].mean(), "\n")
# Varianza
print("Julio, Grave")
print("Varianza: ", dAlertsJul1["vulnerabilities"].var(), "\n")
print("Julio, Media")
print("Varianza: ", dAlertsJul2["vulnerabilities"].var(), "\n")
print("Julio, Baja")
print("Varianza: ", dAlertsJul3["vulnerabilities"].var(), "\n")
print("Agosto, Grave")
print("Varianza: ", dAlertsAgo1["vulnerabilities"].var(), "\n")
print("Agosto, Media")
print("Varianza: ", dAlertsAgo2["vulnerabilities"].var(), "\n")
print("Agosto, Baja")
print("Varianza: ", dAlertsAgo3["vulnerabilities"].var(), "\n")
# Maximo y minimo
print("Julio, Grave")
print("Maximo: ", dAlertsJul1["vulnerabilities"].max())
print("Minimo: ", dAlertsJul1["vulnerabilities"].min(), "\n")
print("Julio, Media")
print("Maximo: ", dAlertsJul2["vulnerabilities"].max())
print("Minimo: ", dAlertsJul2["vulnerabilities"].min(), "\n")
print("Julio, Baja")
print("Maximo: ", dAlertsJul3["vulnerabilities"].max())
print("Minimo: ", dAlertsJul3["vulnerabilities"].min(), "\n")
print("Agosto, Grave")
print("Maximo: ", dAlertsAgo1["vulnerabilities"].max())
print("Minimo: ", dAlertsAgo1["vulnerabilities"].min(), "\n")
print("Agosto, Media")
print("Maximo: ", dAlertsAgo2["vulnerabilities"].max())
print("Minimo: ", dAlertsAgo2["vulnerabilities"].min(), "\n")
print("Agosto, Baja")
print("Maximo: ", dAlertsAgo3["vulnerabilities"].max())
print("Minimo: ", dAlertsAgo3["vulnerabilities"].min(), "\n")

# Ejercicio 4
# 10 IPs de origen mas problematicas en un grafico de barras
query = con.execute("SELECT ORIGIN, COUNT(*) AS num FROM ALERTS GROUP BY ORIGIN ORDER BY num DESC LIMIT 10;")
data = query.fetchall()
df_problematic_ips = pd.DataFrame(data, columns=['origin', 'num'])
df_problematic_ips.plot(kind='bar', x='origin', y='num')
plt.title("10 IPs origen mas problematicas")
plt.show()
# Numero de alertas en el tiempo en una serie temporal
query = con.execute("SELECT DATETIME, COUNT(*) AS num FROM ALERTS GROUP BY DATETIME ORDER BY DATETIME ASC;")
data = query.fetchall()
df_alerts_category = pd.DataFrame(data, columns=['datetime', 'num'])
df_alerts_category.plot(kind='line', x='datetime', y='num')
plt.title("Alertas en el tiempo")
plt.show()
# Numero de alertas por categoria en grafico de barras
query = con.execute("SELECT CLASSIFICATION, COUNT(*) AS num FROM ALERTS GROUP BY CLASSIFICATION ORDER BY num DESC;")
data = query.fetchall()
df_alerts_category = pd.DataFrame(data, columns=['classification', 'num'])
df_alerts_category.plot(kind='bar', x='classification', y='num')
plt.title("Alertas por categoria")
plt.show()
# Dispositivos mas vulnerables (Servicios y vulnerabilidades)
query = con.execute("SELECT IP, (SERVICES+VULNERABILITIES) AS secure FROM DEVICES ORDER BY secure DESC;")
data = query.fetchall()
df_alerts_category = pd.DataFrame(data, columns=['ip', 'secure'])
df_alerts_category.plot(kind='bar', x='ip', y='secure')
plt.title("Dispositivos mas vulnerables")
plt.show()
# Media de puertos abiertos frente a servicios inseguros y total de servicios
