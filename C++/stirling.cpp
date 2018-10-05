#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

double stirling (int n) {
    return  n*log(n)-n;
}

int main(){
    vector<int> vals{2,5,10,50,100,1000};
    for (int x: vals){
        cout << "approx x=" << stirling(x) << "  True x:" << lgamma(x+1) << endl;
    }
    return 1;
}
