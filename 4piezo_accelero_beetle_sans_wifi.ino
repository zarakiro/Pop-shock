#include <WiFi.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
Adafruit_MPU6050 mpu;

const char *ssid = "ESP32_Server"; // Nom du réseau Wi-Fi créé par l'ESP32C3
const char *password = "password"; // Mot de passe du réseau Wi-Fi
const int sensor1=1;//piezo gauche
const int sensor2=2;//piezo droite
const int sensor3=4;//piezo devant
const int sensor4=3;// a changer parce que adc2 pas pris encompte mais piezzo au dessus

WiFiServer server(12345); // Création d'un serveur TCP sur le port 12345

void setup() {
  Serial.begin(921600);
  Serial.println("SETUP");
  Serial.println("Adafruit MPU6050 test!");
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.println("Sensor set");
  // Initialisation du mode point d'accès Wi-Fi
  WiFi.softAP(ssid, password);
  delay(100);

  // Obtention de l'adresse IP du point d'accès
  IPAddress IP = WiFi.softAPIP();
  Serial.print("Adresse IP du serveur : ");
  Serial.println(IP);

  server.begin(); // Démarrage du serveur
}

void loop() {
      // calcul données accelero
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);
      float AccTotal = sqrt(pow(a.acceleration.x, 2) + pow(a.acceleration.y, 2) + pow(a.acceleration.z, 2)) / 9.81 - 1; // Conversion en g
      //Calcul piezo
      int piezoValues[4];
      piezoValues[0] = analogRead(sensor1);
      piezoValues[1] = analogRead(sensor2);
      piezoValues[2] = analogRead(sensor3);
      piezoValues[3] = analogRead(sensor4);
      
      //Print en serial pour vérifier
      Serial.print(AccTotal);
      Serial.print(",");
      Serial.print(piezoValues[0]);
      Serial.print(",");
      Serial.print(piezoValues[1]);
      Serial.print(",");
      Serial.print(piezoValues[2]);
      Serial.print(",");
      Serial.println(piezoValues[3]);

      delay(200); // Délai d'attente entre chaque envoi de données
  }
