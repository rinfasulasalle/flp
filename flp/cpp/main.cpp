#include <iostream>

using namespace std;


int main() {
    int c_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    cout << "array size: " << sizeof(c_array)/sizeof(c_array[0]) << endl;
    return 0;
}