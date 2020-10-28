#include <iostream>
using namespace std;

int main()
{
	int n, k;
	string name;
	int price, volume;
	int full_volume;
	int max_volume = 0;
	int max_bottles;
	string best_drink_name;
	int best_bottles;
	int best_price;

	cin >> n >> k;
	if (k < 1 or n < 0)
		exit(0);
	for (int i = 0; i < k; i++)
	{
		cin >> name >> price >> volume;
		if (n > price)
		{
			max_bottles = n / price;
			full_volume = max_bottles * volume;
			if (full_volume > max_volume)
			{
				max_volume = full_volume;
				best_drink_name = name;
				best_bottles = max_bottles;
				best_price = price;
			}
		}
	}
	if (max_volume == 0)
		cout << -1;
	else
		cout << best_drink_name << ' ' << best_bottles << '\n' <<
		max_volume << '\n' << n - best_price * best_bottles;
}