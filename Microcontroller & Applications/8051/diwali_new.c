#include <reg51.h>  // Header file for 8051 register definitions

// Delay function (approximate delay)
// Adjust the loop values as needed depending on clock speed
void delay() {
    int i, j;
    for (i = 0; i < 110; i++) {
        for (j = 0; j < 60; j++) {
            // Do nothing, just wait
        }
    }
}

void main() {
    while (1) {
        // LED Pattern: Left to right shift
        P1 = 0x80; P2 = 0x01; delay();  // 1000 0000 | 0000 0001
        P1 = 0x40; P2 = 0x02; delay();  // 0100 0000 | 0000 0010
        P1 = 0x20; P2 = 0x04; delay();  // 0010 0000 | 0000 0100
        P1 = 0x10; P2 = 0x08; delay();  // 0001 0000 | 0000 1000
        P1 = 0x08; P2 = 0x10; delay();  // 0000 1000 | 0001 0000
        P1 = 0x04; P2 = 0x20; delay();  // 0000 0100 | 0010 0000
        P1 = 0x02; P2 = 0x40; delay();  // 0000 0010 | 0100 0000
        P1 = 0x01; P2 = 0x80; delay();  // 0000 0001 | 1000 0000

        // All LEDs ON
        P1 = 0xFF; 
        P2 = 0xFF; 
        delay();
    }
}
