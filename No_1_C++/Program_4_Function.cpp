# include <iostream>
using namespace std;

int sum_of_n_nums(int);
int sum_of_n_odd_nums(int);
int sum_of_n_even_nums(int);

void greeting() {
    cout << "Hello I'm C++" << endl;
}

// || Recursion ||
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

int opeartion(int a, int b) {
    static int c = 0; // Static - This exicutes only once and the value of c will be retaind
    c += 1;
    return a * b + c;
}

float interest(int principal, float rate = 1.04) {  // Default Argument
    return principal * rate;
}

// void swaping(int * a, int * b) {    // Call by reference
//     int temp = * a;
//     * a = * b;
//     * b = temp;
// }
void swaping(int & a, int & b) {    // Call by reference using C++ Refrence
    const int temp = a; // const - cannot be changed
    a = b;
    b = temp;
}
int & swap(int & a, int & b) {    // Return by reference
    int temp = a;
    a = b;
    b = temp;
    return a;
}

int main() {
    int num, money;
    cout << "Enter the number:- ";
    cin >> num;

    money = 1000000;
    int total = sum_of_n_nums(num);
    int odd_total = sum_of_n_odd_nums(num);
    int even_total = sum_of_n_even_nums(num);
    cout << "Sum of all number till " << num << " is:- " << total << " All odd number is :- " << odd_total << " All even number is :- " << even_total << endl;
    swaping(odd_total, even_total);
    swap(odd_total, even_total);
    opeartion(odd_total, even_total);
    interest(money, 3);
    cout << "Factorial of the num is:- " << factorial(num) << endl;
    cout << "Sum of all number till " << num << " is:- " << total << " All odd number is :- " << odd_total << " All even number is :- " << even_total << endl;

    return 0;
}

inline int sum_of_n_nums(int n) {
    return (n * (n + 1)) / 2;
}

inline int sum_of_n_odd_nums(int n) {
    return n * n;
}

inline int sum_of_n_even_nums(int n) {
    return n * (n + 1);
}