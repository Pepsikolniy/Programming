#include <iostream>
using namespace std;

int main()
{
	double x0, v0, t, g;
	g = 9.8;
	cin >> x0 >> v0 >> t;
	if (t < 0) exit(0);
	if (v0 < 0) exit(0);
	cout <<x0 + v0 * t + g * t * t / 2;

}