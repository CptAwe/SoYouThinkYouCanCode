
// The pins of each LED are stored into an array
int LED_pins[] = {11, 12, 13};


void setup() {
    // Run the command pinMode( <...> , OUTPUT) for each LED pin
    for (byte i=0; i<= 2; i++) {
        pinMode(LED_pins[i], OUTPUT);
    }
}


void loop() {
    // Turn on each LED one by one
    for (byte i=0; i<= 2; i++) {
        digitalWrite(LED_pins[i], HIGH);
        delay(500);
    }

    // Turn off each LED one by one in reverse order
    for (byte i=2; i>=0; i--) {
        digitalWrite(LED_pins[i], LOW);
        delay(500);
    }

    // I want them to stay off for a sec to make the effect visible
    delay(1000);
}