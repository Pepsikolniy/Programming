#include<iostream>
using namespace std;	

int main()
{
	int n;
	cin >> n;
	string nomer_bileta;
	bool takoy_nomer_est = false;
	for (int i = 0; i < n; i++)
	{
		cin >> nomer_bileta;
		if (nomer_bileta.length() != 9) continue;
		if (nomer_bileta[0] == 'a' && nomer_bileta[4] == '5' && nomer_bileta[5] == '5' && nomer_bileta[6] == '6' && nomer_bileta[7] == '6' && nomer_bileta[8] == '1')
		{
			takoy_nomer_est = true;
			cout << nomer_bileta << ' ';
		}
	}
	if (takoy_nomer_est == false) cout << "-1";
}