# include <iostream>
using namespace std; 

// Creating Template for Class
template <class custom = int> // Can be crated with multiple parameters or data types as well, By Default int is given
class vector {
    public:
        custom * arr;
        int size;
        vector(int m) {
            size = m;
            arr = new custom[size];
        }
        custom dotProduct(vector &v) {
            custom d = 0;
            for (int i = 0; i < size; i++) {
                d += this -> arr[i] * v.arr[i];
            }
            return d;
        }
        void showVector();
};
template <class t>
void vector <t> :: showVector() {
    cout << "This is Vector!" << endl;
}

// Creating Template for function
template <class any = int>
float average(any a, any b) {
    float avg;
    avg = (a + b) / 2.0;
    return avg;
}

int main() {
    
    // For Integer
    vector <int> v1(3);
    v1.arr[0] = 4;
    v1.arr[1] = 3;
    v1.arr[2] = 1;

    vector <int> v2(3);
    v2.arr[2] = 1;
    v2.arr[2] = 0;
    v2.arr[2] = 1;

    int pro = v1.dotProduct(v2);
    cout << "Dot product of vertor of intergers is:- " << pro << endl;
    
    // For Float
    vector <float> v3(3);
    v1.arr[0] = 4.5;
    v1.arr[1] = 3.3;
    v1.arr[2] = 1.5;

    vector <float> v4(3);
    v2.arr[2] = 1.8;
    v2.arr[2] = 0.9;
    v2.arr[2] = 1.1;

    float product = v1.dotProduct(v2);
    cout << "Dot product of vertor of floats is:- " << product << endl;

    // Using function Template
    int a = 31, b = 15, avg;
    avg = average(a, b);
    cout << "The average is:- " << avg << endl;

    return 0;
}