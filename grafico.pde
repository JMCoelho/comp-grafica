 float x0 = -TWO_PI;
 float xf = TWO_PI;
 float dx = 0.01;
 float yMax = 1.0;
 float yMin = -1.0;
 int margem = 10;
 
 void setup()
 {
   size(800, 600);
 }
 
 void draw()
 {
   line(margem, height/2, width - margem, height/2);
   line(width/2, 0, width/2, height);   
   
   //beginShape();
   for(float x = x0; x < xf; x += dx)
   {
     float xt = map(x, x0, xf, margem, width - margem);
     float yt = map(f(x), yMin, yMax, height - margem, margem);
     
     point(xt,yt);
   }
   //endShape();
 }
 
 float f(float x)
 {
    return cos(x);
 }
