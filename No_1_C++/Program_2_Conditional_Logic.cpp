# include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age:- ";
    cin >> age;

    // || Conditional Ladder ||
    if (age > 18 && age % 2 == 0) {
        cout << "You can Vote and your age is even!" << endl;
    }

    else if (age == 18 || age % 2 != 0) {
        cout << "Your age is 18 or your age is odd!" << endl;
    }
    
    else {
        cout << "You cannot vote" << endl;
    }

    // || Switch Case ||
    switch (age) {
    case 18:
        cout << "Your age is 18";
        break;

    case 12:
        cout << "Your age is 12";
        break;
    default:
        cout << "Sorry, age doesn't match";
        break;
    }

    return 0;
}