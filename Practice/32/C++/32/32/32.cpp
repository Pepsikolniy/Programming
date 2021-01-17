#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<iomanip>
using namespace std;

struct Passenger {
    unsigned int PassengerId;
    bool Survived;
    unsigned int Pclass;
    string Name;
    string Sex;
    double Age;
    unsigned int SibSp;
    unsigned int Parch;
    string Ticket;
    double Fare;
    string Cabin;
    string Embarked;
}mine;

void sorting(vector<Passenger*>& woman) {
    for (int i = 0; i < woman.size() - 1; i++) {
        for (int j = i; j < woman.size(); j++) {
            if (woman[i]->Age > woman[j]->Age) {
                swap(*woman[i], *woman[j]);
            }
        }
    }
}

vector<Passenger*> people(vector<Passenger>& passengers) {
    vector<Passenger*> woman;

    for (int i = 0; i < passengers.size(); i++) {
        if (passengers[i].Survived = true and passengers[i].Sex == "female" and passengers[i].Pclass == 1) {
            woman.push_back(&passengers[i]);
        }
    }
    sorting(woman);
    return woman;
}

istream& operator >> (istream& file, vector<Passenger>& passengers) {



    string str_file;


    bool check = false;

    while (!file.eof()) {

        str_file = "";
        if (!check) {
            getline(file, str_file, '\r');
            check = true;
        }
        getline(file, str_file, ',');          
        unsigned int passengerId = stoi(str_file);
        mine.PassengerId = passengerId;

        getline(file, str_file, ',');
        bool survived = stoi(str_file);
        mine.Survived = survived;

        getline(file, str_file, ','); 
        unsigned int pclass = stoi(str_file);
        mine.Pclass = pclass;

        getline(file, str_file, ',');
        string name = str_file;
        if (name[name.length() - 1] != '"')
        {
            getline(file, str_file, ',');
            name += str_file;
        }
        
        name.erase(0, 1);                    
        name.erase(name.size() - 1, 1);
        mine.Name = name;

        getline(file, str_file, ',');
        mine.Sex = str_file;

        getline(file, str_file, ',');
        if (str_file == "") {
            str_file = "0";
        }
        double age = stoi(str_file);
        mine.Age = age;

        getline(file, str_file, ',');
        unsigned int sibSp = stoi(str_file);
        mine.SibSp = sibSp;

        getline(file, str_file, ',');
        unsigned int parch = stoi(str_file);
        mine.Parch = parch;

        getline(file, str_file, ',');
        mine.Ticket = str_file;

        getline(file, str_file, ',');
        double fare = stoi(str_file);
        mine.Fare = fare;

        getline(file, str_file, ',');
        if (str_file == "") {
            str_file = "";
        }
        mine.Cabin = str_file;

        getline(file, str_file, '\r');
        mine.Embarked = str_file;
        cout << str_file << endl;
        passengers.push_back(mine);

    }
    return file;
}

ostream& operator<< (ostream& out, vector<Passenger>& passengers) {
    out << "PassengerId\t" << "Survived\t" << "Pclass\t" << "Name\t" << "Sex\t" << "Age\t" << "SibSp\t" << "Parch\t" << "Ticket\t" << "Fare\t" << "Cabin\t" << "Embarked";
    out << endl;

    for (int i = 0; i < passengers.size(); i++) {
        Passenger& p = passengers[i];
        out << p.PassengerId << "\t" << p.Survived << "\t" << p.Pclass << "\t" << p.Name << "\t" << p.Sex << "\t" << p.Age << "\t" << p.SibSp << "\t" << p.Parch << "\t" << p.Ticket << "\t" << p.Fare << "\t" << p.Cabin << "\t" << p.Embarked << endl;
    }

    return out;
}

int main() {

    ifstream file;
    file.open("train.csv");
    vector<Passenger> passengers;
    file >> passengers;
    people(passengers);

    ofstream who_live;
    who_live.open("live.csv");
    who_live << passengers;
}