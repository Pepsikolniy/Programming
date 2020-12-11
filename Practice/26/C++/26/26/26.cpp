#include <iostream>
#include <vector>
#include <ctime>
#include <random>
using namespace std;

template<typename T>
void print(vector<T> arr) {
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n";
}
template<typename T>
bool is_sorted(vector<T> arr, bool sorted = true) {
    if (sorted)
    {
        for (int i = 0; i < arr.size() - 1; i++)
        {
            if (arr[i] > arr[i + 1])
                return false;
        }
    }
    else
    {
        for (int i = 0; i < arr.size() - 1; i++)
        {
            if (arr[i] < arr[i + 1])
                return false;
        }
    }
    return true;
}
template<typename T>
vector<T> BozoSort(vector<T> arr, bool sorted = true)
{
    vector<T> result = arr;
    int rand1;
    int rand2;
    while (is_sorted(result, sorted) == false)
    {
        rand1 = rand() % arr.size();
        rand2 = rand() % arr.size();
        swap(result[rand1], result[rand2]);
    }
    return result;
}
template<typename T>
vector<T> BozoSort(vector<vector<T>> arr, bool sorted = true)
{
    vector<T> result;
    for (vector<T> vec : arr) {
        for (T elem : vec) {
            result.push_back(elem);
        }
    }
    return BozoSort(result, sorted);
}
template<typename T>
vector<T> BozoSort(T a1, T a2, T a3, bool sorted = true) {
    vector<T> result{ a1, a2, a3 };
    return BozoSort(result, sorted);
}
int main()
{
    srand(time(NULL));
    int n;
    cin >> n;
    vector<int> input;
    vector<int> stroka;
    vector<vector<int>> matrica;
    for (int i = 1; i < n + 1; i++)
    {
        int num;
        cin >> num;
        stroka.push_back(num);
        input.push_back(num);
        if (i % int(sqrt(n)) == 0) {
            matrica.push_back(stroka);
            stroka.clear();
        }
    }
    print(BozoSort(input));
    print(BozoSort(input, false));
    print(BozoSort(matrica));
    print(BozoSort(matrica, false));
    print(BozoSort(input[0], input[1], input[2]));
    print(BozoSort(input[0], input[1], input[2], false));
}