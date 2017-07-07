#include <stdio.h>
#include <math.h>
int main()
{
    int count, n = 1000000;
    double pi;
    float val = 0.0, p = 0.5;
    for(count = 1; count < n; ++count)
    {
      val += (pow((1.0-(((float)count/(float)n)*((float)count/(float)n))), p));
    }
    pi = (val + 1.0) * (2.0/(float)n);
    pi = pi*2;
    printf("%.11f", pi);
}
