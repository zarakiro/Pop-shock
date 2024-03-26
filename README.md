# Pop-Shock
Pop-shock is a connected rugby helmet designed for the prevention and management of concussions in sport. It embeds discreet electronics to obtain as much data as possible and promote the safety of players both professional and amateur players. Its design and comfort are indistinguishable from conventional rugby helmets. Pop-Shock uses an accelerometer and several pressure sensors distributed throughout the helmet. An alarm signal is sent directly via an application to the coach or medical staff as soon as a player receives a shock considered too violent. It's then easy to inform the referee so that the player in question can be taken out and undergo a concussion protocol. Although Pop-Shock may not perform as well as a custom-made mouthguard, its affordability and compatibility with all head sizes make it accessible to all rugby players, contributing to safety on the field.



# Tutorial

## Required Materials

To use Pop-shock, you will need the following materials:

- A rugby helmet
- An ESP32C3 Beetle board or equivalent
- A battery for the ESP32C3 Beetle
- 4 piezoelectric sensors
- 1 MPU6050 accelerometer
- Wires
- 10,000 Ohm resistors

## Installation

1. To connect the piezoelectric sensors, you'll need to plug them into the analog pins of the microcontroller, specifically utilizing pins A1, A2, A3, and A4. We've employed a voltage divider setup to ensure more practical readings. The black wire of the piezo should be connected to the ground (GND). As for the red wire, it should be split into two parts: one part goes to an analog pin, while the other part connects to a 10K Ohm resistor, ultimately linked to the ground (GND). This configuration establishes a pull-down resistor mechanism, aiding in obtaining lower values for accurate measurements.
2. Connect the accelerometer to the SDA and SCL pins (8 and 9).
3. Download and implement the .ino code on the ESP32C3 Beetle using the Arduino IDE. Make sure to choose the correct port and board: ESP32C3 Dev Module.
4. Once the code is compiled, the microcontroller will create a WiFi network named ESP32_Server. Connect your computer to this network and run the provided Python code (server_plot).

## Usage

Once these steps are completed, your rugby helmet will be ready to detect impacts and send data to the computer connected to the ESP32C3 Beetle's WiFi network. You can then visualize graphs for the accelerometer and piezoelectric sensors.
