import socket
import matplotlib.pyplot as plt

# Adresse IP et port de l'ESP32C3
ESP32C3_IP = '192.168.4.1'  # Adresse IP du point d'accès Wi-Fi de l'ESP32C3
ESP32C3_PORT = 12345  # Port utilisé par l'ESP32C3

# Créer un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((ESP32C3_IP, ESP32C3_PORT))
print("Connecté à l'ESP32C3")

# Initialisation des listes pour les données
x_values_acc = []
y_values_acc = []
x_values_piezo = [[] for _ in range(4)]
y_values_piezo = [[] for _ in range(4)]

# Création des graphiques
fig_acc, ax_acc = plt.subplots()
fig_piezo, axs_piezo = plt.subplots(4, 1, figsize=(8, 10))

# Fonction de mise à jour des graphiques
def update_plots(data):
    global x_values_acc, y_values_acc, x_values_piezo, y_values_piezo
    
    data_splited = data.split('\r\n')
    data_values_splited = data_splited[0].split(",")
    
    if data_values_splited[0].strip():  # Vérifie si la première valeur n'est pas vide
        acc_value = float(data_values_splited[0])
    else:
        acc_value = None
    
    piezo_values = []
    for value in data_values_splited[1:]:
        if value.strip():
            piezo_values.append(float(value.strip()))
    
    if acc_value is not None:
        x_values_acc.append(len(x_values_acc))
        y_values_acc.append(acc_value)
    
    for i, (piezo_value, ax_piezo) in enumerate(zip(piezo_values, axs_piezo)):
        x_values_piezo[i].append(len(x_values_piezo[i]))
        y_values_piezo[i].append(piezo_value)
    
    ax_acc.clear()
    ax_acc.plot(x_values_acc, y_values_acc)
    ax_acc.set_title('Accéléromètre')
    ax_acc.set_xlabel('Temps')
    ax_acc.set_ylabel('Valeur')
    
    for i, ax_piezo in enumerate(axs_piezo):
        ax_piezo.clear()
        ax_piezo.plot(x_values_piezo[i], y_values_piezo[i])
        ax_piezo.set_title(f'Capteur piezo {i+1}')
        ax_piezo.set_xlabel('Temps')
        ax_piezo.set_ylabel('Valeur')
    
    plt.pause(0.1)  # Petit délai pour rafraîchir le graphique

# Boucle pour recevoir les données et mettre à jour les graphiques
try:
    while True:
        data = client_socket.recv(1024).decode().strip()
        if not data:
            break
        update_plots(data)
        
except KeyboardInterrupt:
    print("Arrêt de la connexion.")

# Fermer le socket client
client_socket.close()

# Affichage des graphiques
plt.tight_layout()
plt.show()
