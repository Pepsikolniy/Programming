#include <iostream>

int main(){

	setlocale(LC_ALL, "Russian");
	
	std::cout << "Результат выражения 2+2*2 = " << 2 + 2 * 2;



	int p = 3;
	int b = 3.14;

	double q = 3;
	double w = 3.14;

	std::cout << '\n' << '\n' << p << '\n' << b << '\n' << q << '\n' << w;


	int z = 2;
	int x = 3;
	double c = 2;
	double f = 3;

	std::cout << '\n' << '\n' << z + x << '\n' << z - x << '\n' << z * x << '\n' << z / x
		<< '\n' << '\n' << c + f << '\n' << c - f << '\n' << c * f << '\n' << c / f
		<< '\n' << '\n' << z + f << '\n' << z - f << '\n' << z * f << '\n' << z / f
		<< '\n' << '\n' << c + x << '\n' << c - x << '\n' << c * x << '\n' << c / x << '\n' << '\n';

	int e;
	int r;

	std::cin >> e >> r;

	std::swap(e, r);
	std::cout << '\n' << '\n' << e << '\n' << r;

	std::cin >> e >> r;
	int y;
	y = e;
	e = r;
	r = y;

	std::cout << '\n' << '\n' << e << '\n' << r << '\n' << '\n';

	
	double s, v, t, a;
	a = 9.8;
	std::cin >> v >> t;

	s = v * t + a * t * t / 2;

		std::cout << '\n' << '\n' << s;


	

}