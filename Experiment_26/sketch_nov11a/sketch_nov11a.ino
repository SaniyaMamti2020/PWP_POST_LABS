void setup() {
  pinMode(13, OUTPUT);   // Set pin 13 (built-in LED) as output
  Serial.begin(9600);    // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {   // Check if data received
    char command = Serial.read(); // Read the incoming command

    if (command == '1') {
      digitalWrite(13, HIGH);     // Turn ON LED
    } 
    else if (command == '0') {
      digitalWrite(13, LOW);      // Turn OFF LED
    }
  }
}
