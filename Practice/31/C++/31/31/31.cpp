#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

/*ofstream& operator<< (ofstream& out, const vector<int>& vector){
    out << vector.size() << "\t| ";
    for (auto& elem : vector) out << &elem << " ";
    out << "\n";
    return out;
}*/
ofstream& operator<< (ofstream& out, const vector<int> vector){
    out << vector.size() << "\t| ";
    for (auto& elem : vector) out << &elem << " ";
    out << "\n";
    return out;
}
int main() {
    vector<int> vector;
    ofstream txt;
    txt.open("data_without_ref.txt");
    for (int i = 0; i < 64; i++)
    {
        vector.push_back(i);
        txt << vector;
    }
    for (int i = 0; i < 64; i++)
    {
        vector.pop_back();
        txt << vector;
    }
}
/* Вопрос 1.
    Адрес первого элемента вектора всегда разный, т.к. оператор << использует случайные адреса в памяти и вектор копируется в новую.
    Следующие элементы идут в памяти упорядоченно, адрес следующего элемента + 4(sizeof(int) = 4)*/