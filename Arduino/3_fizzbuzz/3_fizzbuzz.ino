/**
 * In a range of numbers, if the current number is perfectly divided by 3
 * then light an led. If it is perfectly divided by 5 then light another
 * led. If it is divided perfectly by both numbers, light then all.
 * 
 * In any other situation just print the number to Serial.
 * 
*/


int FizzLED_pin = 11;
int BuzzLED_pin = 12;

void setup() {
    pinMode(FizzLED_pin, OUTPUT);
    pinMode(BuzzLED_pin, OUTPUT);
    Serial.begin(9600);
}

void loop () {
    for (int i = 1; i <= 255; i++){
        bool lightEmUp = false;
        if (i%3 == 0) {
            digitalWrite(FizzLED_pin, HIGH);
            lightEmUp = true;
        }
        if (i%5 == 0) {
            digitalWrite(BuzzLED_pin, HIGH);
            lightEmUp = true;
        }
        if (lightEmUp == false){
            Serial.println(i);
        }
        
        delay(500);
        digitalWrite(BuzzLED_pin, LOW);
        digitalWrite(FizzLED_pin, LOW);
        delay(500);
    }
}


