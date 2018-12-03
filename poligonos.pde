void setup() 
{
  size(800, 600);
}

float x = width/8;
float y = height/8;
float raio = 0.5 * width;
void draw()
{
  desenhaPoligono(3);
}

void keyPressed() 
{
  int value = (int)key;
  if (value > 50) 
  {
    int numeroDePontos = value - 48;
    desenhaPoligono(numeroDePontos);
  } 
}
void desenhaPoligono(int numeroDePontos) 
{
  float angulacao = TWO_PI / numeroDePontos;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angulacao) 
  {
    float nx = x + cos(a) * raio;
    float ny = y + sin(a) * raio;
    vertex(nx, ny);
  }
  endShape(CLOSE);
}
