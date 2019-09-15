#include<iostream>
#include<string>
//Calculate Fahrenheit to celsius
int main(int argc, char* argv[], char* envp[]) {
    double celsius = std::stod(argv[1]);
    double cToF = celsius * 1.8 + 32;
    double cToK = celsius + 273.15;
    std::cout << '\n' << celsius << "°C to Fahrenheit is " << cToF << "°F\n";
    std::cout << celsius << "°C to Kelvin is " << cToK << "°K\n\n";

    double fahrenheit = std::stod(argv[2]);
    double fToC = (fahrenheit - 32) * 5 / 9;
    double fToK = fToC + 273.15;
    std::cout << fahrenheit << "°F to Celsius is " << fToC << "°C\n";
    std::cout << fahrenheit << "°F to Kelvin is " << fToK << "°K\n\n";

    double kelvin = std::stod(argv[3]);
    double kToC = kelvin - 273.15;
    double kToF = kToC * 1.8 + 32;
    std::cout << kelvin << "°K to Celsius is " << kToC << "°C\n";
    std::cout << kelvin << "°K to Fahrenheit is " << kToF << "°F\n\n";

}
