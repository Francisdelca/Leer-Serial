int v;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  v = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(v);
  v++;
  delay(1000);
}
