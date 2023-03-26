# include <iostream>
using namespace std;

class Employee {
        public:
            string name;
            int salary;

        Employee(string n, int s) {
            this -> name = n;
            this -> salary = s;
        }
        
        void printDetails() {
            cout << "The name of the empoyee is:- " << this -> name << " and his salary is:- " << this -> salary << "$"; 
        }
};

class Programmer : public Employee {
    public:
        int null;
};
    
int main() {
    Employee FSZ("Zihan", 1000);
    FSZ.printDetails();

    return 0;
}