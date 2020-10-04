#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	double a, b;
	char znak;

	cin >> a >> znak >> b;
	switch (znak)
	{
	case '+': cout << a + b; break;
	case '-': cout << a - b; break;
	case '*': cout << a * b; break;
	case '/': cout << a / b; break;

	}
}	