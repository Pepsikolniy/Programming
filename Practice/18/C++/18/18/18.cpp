#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{	
	char bukavki[26]{ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };
	double upavshiebukavki[26]{};
	vector<string>knownwords = {"hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"};
	double length = 0;
	for (int i = 0; i < knownwords.size(); i++)
	{
		for (int j = 0; j < knownwords[i].size(); j++)
		{
			length++;
			for (int q = 0; q < 26; q++)
				if (knownwords[i][j] == bukavki[q]) upavshiebukavki[q]++;
		}
	}
	string slovo;
	cin >> slovo;
	double veroyatnost = 1;
	for (int i = 0; i < slovo.size(); i++)
		for (int j = 0; j < 26; j++)
			if (slovo[i] == bukavki[j])
				veroyatnost *= upavshiebukavki[j] / length;
	cout.precision(16);
	cout << veroyatnost;
}