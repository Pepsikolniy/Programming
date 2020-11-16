#include<iostream>
#include<fstream>
#include"json.hpp"
#include<iomanip>

using json = nlohmann::json;

int main()
{
	std::ifstream input("in.json");
	std::ofstream output("out.json");

	json jin;
	input >> jin;
	
	json jout;

	????
	????
	????
	????
	????

	output << std::setw(2) << jout << std::endl;
}