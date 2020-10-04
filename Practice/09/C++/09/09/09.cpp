#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");

	int h1, m1, h2, m2;
	char znak;

	cin >> h1 >> znak >> m1;
	cin >> h2 >> znak >> m2;

	if (h1 > 23 || h1 < 0) exit(0);
	if (h2 > 23 || h2 < 0) exit(0);
	if (m1 > 59 || m1 < 0) exit(0);
	if (m2 > 59 || m2 < 0) exit(0);

	h1 = 60 * h1;
	m1 = h1;
	h2 = 60 * h2;
	m2 = h2;

	if (abs(m1 - m2) > 15) cout << "Встреча не состоится";
	if (abs(m1 - m2) < 16) cout << "Встреча состоится";
}