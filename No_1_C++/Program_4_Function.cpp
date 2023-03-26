# include <iostream>
using namespace std;

int sum_of_n_nums(int n) {
    return (n * (n + 1)) / 2;
}

int sum_of_n_odd_nums(int n) {
    return n * n;
}

int sum_of_n_even_nums(int n) {
    return n * (n + 1);
}

int main() {

    int num;
    cout << "Enter the number:- ";
    cin >> num;

    int total = sum_of_n_nums(num);
    int odd_total = sum_of_n_odd_nums(num);
    int even_total = sum_of_n_even_nums(num);
    cout << "Sum of all number till " << num << " is:- " << total << " All odd number is :- " << odd_total << " All even number is :- " << even_total << endl;

    return 0;
}