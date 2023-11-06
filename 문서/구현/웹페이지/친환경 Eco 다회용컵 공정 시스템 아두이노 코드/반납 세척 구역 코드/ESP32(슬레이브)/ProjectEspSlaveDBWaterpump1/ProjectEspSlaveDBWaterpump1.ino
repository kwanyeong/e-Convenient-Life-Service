#include <Wire.h>       //ESP 통신
#include <Arduino.h>    //아두이노 코드
#include <WiFi.h>       //Wifi 통신
#include <HTTPClient.h> //HTTP 

#define MOTOR_PIN_A 16 //컨베이어벨트 motor
#define MOTOR_PIN_B 17 //컨베이어벨트 motor
#define I2C_ADDRESS 0x08
#define TRIGGER_PIN_1 12 //초음파 송신
#define ECHO_PIN_1 13    //초음파 수신
#define TRIGGER_PIN_2 26 //초음파 송신
#define ECHO_PIN_2 25    //초음파 수신
#define DELAY_STOP_MOTOR 10000 //motor 정지 dela설정
#define DELAY_WATER_PUMP 5000
#define DISTANCE_THRESHOLD 16.5 //초음파센서 감지거리
#define L9110S_IA 14 // waterpump; 바뀐 부분: L9110S IA 핀 번호
#define L9110S_IB 27 // waterpump; 바뀐 부분: L9110S IB 핀 번호

byte uid[4];
bool rfidDetected = false;
unsigned long rfidDetectedTime = 0;
unsigned long stopTime = 0;
bool motorStopped = false;
bool secondSensorReached = false;
bool waterPumpActivated = false;
unsigned long waterPumpActivatedTime = 0;

const char* SSID = "박지균의 iPhone"; //핫스팟 Wifi ID
const char* PASSWORD = "qwertyuiop"; //핫스팟 Wifi PW

void setup() {
  pinMode(MOTOR_PIN_A, OUTPUT);
  pinMode(MOTOR_PIN_B, OUTPUT);
  pinMode(TRIGGER_PIN_1, OUTPUT);
  pinMode(ECHO_PIN_1, INPUT);
  pinMode(TRIGGER_PIN_2, OUTPUT);
  pinMode(ECHO_PIN_2, INPUT);
  pinMode(L9110S_IA, OUTPUT); // 바뀐 부분: L9110S IA 핀 설정
  pinMode(L9110S_IB, OUTPUT); // 바뀐 부분: L9110S IB 핀 설정
  Wire.begin(I2C_ADDRESS);
  Wire.onReceive(receiveEvent);
  Serial.begin(115200); //Serial 통신 115200;
  connectToWifi();
}

void loop() {
  if (rfidDetected) {
    sendDataToDatabase(uid);
    float distance1 = getDistance(TRIGGER_PIN_1, ECHO_PIN_1);
    float distance2 = getDistance(TRIGGER_PIN_2, ECHO_PIN_2);

    if (!motorStopped && !secondSensorReached && distance1 <= DISTANCE_THRESHOLD) {
      // 첫 번째 센서에 물체가 가까이 있으면 10초 동안 컨베이어벨트 모터를 멈춤
      stopMotor();
      motorStopped = true;
      stopTime = millis(); //현재 시각을 1000분의 1초 단위로 선언

      // 워터 펌프 모터 작동 (conveyor belt 처럼 핀값을 반대로 설정해야 작동됨.)
      if (!waterPumpActivated) {
          digitalWrite(L9110S_IA, HIGH); // 바뀐 부분: L9110S IA 핀에 HIGH 전송
          digitalWrite(L9110S_IB, LOW); // 바뀐 부분: L9110S IB 핀에 LOW 전송
          waterPumpActivated = true;
          waterPumpActivatedTime = millis();
      }
    } else if (motorStopped && !secondSensorReached && !secondSensorReached) {
      if (millis() - stopTime >= DELAY_STOP_MOTOR){ //현재시각에서 감지했을때 시각까지 10초동안 정지 (DELAY_STOP_MOTOR 참고)
        runMotor(); //작동개시
        motorStopped = false; 
      }
      else{
        stopMotor();
      }

      if (waterPumpActivated && millis() - waterPumpActivatedTime >= DELAY_WATER_PUMP) {
        digitalWrite(L9110S_IA, LOW); // 바뀐 부분: L9110S IA 핀에 LOW 전송
        digitalWrite(L9110S_IB, LOW); // 바뀐 부분: L9110S IB 핀에 LOW 전송
        waterPumpActivated = false;
      }
    } else if (!secondSensorReached && distance2 <= 13) { //DISTANCE_THRESHOLD
      // 두 번째 센서에 물체가 가까이 있으면 모터를 멈춤
      stopMotor();
      secondSensorReached = true;
    } else if (!secondSensorReached) {
      // 모터 실행
      runMotor();
      motorStopped = false;
    }
  }
}

void runMotor() {
  // 컨베이어벨트 servo모터 방향설정: A핀과 B핀의 값을 반대로 설정함.
  digitalWrite(MOTOR_PIN_A, HIGH);
  digitalWrite(MOTOR_PIN_B, LOW);
}

void stopMotor() {
  digitalWrite(MOTOR_PIN_A, LOW);
  digitalWrite(MOTOR_PIN_B, LOW);
}

float getDistance(int triggerPin, int echoPin) {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2); // delay를 줘야 작동하는데(오류발생 최소화) delay를 최소로 주기 위해 선언
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(2);
  digitalWrite(triggerPin, LOW);
  float duration = pulseIn(echoPin, HIGH);
  float distance = (duration * 0.0344) / 2; //음속 거리계산
  return distance;
}

// numBytes : RFID 아두이노 고유번호
void receiveEvent(int numBytes) {
  for (int i = 0; i < numBytes; i++) {
    uid[i] = Wire.read();
  }
  rfidDetected = true;
  secondSensorReached = false;
}


//Wifi 연결 확인
void connectToWifi() {
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to Wi-Fi...");
  }
  Serial.println("Connected to Wi-Fi");
}


//sizeof ?
//HTTPClient ?
void sendDataToDatabase(byte* uid) {
  char uidHex[9];
  snprintf(uidHex, sizeof(uidHex), "%02X%02X%02X%02X", uid[0], uid[1], uid[2], uid[3]);
  HTTPClient http;
  http.begin("http://172.31.98.241:5080/rfid-data");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  String requestData = String("uid=") + uidHex;
  int responseCode = http.POST(requestData);
  if (responseCode > 0) { //RFID가 서버에 전송됐으면
    String response = http.getString(); //전송 성공
    Serial.print("Server response: ");
    Serial.println(response);
  } else { //전송이 안되면
    Serial.print("Error sending data to server. HTTP error: ");
    Serial.println(responseCode);
  }
  http.end();
}