#include <iostream>
using namespace std;

int main()
{
	double x0, v0, t, g;
	g = 9.8;
	cin >> x0 >> v0 >> t;
	if (t < 0) exit(0);
	if (v0 < 0) exit(0);
	int xt = x0 + v0 * t - g * t * t / 2;
	cout << abs(xt - x0);

}