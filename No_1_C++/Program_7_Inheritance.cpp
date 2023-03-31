# include <iostream>
using namespace std;

class A {
        public:
            string name;
            int salary;

            A(string n, int s) {
                this -> name = n;
                this -> salary = s;
            }
            
            void printDetails() {
                cout << "The name of the person is:- " << this -> name << " and his salary is:- " << this -> salary << "$"; 
            }
};
// Single Inheritance A -> B
class B : public A {
    public:
        int null;
};
// Multiple Inheritance A -> B, C
class C : protected A, public B {
    private:
        int num;
};
// Multilevel Inheritance A -> B -> D
class D : virtual private B {  // Virtual Base Class
    protected:
        int number;
};

    
int main() {
    A num("Number", 1000);
    num.printDetails();

    return 0;
}