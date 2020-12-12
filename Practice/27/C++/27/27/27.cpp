#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
#define print(N) cout<<N;
#define println(N) cout<<N<<endl;
void printl(vector<int> mass, int max, int couner) {
    for (couner; couner < max; couner++) {
        cout << mass[couner] << " ";
    }
}
bool is_sorted(vector<int> mass, bool des = true) {
    int size = mass.size();;
    if (des) {
        for (int i = 0; i < size - 1; i++)
        {
            if (mass[i] < mass[i + 1]) return false;
        }
    }
    return true;
}
vector<int> Bozosort(vector<int> mass, int max, bool des = true) {
    vector<int> result = mass;
    while (is_sorted(result, des) == false) {
        for (int i = 0; i < max; i++) {
            int k = std::rand() % max;
            int j = std::rand() % max;
            swap(result[k], result[j]);
        }
    }
    return result;
}
int main() {
    int n, max = 0, counter;
    println("Enter the integer n that will be the len of vector");
    cin >> n;
    vector<int> vec;
    vector<int> vec1;
    println("Enter the numbers of vector");
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        vec.push_back(a);
        max++;
        if (max <= 5) {
            vec1 = Bozosort(vec, max);
            printl(vec1, max, counter = 0);
        }
        else {
            counter = max - 5;
            vec1 = Bozosort(vec, max);
            printl(vec1, max, counter);
        }

    }
}