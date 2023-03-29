# include <iostream>
# include <vector>  // STL - Container - Sequence Container - Vector
# include <list>  // STL - Container - Sequence Container - List
# include <map>  // STL - Container - Assosiative Container - Map
# include <algorithm>  // STL - Algorithms
# include <functional>  // Functional Object or Functor
# include <string>
using namespace std; 

void display(vector <int> &v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
}

int main() {
    // || Vector ||
    vector <int> vec1;
    int element;
    for (int i = 0; i < 4; i++) {
        cout << "Enter a number:- ";
        cin >> element;
        vec1.push_back(element);  // push_back method in vector
    }
    vec1.pop_back();  // pop_back method in vector
    display(vec1);
    vector <int> :: iterator iter1 = vec1.begin();  // Iterator
    vec1.insert(iter1, 343);  // Inserting element in vector
    display(vec1);

    // || List ||
    list <int> list1;
    list <int> list2;
    // List 1
    list1.push_back(5);  // push_back method in list
    list1.push_back(8);
    list1.push_back(6);
    list1.push_back(19);
    list1.push_front(6);  // push_front method in list
    list <int> :: iterator iter2;
    iter2 = list1.begin();
    cout << * iter2 << " "; 
    iter2 ++;
    cout << * iter2 << " "; 
    iter2 ++;
    cout << * iter2 << " "; 
    iter2 ++;
    list1.pop_back();  // pop_back method in list
    list1.pop_front();  // pop_front method in list
    list1.remove(5);  // removes given element from list
    list1.sort();  // Sorts the list
    // List 2
    list2.push_back(5);  // push_back method in list
    list2.push_back(8);
    list2.push_back(6);
    list2.push_back(19);
    list1.merge(list2);  // merges two list

    // || Map ||
    map <string, int> marks;
    marks["Zihan"] = 100;
    marks["Aman"] = 100;
    marks["Harry"] = 100;
    marks["Babbar"] = 100;
    marks["Sandeep"] = 100;
    map <string, int> :: iterator iter;
    for (iter = marks.begin(); iter != marks.end(); iter++) {
        cout << (* iter).first << " " << (* iter).second << endl;
    }
    cout << marks.size() << endl;  // Returns length of the map
    cout << marks.max_size() << endl; // Returns max size of the map
    cout << marks.empty() << endl;  // Return empty or not

    // || Function Object ||
    int arr[] = {1, 23, 4, 34, 32, 2, 3, 4, 5, 5, 6, 7};
    sort(arr, arr + 7, greater <int> ());  // Sorts the array, "greater <int> ()" - used for descending order
    for (int i = 0; i < 7; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}