# include <iostream>
using namespace std;

int main() {
    // || Array ||
    int arr[] = {1, 2, 3};
    
    int arr2d[3][3] = {{1, 2, 3}, 
                       {4, 5, 6},   // Creating 2d Array
                       {7, 8, 9}};

    for (int ind = 0; ind < 3; ind ++) {
        cout << arr[ind] << endl;
    } 

    
    // || Pointer ||
    int num = 10;
    int * address;
    address = & num; // Storing mamory location of num in address
    cout << "The value of num:- " << * address << endl;

    return 0;
}