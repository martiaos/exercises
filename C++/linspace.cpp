#include <iostream>
#include <vector>

using namespace std;

vector<double> linspace(double a, double b){
    double step = (b-a)/49;
    vector<double> space;
    for (int i = 0; i < 50; i++){
        space.push_back(a + i*step);
        }
    return space;
}

vector<double> linspace(double a, double b, int n){
    double step = (b-a)/(n-1);
    vector<double> space;
    for (int i = 0; i < n; i++){
        space.push_back(a + i*step);
        }
    return space;
}


int main(){
    double a = 10.0;
    double b = 20.0;
    int n = 100;
    vector<double> space = linspace(a, b);
    for (int i = 0; i < 50; i++){
        cout << "Space[" << i <<"]:  " << space[i] << endl;
    }

    vector<double> space2 = linspace(a, b, n);
    for (int i = 0; i < n; i++){
        cout << "Space[" << i <<"]:  " << space2[i] << endl;
    }
    return 0;
}
