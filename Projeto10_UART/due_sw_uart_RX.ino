#include "sw_uart.h"

due_sw_uart uart;

void setup() {
  Serial.begin(115200);
  sw_uart_setup(&uart, 8, 9, 1, 8, SW_UART_EVEN_PARITY);
}

void loop() {
 test_receive();
 delay(1);
}



void test_receive() {
  char data;
  int code = sw_uart_receive_byte(&uart, &data);
  if(code == SW_UART_SUCCESS) {
     Serial.print(data);
  } else if(code == SW_UART_ERROR_PARITY) {
    Serial.println("\nPARITY ERROR");
  } else {
    Serial.println("\nOTHER");
    Serial.print(code);
  }
}
