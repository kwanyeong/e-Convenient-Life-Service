#include <Wire.h>
#include <Keypad.h>
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// LCD 설정
LiquidCrystal_I2C lcd(0x27, 16, 2);

// WiFi 설정
const char* ssid = "박지균의 iPhone";
const char* password = "qwertyuiop";
const char* serverName = "http://172.20.10.4:5000/fetch_name";

// 키패드 설정
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {27, 14, 12, 13};
byte colPins[COLS] = {26, 25, 17, 16};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  Serial.begin(115200);

  // LCD 초기화
  lcd.init();
  lcd.backlight();

  // 시작 메시지 출력
  lcd.setCursor(0, 0);
  lcd.print("Welcome ECO Users"); 

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  String inputStr = "";

  while (true) {
    char key = keypad.getKey();
    
    if (key != NO_KEY) {
      if (key == 'B') {
        inputStr = "";
      } else if (key == 'A') {
        Serial.println("Input Received: " + inputStr);
        sendDataToServer(inputStr);
        inputStr = "";
        printInputToLCD(inputStr);
      } else {
        inputStr += key;
        
        if (inputStr.length() > 16) {
          inputStr.remove(inputStr.length() - 1);
        }
      }
      
      printInputToLCD(inputStr);
      delay(100);
    }
  }
}

void printInputToLCD(String input) {
  lcd.setCursor(0, 1);
  lcd.print("                "); // Clear the row
  lcd.setCursor(0, 1);
  lcd.print(input);
}

void printInfoToLCD(const String& serverResponse) {
  DynamicJsonDocument doc(1024);
  deserializeJson(doc, serverResponse);
  
  if (!doc["error"].isNull()) {
    lcd.setCursor(0, 1);
    lcd.print("No data found   ");
  } else if (!doc["name"].isNull()) {
    String name = doc["name"].as<String>();
    String output = "Name: " + name;
    output += String(' ', 16 - output.length());
    lcd.setCursor(0, 1);
    lcd.print(output);
    delay(5000); // 5초간 출력 내용을 유지한 후 화면을 지웁
  } else {
    // 추가된 코드: 문제가 발생할 경우 더 많은 정보를 출력
    lcd.setCursor(0, 0);
    lcd.print("Server response:");
    lcd.setCursor(0, 1);
    lcd.print(serverResponse);
    delay(5000); // 5초간 출력 내용을 유지한 후 화면을 지웁
  }
  lcd.setCursor(0, 0);
  lcd.print("Welcome ECO Users");
  lcd.setCursor(0, 1);
  lcd.print("                "); 
}



void sendDataToServer(String input) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName + String("?uid=") + input);
    int httpResponseCode = http.GET();
    
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Server response: " + response);
      printInfoToLCD(response);
    } else {
      Serial.println("Error in sending request: " + httpResponseCode);
    }
    
    http.end();
  } else {
    Serial.println("Error in WiFi connection");
  }
}