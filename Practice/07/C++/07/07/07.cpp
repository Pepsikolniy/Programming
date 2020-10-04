#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	double a, b, c;
	int x1, y1;
	int x2, y2;
	int x3, y3;
	int choose;

	cin >> choose;
	if (abs(choose) > 1000) exit(0);
	switch (choose)
	{
	case 1: { cin >> a; cin >> b; cin >> c;
		if (a + b < c) exit(0);
		if (a + c < b) exit(0);
		if (b + c < a) exit(0);
		int p = (a + b + c) / 2;
		cout << "S = " << sqrt(p * (p - a) * (p - b) * (p - c));
		break;
	}
	case 2: { cin >> x1 >> y1; cin >> x2 >> y2; cin >> x3 >> y3; 
		double AB, BC, AC;
		AB = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
		BC = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
		AC = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
		if (AB + BC < AC) exit(0);
		if (AB + AC < BC) exit(0);
		if (BC + AC < AB) exit(0);
		cout << "S = " << abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2;
		break; }
	default: break;
    }


}