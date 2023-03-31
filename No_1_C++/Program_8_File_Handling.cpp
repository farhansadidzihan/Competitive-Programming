# include <iostream>
# include <fstream> // module for file handling
using namespace std; 

int main() {
    string str1 = "C++ is a high-level programming language that was developed in the early 1980s by Bjarne Stroustrup as an extension of the C programming language.";
    string str2;
    // Opening File Using Constructor and writing it
    ofstream out("cpp.txt");  // Writing Operation, instead of "out" we can use any object
    out << str1;
    out.close();

    // Opening File Using open() and writing it
    ofstream out;
    out.open("cpp.txt");
    out << "C++ is a high-level programming language that was developed in the early 1980s by Bjarne Stroustrup as an extension of the C programming language.";
    out.close();

    // Opening File Using Constructor and Reading it
    ifstream in("cpp.txt");  // Reading Operation, instead of "in" we can use any object
    // in >> str2;  // Gives the string before any space or tab  
    getline(in, str2);  // Gives the whole line
    cout << str2 << endl;

    // Opening File Using open() and Reading it
    ifstream in;
    in.open("cpp.txt");
    while (in.eof() == 0) {
        getline(in, str2);
        cout << str2 << endl;
    }
    in.close();

    return 0;
}