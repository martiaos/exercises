#include <iostream>
using namespace std;
#include <vector>

int triangle (int n){
    int sum = 0;
    for (int i =0; i<n+1; i++){
            sum = sum + i;
    }
    return sum;
}


//int true_triangle (int n){
//    return n*(n+1)/2;
//
//}

int main(){
    int n;

    cout << "Please enter a number: ";
    cin >> n;
    cout << "Triangle(" << n << "):  " << triangle(n) << endl;
    // cout << "True Triangle:" << true_triangle(n) << endl;

    return 0;
}
