



#include "WiFi.h"
#include "Wire.h"
// #include <BlynkSimpleEsp32.h>
#include <LiquidCrystal_I2C.h>  // https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library.git
#include <HTTPClient.h>
#include <ArduinoJson.h>  // https://github.com/bblanchon/ArduinoJson.git
#include <ESPping.h> // https://github.com/dvarrel/ESPping


const int pH_pin = A13;

int pH_analog;
float Voltage;

const bool IoT_mode = true;  // true means 'on'
char* SSID = "RACHMAN";
char* PASSWORD = "20111996";

// untuk kalibrasi
float PH4 = 3.3;
float PH7 = 2.40;  // ori: 2.91

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Wire.begin();
  Serial.begin(9600);
  if (IoT_mode) {
    initWiFi(SSID, PASSWORD);
    // Blynk.config(BLYNK_AUTH_TOKEN);
    bool internetAvailability = Ping.ping("192.168.1.10", 3);
    if (internetAvailability) {
      Serial.println("[INFO] Internet Available");
    } else {
      ESP.restart();
    }
  }
  pinMode(pH_pin, INPUT);

  lcd.begin();
  lcd.backlight();
  lcd.print("Alat pH");
  delay(5000);
  lcd.clear();
}

void loop() {
  if (IoT_mode) {
    // Blynk.run();
    Serial.println("[INFO] IoT mode: ON");
  } else {
    Serial.println("[INFO] IoT mode: OFF");
  }

  pH_analog = analogRead(pH_pin);
  Serial.print("ADC pH: ");
  Serial.println(pH_analog);

  Voltage = pH_analog * (5.0 / 4095.0) + 3.2;
  Serial.print("Voltage: ");
  Serial.println(Voltage);

  float pH_step = (PH4 - PH7) / 3;
  float Po = abs(7.00 + ((PH7 - Voltage) / pH_step));
  Serial.print("pH cairan: ");
  Serial.println(Po, 2);

  char* status = determine_status(Po);
  Serial.print("Status: ");
  Serial.println(status);
  display_result(Po, status);

  delay(1000);

  if (IoT_mode) {
    // Blynk.virtualWrite(V0, Po);
    // Blynk.virtualWrite(V1, status);
    char* serverURL = "192.168.1.10:8000/ph";
    postPhToAPI(serverURL, Po, status);
  }

  lcd.clear();
}

void initWiFi(char* ssid, char* password) {

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println("WiFi Connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

char* determine_status(float pH_val) {
  if (pH_val >= 6.3 && pH_val <= 6.8) {
    return "Aman";
  } else {
    return "Tak Aman";
  }
}

void display_result(float pH_val, char* status) {
  lcd.setCursor(0, 0);
  lcd.printf("pH cairan: %.2f", pH_val);
  lcd.setCursor(0, 1);
  lcd.printf("Status: %s", status);
}

void postPhToAPI(char* url, float ph, char* status) {
  Serial.println("[INFO] Sending data to API...");
  Serial.println(url);
  Serial.println(ph);
  Serial.println(status);

  DynamicJsonDocument data(2048);
  data["ph"] = ph;
  data["result"] = status;
  String payload;
  serializeJson(data, payload);
  serializeJson(data, Serial);


  HTTPClient http;
  http.begin(url);
  // Set content type to JSON
  http.addHeader("Content-Type", "application/json");
  http.addHeader("accept", "application/json");
  http.setFollowRedirects(HTTPC_FORCE_FOLLOW_REDIRECTS);
  
  int responseCode = http.POST(payload);

  // int responseCode = http.POST(payload);
  if (responseCode >= 200 && responseCode < 300) {
    Serial.println("[SUCCESS] Data sent to the API");
    Serial.println(http.getString());
  } else {
    // If the request failed, print the error code
    Serial.println("Error on HTTP request: " + String(responseCode));
    Serial.println(http.getString());
  }

  http.end();
}

// float calculate_avg() {
//   int buffer_arr[10], temp;

//   // Store several analog val into an array
//   for (int i = 0; i < 10; i++) {
//     buffer_arr[i] = analogRead(A0);
//     delay(30);
//   }
//   for (int i = 0; i < 9; i++) {
//     for (int j = i + 1; j < 10; j++) {
//       if (buffer_arr[i] > buffer_arr[j]) {
//         temp = buffer_arr[i];
//         buffer_arr[i] = buffer_arr[j];
//         buffer_arr[j] = temp;
//       }
//     }
//   }
// }