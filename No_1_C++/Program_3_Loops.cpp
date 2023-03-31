# include <iostream>
using namespace std;

int main() {
    int ind = 0;
    
    // || While Loop ||
    while (ind <= 10) {
        cout << "Index is " << ind << endl;
        ind ++;
    }

    // || Do While Loop ||
    do {
        cout << "Index is " << ind << endl;
        // ind ++;
    } while (ind > 1);
    
    // || For Loop ||
    for (int num = 1; num < 10; num ++) {
        cout << "num is " << num << endl;
    }

    // || Multipication Table ||
    

    return 0;
}