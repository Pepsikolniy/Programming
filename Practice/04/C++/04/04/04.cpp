#include <iostream>
using namespace std;

int main()
{	
	setlocale(LC_ALL, "Rus");
{
	double a, b, c;
	cout << "Введите значение переменной a: ";
	cin >> a;
	cout << "Введите значение переменной b: ";
	cin >> b;
	c = a;
	a = b;
	b = c;
	cout << a << endl << b << endl;
}
{
	double a, b;
	cout << "Введите значение переменной a: ";
	cin >> a;
	cout << "Введите значение переменной b: ";
	cin >> b;
	swap(a, b);
	cout << a << endl << b;
}
}