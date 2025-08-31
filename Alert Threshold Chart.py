import matplotlib.pyplot as plt

temps = [82.1, 84.3, 88.6, 92.7, 101.4]
timestamps = ["12:00", "12:01", "12:02", "12:03", "12:04"]

plt.plot(timestamps, temps, marker='o')
plt.axhline(y=100, color='r', linestyle='--', label='Critical Threshold')
plt.title('Temperature Monitoring Chart')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
