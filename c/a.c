#include <stdio.h>

int main(void)
{
	int n=1;
	while(n!=0)
	{
		scanf("%d", &n);
		if(n%2==0)
			continue;
		if(n!=0) printf("%d\n", n);
	}
}