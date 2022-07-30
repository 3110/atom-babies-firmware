#include "AtomBabies.h"

using namespace M5Stack_AtomBabies;

AtomBabies babies;

void setup(void) {
    babies.begin();
    babies.display();
}

void loop(void) {
    if (babies.update()) {
        babies.clear();
        babies.display();
    }
    if (M5.Btn.wasPressed()) {
        babies.toggleBlink();
    }
}
