
#include <iostream>
using namespace std;
 
int findNum(int n) {
    char num = 1;
    int cnt = 0;
    while (true) {
        int temp = num;
        while (temp % 5 == 0) {
            cnt++;
            temp /= 5;
        }
        if (cnt >= n) {
            return num;
        }
        num++;
    }
}
 
int main() {
    int n = 1;
    cout << findNum(n) << endl;
    return 0;
}