int cx, cy;
float segRaio;
float minRaio;
float horaRaio;
float diam;

void setup() {
  size(800, 500);
  stroke(255);
  
  int raio = min(width, height) / 2;
  segRaio = raio * 0.72;
  minRaio = raio * 0.60;
  horaRaio = raio * 0.50;
  diam = raio * 1.8;
  
  cx = width / 2;
  cy = height / 2;
}

void draw() {
  fill(0);
  ellipse(cx, cy, diam, diam);
  float s = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;
  float m = map(minute() + norm(second(), 0, 60), 0, 60, 0, TWO_PI) - HALF_PI; 
  float h = map(hour() + norm(minute(), 0, 60), 0, 24, 0, TWO_PI * 2) - HALF_PI;
  
  // ponteiros
  stroke(255); 
  strokeWeight(1);
  line(cx, cy, cx + cos(s) * segRaio, cy + sin(s) * segRaio);
  strokeWeight(2);
  line(cx, cy, cx + cos(m) * minRaio, cy + sin(m) * minRaio);
  strokeWeight(4);
  line(cx, cy, cx + cos(h) * horaRaio, cy + sin(h) * horaRaio);
  
  // movimentos
  beginShape(POINTS);
  for (int a = 0; a < 360; a+=6) {
    float angle = radians(a);
    float x = cx + cos(angle) * segRaio;
    float y = cy + sin(angle) * segRaio;
    if(a%30 == 0){
       strokeWeight(5);
       vertex(x, y);
    } else if(a%30 != 0){
      strokeWeight(1);
      vertex(x, y);
    }
  }
  endShape();
}
