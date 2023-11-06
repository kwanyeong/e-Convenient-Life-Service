#include <SPI.h> 
#include <MFRC522.h> //RFID header
#include <Wire.h> //I2C 통신

#define SS_PIN 10
#define RST_PIN 9
#define ESP32_ADDRESS 0x08 // 이 주소는 예시입니다. 원하는 I2C 주소로 변경할 수 있습니다.

MFRC522 rfid(SS_PIN, RST_PIN); // MFRC522 RFID센서 

void setup() {
  SPI.begin();
  rfid.PCD_Init();
  Wire.begin(); // I2C 통신 시작
  Serial.begin(115200);
}

//RFID 센서를 인식해서 서버로 전송 
void loop() {
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    Wire.beginTransmission(ESP32_ADDRESS);
    for (byte i = 0; i < rfid.uid.size; i++) {
      Wire.write(rfid.uid.uidByte[i]);
    }
    Wire.endTransmission();

    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();
  }
}