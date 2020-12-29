#include <iostream>
#include <vector>
#include <map>
#include <time.h>
#include "bozosort.h"
using namespace std;

struct Student {
    map<string, int> exams;
    string sName;
    int sgroup;
    Student(string Name, int group, int math, int phys, int hist, int prog) {
        exams = { {"mathematics", math},{"physics", phys},{"history", hist},{"programming", prog} };
        sName = Name;
        sgroup = group;
    }
    friend
        ostream& operator<< (ostream& print, const Student& student) {
        auto namelen = max(int(student.sName.length()), 4);
        auto del = string(namelen, '-');
        print << "+-" << del << "-+-------+------+------+------+------+\n"
            << "| Name" << string(namelen - 4, ' ')
            << " | Group | Math | Phys | Hist | Prog |\n"
            << "+-" << del << "-+-------+------+------+------+------+\n"
            << "| " << student.sName << " |   " << student.sgroup
            << "   |  " << student.exams.at("math")
            << "   |  " << student.exams.at("phys")
            << "   |  " << student.exams.at("hist")
            << "   |  " << student.exams.at("prog") << "   |\n"
            << "+-" << del << "-+-------+------+------+------+------+\n";
        return print;
    }
    bool operator > (const Student& Deb) {
        return sName > Deb.sName;
    }
    bool operator < (const Student& Deb) {
        return sName < Deb.sName;
    }
};
ostream& operator << (ostream& print, const vector<Student>& loxi) {
    auto namelen = loxi.at(0).sName.length();
    for (auto lox = loxi.begin() + 1; lox != loxi.end(); lox++) {
        if (lox->sName.length() > namelen) {
            namelen = lox->sName.length();
        }
    }
    auto del = string(namelen, '-');
    print << "+-" << del << "-+-------+------+------+------+------+\n"
        << "| Name" << string(namelen - 4, ' ')
        << " | Group | Math | Phys | Hist | Prog |\n"
        << "+-" << del << "-+-------+------+------+------+------+\n";
    for (auto student : loxi) {
        print << "| " << student.sName << string(namelen - student.sName.length(), ' ') << " |   " << student.sgroup
            << "   |  " << student.exams.at("math")
            << "   |  " << student.exams.at("phys")
            << "   |  " << student.exams.at("hist")
            << "   |  " << student.exams.at("prog")
            << "   |\n"
            << "+-" << del << "-+-------+------+------+------+------+\n";
    }
    return print;
}
int main() {
    srand(time(NULL));
    vector<Student> students = {
                                    Student("Suleymanov I",   1, 5, 5, 5, 2),
                                    Student("Ivanov I",       4, 2, 3, 3, 4),
                                    Student("Ghoul Z",        3, 2, 2, 2, 2),
                                    Student("Ghoul X",        9, 2, 2, 2, 2),
                                    Student("Ghoul C",        3, 2, 2, 2, 2),
                                    Student("Uzumaki N",      0, 4, 5, 4, 3),
                                    Student("Hatake K",       6, 3, 4, 3, 5),
                                    Student("Uchiha S",       0, 3, 3, 3, 3),
                                    Student("Supec S",        5, 4, 3, 3, 1),
                                    Student("Droog D",        4, 5, 2, 3, 3) 
                                };
    vector<Student> dvoeshniki;
    int kolvo = 0;
    for (auto lox : students) {
        for (auto exam : lox.exams) {
            if (exam.second == 2) {
                dvoeshniki.push_back(lox);
                kolvo += 1;
                break;
            }
        }
    }
    if (kolvo) {
        int ktoto = rand() % kolvo;
        cout << Bozosort(dvoeshniki);
        cout << "Explusion\n";
        cout << dvoeshniki[ktoto];
    }
    else {
        cout << "Not found\n";
    }
}