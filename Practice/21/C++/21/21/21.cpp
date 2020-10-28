#include<iostream>
using namespace std;

double BMI(double weight, double height)
{
	return weight /pow(height, 2);
}
void printBMI(double BMI)
{
	if (BMI < 18.5)
		cout << "Underweight";
	else if (BMI >= 18.5 && BMI < 25.0)
		cout << "Normal";
	else if (BMI >= 25.0 && BMI < 30)
		cout << "Overweight";
	else if (BMI >= 30.0)
		cout << "Obesity";
}

int main()
{
	double weight, height;
	cin >> weight >> height;
	height /= 100;
	printBMI(BMI(weight, height));
}