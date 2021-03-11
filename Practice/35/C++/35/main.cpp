#include <iostream>
using namespace std;

struct IntArray {
  int *data;
  int size;
};

void create(IntArray* arr, int size){
    arr->data = new int[size];
    arr->size = size;
}
void create(IntArray& arr, int size){
    arr.data = new int[size];
    arr.size = size;
}
  /** Возвращает элемент массива с индексом index, при этом проверяет выход за границы массива. Если index лежит за пределами массива, вывести сообщение об ошибке и прервать работу программы */
int get(IntArray* arr, int index){
    if (index < 0 || index > arr->size){
        cout << "Index out of range";
        return 0;
    }
    return arr->data[index];
}
int get(IntArray& arr, int index){
    if (index < 0 || index > arr.size){
        cout << "Index out of range";
        return 0;
    }
    return arr.data[index];
}
  /** Изменяет значение элемента массива с индексом index на значение параметра value, при этом проверяет выход за границы массива. Если index лежит за пределами массива, вывести сообщение об ошибке и прервать работу программы */
void set(IntArray* arr, int index, int value){
    if (index < 0 || index > arr->size){
        cout << "Index out of range";
        return;
    }
    arr->data[index] = value;
}
void set(IntArray& arr, int index, int value){
    if (index < 0 || index > arr.size){
        cout << "Index out of range";
        return;
    }
    arr.data[index] = value;
}
void print(IntArray* arr){
    cout << '[';
    for(int i = 0; i < arr->size; i++)
    {
        cout << arr->data[i];
        if(i != arr->size - 1)
            cout << ", ";
    }
    cout << ']';
}
void print(IntArray& arr){
    cout << '[';
    for(int i = 0; i < arr.size; i++)
    {
        cout << arr.data[i];
        if(i != arr.size - 1)
            cout << ", ";
    }
    cout << ']';
}
  /** Изменяет размер массива с сохранением элементов. Если новый размер меньше, хвостовые элементы обрезаются, если больше, то дополнительные элементы инициализируются нулём */
void resize(IntArray* arr, int newSize){
    int* array = new int[newSize];
    if (newSize > arr->size)
    {
        for(int i = 0; i < newSize; i++){
            if (i < arr->size)
                array[i] = arr->data[i];
            else
                array[i] = 0;
        }
    }
    else{
        for(int i = 0; i < newSize; i++)
            array[i] = arr->data[i];
    }
    delete [] arr->data;
    arr->data = array;
    arr->size = newSize;
}
void resize(IntArray& arr, int newSize){
    int* array = new int[newSize];
    if (newSize > arr.size)
    {
        for(int i = 0; i < newSize; i++){
            if (i < arr.size)
                array[i] = arr.data[i];
            else
                array[i] = 0;
        }
    }
    else{
        for(int i = 0; i < newSize; i++)
            array[i] = arr.data[i];
    }
    delete [] arr.data;
    arr.data = array;
    arr.size = newSize;
}

void destroy(IntArray* arr){
    delete [] arr->data;
    arr->data = nullptr;
    arr->size = 0;
}
void destroy(IntArray& arr){
    delete [] arr.data;
    arr.data = nullptr;
    arr.size = 0;
}
int main()
{
    IntArray arr;
    int size = 30;
    create(arr, size);
    for (int i = 0; i < size; i++)
        set(arr, i, i+1);
    print(arr);

    cout << endl << endl;
    resize(arr, 50);
    print(arr);

    cout << endl << endl;
    resize(arr, 10);
    print(arr);

    destroy(arr);

    return 0;
}
