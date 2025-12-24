#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";
#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  String body = "{\"temperature\":" + String(temperature) +",\"humidity\":" + String(humidity) + ",\"location\":\"hall\"}";

  WiFiClient wifiClient;
  HTTPClient httpClient;

  httpClient.begin(wifiClient, "http://172.18.4.146:4000/temperature");
  httpClient.addHeader("Content-Type", "application/json");

  int status = httpClient.POST(body);

  Serial.print("HTTP Status Code: ");
  Serial.println(status);
  Serial.println(body);

  httpClient.end();
  delay(5000);
}
