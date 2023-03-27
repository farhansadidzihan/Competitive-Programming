# include <iostream>
using namespace std;

int main() {
    // || Array ||
    int nums[] = {1, 2, 3};

    int arr2d[3][3] = {{1, 2, 3}, 
                       {4, 5, 6},   // Creating 2d Array
                       {7, 8, 9}};

    // for (int ind = 0; ind < 3; ind ++) {
    //     cout << arr[ind] << endl;
    // } 

    
    // || Pointer ||
    int num = 10;
    int * address = & num; // Storing mamory location of num in address
    int ** pointer_address = & address; // Pointer to pointer
    // cout << "The value of num:- " << * address << endl;
    // cout << "The value of num:- " << * pointer_address << endl;

    int * p = nums; // Pointer in Array
    cout << * p << endl;
    cout << * (p++) << endl; // Pointer Arithmetic
    cout << * (p++) << endl;
    cout << * (p++) << endl;

    // User Defined Data Structures
    struct Employee {   // struct data structure
        int salary, id;
    };
    // typedef struct Employee {   // Onother way
    //     int id, salary; 
    // } ep;
    union Money {   // Union data structure, it's very memory efficient
        int net_worth, car, jet; // Uses the maximum bytes of variable at a time
    };

    enum Meal {breakfast, lunch, dinner}; // Set index for that word

    struct Employee Zihan;    
    Zihan.id = 12345;
    Zihan.salary = 12000;
    union Money man;
    man.net_worth = 2000000000;
    man.car = 24442323;
    man.jet = 5000000;
    Meal today = dinner;
    cout << Zihan.id << endl;
    cout << man.net_worth << endl;
    cout << today << endl;

    return 0;
}