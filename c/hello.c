#include <stdio.h>

long long int n;


int aaa(long long int k)
{
	long long int x_n;
	while(1){
		x_n =(x_n+k/x_n)/2;

		if((x_n*x_n<=k)&&((x_n+1)*(x_n+1)>k)){
		return x_n;
		}
	}
}
int main()
{
  scanf("%lld", &n);
  printf("%d", aaa(n));
  return 0;
}
