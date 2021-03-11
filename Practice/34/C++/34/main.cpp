#include <iostream>
using namespace std;

void create(int **arr,int length, int first_num = 0, int step = 0)
{
    *arr = new int[length];
    for (int i = 0; i < length; i++) (*arr)[i] = first_num + i*step;
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
void destroy(int *&arr)
{
    delete [] arr;
    arr = nullptr;
}
int main()
{
    int length, first_num, step;
    cin >> length >> first_num >> step;
    int* arr;
    create(&arr, length, first_num, step);
    sort(arr, length);
    print(arr, length);
    destroy(arr);
    return 0;
}
