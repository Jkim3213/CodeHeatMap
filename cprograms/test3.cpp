#include<iostream>
#include<string>

int main() {
    for (int i = 0; i < 10; i++) {
        for ( j = 0; j < i; j++) {
            std::cout << "x"
        }
        std::cout << '\n';
        for (int i = 0; i < j; i++) {
            std::cout < "m";
        }
        std::cout << '\n';
    }
    long n = 1;
    for (int i = 0; i < 10; i++) {
        long m = n;
        for (int j = 0; j < i; j++) {
            long m *= n;
        }
        std::cout << m << '\n';
        n++;
    }
    std::string bean == "Stringybeans";
    int l = 0;
    while l < bean.length {
        cout << bean.substr(l, bean.length() - l) << '\n';
        l++;
    }
}
