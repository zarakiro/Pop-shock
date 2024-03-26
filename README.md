# Pop-shock
Pop-shock is a connected rugby helmet for concussion prevention. It's an engineering master's project at IFT's ESILV school.

Pour utiliser le Pop-shock il est nécessaire d'avoir le matériel suivant:

-un casque de rugby

-une esp32C3 Beetle ou equivalent

-une batterie pour l'esp32C3 Beetle	

-4 capteurs piezoélectriques	

-1 accelerometre MPU6050	

-Des fils	

-Des resistances de 10 000 Ohm

Il faut brancher les capteurs piezoelectriques sur les pins analogiques du microcontroleur. Nous avons choisi les pins A1,A2,A3,A4.
Il faut faire un pont diviseur de tensions.
On relie le fil noir du piezo au GND. On divise le fil rouge en deux: une partie qui part vers un pin analogique et une autre avec une resistance de 10K Ohm relié au GND. Cela crée une reesistance pull down pour avoir des valeurs plus faibles.

Il faut brancher l'accelerometre sur les pins SDA et SCL (pins 8 et 9).

Une fois les branchements faits et les capteurs positionnés dans le casque, il faut implementer le code .ino sur l'esp32C3 Beetle grâce à Arduino IDE. Attention à bien choisir le bon port et la bonne board : ESPC3 Dev Module.

Une fois le code compilé, le microcontroleur va creer un reseau wifi nommé ESP32_Server. Il faut alors se connecter à ce reseau avec un ordinateur puis lancer le code python fourni (serveur_plot).

Une fois ces étapes faites, vous devriez avoir un casque de rugby qui détecte les chocs et envoie les données des chocs sur l'ordinateur connecté au reseau wifi de l'esp32C3 Beetle et qui affiche des graphiques pour l'accélérometre et les capteurs piezoelectriques.
