#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Rus");
	link:
	srand(time(NULL));
	int n = rand() % 100;
	cout << "Приветствуем в нашей игре. Попробуйте угадть загаданное от 0 до 100 число\n";
	int b;
	for (int i = 0; i < 5; i++)
	{
		cin >> b;
		if (b == n) { cout << "Поздравляю! Вы угадали\n"; break; }
		if (i == 4) { cout << "Вы проиграли. Было загадано: " << n << '\n'; break; }
		if (b < n) cout << "Загаданное число больше\n";
		if (b > n) cout << "Загаданное число меньше\n";
	
	}
	int restart;
	cout << "Хотите начать сначала?(1 - ДА)\n";
	cin >> restart;
	if (restart == 1) goto link;
}