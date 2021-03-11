#include <iostream>
using namespace std;

int* create(int length, int first_num = 0, int step = 0)
{
    int* arr = new int[length];
    for (int i = 0; i < length; i++) arr[i] = first_num + i*step;
    return arr;
}

int* sort(int* arr, int length)
{
    for (int i = 1; i < length; i++)
    {
        int temp = arr[i];
        for (int j = i - 1; j >= 0 && arr[j] > temp; j--)
        {
            arr[j + 1] = arr[j];
            arr[j] = temp;
        }
    }
    return arr;
}

int* print(int* arr, int length)
{
    cout << '[';
    for (int i = 0; i < length-1; i++)
    {
        cout << arr[i] << ", ";
    }
    cout << arr[length-1] << ']';
    return arr;
}
int main()
{
    int length, first_num, step;
    cin >> length >> first_num >> step;
    int* arr;
    arr = create(length, first_num, step);
    sort(arr, length);
    print(arr, length);
    delete [] arr;
    arr = nullptr;
    return 0;
}
