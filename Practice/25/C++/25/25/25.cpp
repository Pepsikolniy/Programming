#include <iostream>
#include <vector>
#include <ctime>
#include <random>
using namespace std;

void print(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n";
}
bool is_sorted(vector<int> arr, bool sorted = true) {
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
vector<int> BozoSort(vector<int> arr, bool sorted = true)
{
    vector<int> result = arr;
    int rand1;
    int rand2;
    while(is_sorted(result, sorted) == false)
    {
        rand1 = rand() % arr.size();
        rand2 = rand() % arr.size();
        swap(result[rand1], result[rand2]);
    }
    return result;
}
vector<int> BozoSort(vector<vector<int>> arr, bool sorted = true)
{
    vector<int> result;
    for (vector<int> vec : arr) {
        for (int elem : vec) {
            result.push_back(elem);
        }
    }
    return BozoSort(result, sorted);
}
vector<int> BozoSort(int a1, int a2, int a3, bool sorted = true) {
    vector<int> result{ a1, a2, a3 };
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