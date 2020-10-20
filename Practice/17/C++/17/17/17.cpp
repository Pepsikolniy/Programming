#include<iostream>
using namespace std;

int main()
{
	int a[37]{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36};
	int k = 12;
	int chislo_vipalo[37];
	int chislo_vipalo_bolshe_vseh[37]{};
	int chislo_vipalo_bolshe = 0;
	int black[18]{ 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35};
	int red[18]{1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36};
	int n;
	int game = 0;
	bool restart = true;
	int sum_black = 0;
	int sum_red = 0;
	while (restart == true)
	{
		game++;
		cin >> n;
		if (n < 0 || n > 36)
		{
			restart = false;
			exit(0);
		}
		else
		{
			for (int i = 0; i < 37; i++)
			{
				if (a[i] == n) chislo_vipalo[i] = game;
			}
		}

		chislo_vipalo_bolshe_vseh[n] += 1;
		for (int i = 0; i < 37; i++)
		{
			if (chislo_vipalo_bolshe_vseh[i] > chislo_vipalo_bolshe)
				chislo_vipalo_bolshe = chislo_vipalo_bolshe_vseh[i];
		}
		for (int i = 0; i < 37; i++)
		{
			if (chislo_vipalo_bolshe_vseh[i] == chislo_vipalo_bolshe)
				cout << a[i] << ' ';
		}
		cout << endl;

		for (int i = 0; i < 19; i++)
		{
			if (n == black[i]) sum_black += 1;
			else if (n == red[i]) sum_red += 1;
		}

		for (int i = 0; i < 37; i++)
		{
			if (chislo_vipalo[i] == 0 || game - chislo_vipalo[i] >= k)
				cout << a[i] << ' ';
		}
		
		cout << endl;
		cout << sum_red << ' ' << sum_black << endl << endl;
	}
}