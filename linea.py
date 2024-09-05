import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
arrival_rate = 1.0  # Tasa de llegada promedio (clientes por minuto)
service_rate = 1.5  # Tasa de servicio promedio (clientes atendidos por minuto)
num_customers = 1000  # Número total de clientes a simular

# Inicializar tiempos de llegada y de servicio
inter_arrival_times = np.random.exponential(1 / arrival_rate, num_customers)
service_times = np.random.exponential(1 / service_rate, num_customers)

# Calcular el tiempo de llegada acumulado para cada cliente
arrival_times = np.cumsum(inter_arrival_times)

# Simular el tiempo en el que cada cliente comienza y termina su servicio
start_times = np.zeros(num_customers)
finish_times = np.zeros(num_customers)

for i in range(1, num_customers):
    # El tiempo de inicio es cuando llega el cliente o cuando termina el cliente anterior, lo que sea mayor
    start_times[i] = max(arrival_times[i], finish_times[i - 1])
    # El tiempo de finalización es el tiempo de inicio más el tiempo de servicio
    finish_times[i] = start_times[i] + service_times[i]

# Calcular los tiempos de espera (diferencia entre el inicio del servicio y la llegada)
waiting_times = start_times - arrival_times

# Calcular estadísticas
average_waiting_time = np.mean(waiting_times)
average_service_time = np.mean(service_times)
average_system_time = np.mean(finish_times - arrival_times)  # Tiempo total en el sistema

print(f"Tiempo promedio de espera: {average_waiting_time:.2f} minutos")
print(f"Tiempo promedio de servicio: {average_service_time:.2f} minutos")
print(f"Tiempo promedio total en el sistema: {average_system_time:.2f} minutos")

# Visualización de la simulación
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, label="Tiempo de llegada")
plt.plot(start_times, label="Inicio de servicio")
plt.plot(finish_times, label="Finalización del servicio")
plt.xlabel("Cliente")
plt.ylabel("Tiempo (minutos)")
plt.title("Simulación de una Cola de Espera (M/M/1)")
plt.legend()
plt.show()
