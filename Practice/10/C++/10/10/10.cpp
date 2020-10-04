#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	long long s, l1, r1, l2, r2, x1, x2;
	cin >> s >> l1 >> r1 >> l2 >> r2;
	x1 = l1;
	x2 = l2;
	if (l1 > r1 || l2 > r2) exit(0);
	if (l1 + l2 > s) { cout << "-1"; exit(0); }
	if (r1 + r2 < s) { cout << "-1"; exit(0); }
link:
	if (x1 + x2 > s) { cout << "-1"; exit(0); }
	if (x1 + x2 == s) { cout << x1 << ' ' << x2; exit(0); }
	if (x1 + x2 < s && x2 == r2) { x1 += 1; goto link; }
	else if (x1 + x2 < s) { x2 += 1; goto link; }	
}