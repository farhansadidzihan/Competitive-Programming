# include <iostream>
# include <string>
# include <iomanip>
using namespace std;

int global = 3;

int main() {
    // || Typecsting ||
    int num = 245, global = 24;
    cout << (float)num / 34 << endl;
    cout << float(num) / 34 << endl;

    // || String Sclicing ||
    string name = "Zihan";
    cout << name.length() << " ";
    cout << name.substr(1, 5) << endl; // Len of String 

    cout << :: global << endl; // Scope Resolution Operator For Using Global Value

    // || Constant ||
    float const pi = 3.1416;
    // pi = 32434; // Throw an error=, because pi is constant
    cout << pi << endl;

    // || Manupulation Using <iomanip> ||
    int a = 432, b = 53, c = 8;
    cout << "The name is:- " << setw(3) << a << endl;
    cout << "The name is:- " << setw(3) << b << endl;
    cout << "The name is:- " << setw(3) << c << endl;

    return 0;
}