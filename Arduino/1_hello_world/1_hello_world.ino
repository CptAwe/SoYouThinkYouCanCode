int onboard_led_pin = 13;

void setup() {
    pinMode(onboard_led_pin, OUTPUT);
}


void loop() {
    digitalWrite(onboard_led_pin, HIGH);
    delay(500);
    digitalWrite(onboard_led_pin, LOW);
    delay(500);
}