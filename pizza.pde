void setup() 
{
  size(800, 600);
}

void draw()
{
  pizza(500);
}

void pizza(float diametro)
{
  float angulo = 0;
  
  int[] data = {10, 20, 30, 40, 50, 60, 70, 80};
  
  int soma = 0;
  for(int i = 0; i < data.length; i++) 
  {
     soma = soma + data[i];
  }
  
  for (int i = 0; i < data.length; i++) {
    float cores = map(i, 0, data.length, 0, 255);
    fill(cores);
    arc(width/2, height/2, diametro, diametro, angulo, angulo+radians(data[i]));
    angulo += radians((data[i]*360)/soma);
  }
}
