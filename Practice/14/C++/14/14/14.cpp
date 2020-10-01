#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	long long n;
	cin >> n;
	if (n < 0) exit(0);
	if (n == 0) { cout << 0; exit(0); }
	int sum = 0;
	int x = 1;
	double Log;
	while(x <= n)
	{
		Log = log2(x);
		if (Log == int(Log)) sum++;
		x++;
	}
	cout << sum;
}