#include <iostream>

using namespace std;

int main(){
    double u[10001];
    double t[10001];
    double a = 4.3;
    u[0] = 15.7;
    t[0] = 0;
    float step = 0.001;
    for (int i = 1; i<10001; i++){
        u[i] = (1-a*step)*u[i-1];
        t[i] = i*step;
    }
    cout << "u[0], t[0]:" << u[0] << " " << t[0] << endl;
    cout << "u[100011], t[10001]:" << u[10000] << " " << t[10000] << endl;
    return 0;
}
