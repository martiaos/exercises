#include <iostream>
using namespace std;

void reduction_by_halves (int n) {
    while (n>0){
        n = n/2;
        cout << "n=" << n << endl;
    }
}

int main() {

    int n = 1000;
    reduction_by_halves(n);

    return 0;
}
