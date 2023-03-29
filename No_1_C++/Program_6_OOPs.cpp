# include <iostream>
# include <string>
using namespace std;

class Employee {
        public:
            string name;
            int salary;
            // Constractor
            Employee(void) {  // Default Constractor
                name = "Zihan";
                salary = 10000;
            }
            // Destractor
            ~Employee() {
                cout << "Destractor Called!" << endl;
            }
            static int count; // Static Data Member, By default = 0
            Employee(string n, int s) {
                this -> name = n;
                this -> salary = s;
            }            
            void details();
        private:
            void printDetails() {
                cout << "The name of the empoyee is:- " << this -> name << " and his salary is:- " << this -> salary << "$"; 
            }
};
int Employee :: count = 1000; // changed into 1000
void Employee :: details() {
    cout << "You cannot see deails!" << endl;
}

class Binary {  // By default all members of class are privet
    public:
        string s;
        Binary (string str) {
            this -> s = str;
        }
        void read(void); // Void - means no parameter
        void chk_bin(); // In C++ Void is not mandetory
};
void Binary :: read() {
    cout << "To check it's Binary or not, call chk_bin() function!" << endl;
}
void Binary :: chk_bin() {
    read();
    for (int i = 0; i < s.length(); i++) {
        if (s.at(i) != '0' && s.at(i) != '1') {
            cout << "It's not Binary" << endl;
            exit(0);
        }
    }
}

class Shop {
    public:
        int itemsID[50];
        int itemsPrice[50];
        int counter;
        void initCounter() {
            counter = 0;
        }
        void setPrice();
        void showPrice();
};
void Shop :: setPrice() {
    cout << "Enter Product ID:- " << endl;
    cin >> itemsID[counter];
    cout << "Enter Price ID:- " << endl;
    cin >> itemsPrice[counter];
    counter ++;
}
void Shop :: showPrice() {
    for (int i = 0; i < counter; i++) {
        cout << "The price of the product is:- " << itemsPrice[counter] << endl;
    }
}

int main() {
    Employee FSZ("Zihan", 1000);
    // FSZ.details();
    Binary num("010210");
    // num.chk_bin();
    Shop Shoe_Store;
    // Shoe_Store.setPrice();
    // Shoe_Store.showPrice();

    return 0;
}