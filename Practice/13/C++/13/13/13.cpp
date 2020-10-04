#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	int n;
	cin >> n;
	if (n < 2) exit(0);
	int i = 2;
	bool a = false;
	while (i < n)
	{
		if (n % i == 0) { a = true; break; }
		i++;
	}
	if (a == false) cout << "Простое";
	else cout << "Составное";
}