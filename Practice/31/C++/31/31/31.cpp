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
/*Вопрос 2.
    Нет, потому что вектор будет перемещён в новую память. Также его размер в памяти будет больше, т.к. больше элементов.*/
/*Вопрос 3.
    Такой же ответ, как и в первом вопросе.*/
/*Вопрос 4.
     Изменения есть. Когда мы используем pop_back() для вектора, который мы передали по значению уменьшается длина вектора, но не объём
     используемой памяти, поэтому, новое место в памяти не выделяется, а первый элемент остаётся с прежним адресом*/