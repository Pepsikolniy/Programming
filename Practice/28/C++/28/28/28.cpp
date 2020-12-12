#include <iostream>
#include <map>
#include <string>
void print_factorization(unsigned int n) {
    std::map<unsigned int, unsigned int> delitel;
    const int min = 2;
    for (unsigned int i = 2; n == 0 or i <= n; i++) {
        if (n % i == 0) {
            n /= i;
            delitel[i]++;
            i = min;
        }
    }
    bool not_1 = false;
    for (const auto& elem : delitel) {
        std::cout << (not_1 ? "*" : (not_1 = true, "")) << elem.first;
        if (elem.second > 1) {
            std::cout << "^" << elem.second;
        }
    }
    std::cout << std::endl;
}
int main() {
    unsigned int x;
    std::cin >> x;
    print_factorization(x);
}