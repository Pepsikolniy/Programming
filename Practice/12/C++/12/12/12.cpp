#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	int n, x, i;
	x = 1;
	i = 1;
	cout << "¬ведите факториал целого положительного числа: ";
	cin >> n;
	if (n < 1) exit(0);
	while (i <= n)
	{
		x = x * i;
		i++;
	}
	cout << n << "! = " << x;



}