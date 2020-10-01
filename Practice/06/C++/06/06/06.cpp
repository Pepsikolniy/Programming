#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	double a, b, c, D;
	cout << "Введите параметры a, b, c для квадратного уравнения: " << endl;
	cin >> a >> b >> c;
	if (a, b, c == 0) { cout << "Все корни верны :)"; exit(0); }
	if (b, c == 0) { cout << "x = 0"; exit(0); }
	if (a, b == 0) { cout << "Уравнение не имеет смысла"; exit(0); }
	if (a, c == 0) { cout << "x = 0"; exit(0); }
	if (a == 0) { cout << "x = " << -c / b; exit(0); }
	if (b == 0 && a > 0) { cout << "Вещественных корней не существует"; exit(0); }
	else if (b == 0 && a < 0) { cout << "x1 = " << sqrt(-c / a) << endl << "x2 = " << -sqrt(-c / a); exit(0); }
	if (c == 0) { cout << "x1 = 0" << endl << "x2 = " << -b / a; exit(0); }
	D = pow(b, 2) - 4 * a * c;
	if (D > 0) { cout << "x1 = " << (-1*b + sqrt(D)) / (2 * a) << endl
			     << "x2 = " << (-1*b - sqrt(D)) / (2 * a); }
	else if (D < 0) 
		         cout << "Уравнение не имеет вещественных корней";
	else 
		         cout << "x = " << -b / (2 * a);
	
}