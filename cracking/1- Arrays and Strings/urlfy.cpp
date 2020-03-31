#include <bits/stdc++.h>

using namespace std;

int main(){
    string test = "Mr John Smith         ";
    int length = 13;
    int spaces = 0;
    for(int i = 0; i < length; i++) if(test[i] == ' ') spaces++;
    int newLength = length + 2 * spaces + 1;
    char ans[newLength];
    ans[newLength - 1] = '\0';
    int actualSpaces = 0;
    for(int i = 0; i < length; i++){
        if(test[i] == ' '){
            ans[i + 2 * actualSpaces] = '%';
            ans[i + 2 * actualSpaces + 1] = '2';
            ans[i + 2 * actualSpaces + 2] = '0';
            actualSpaces += 1;
        }
        else{
            ans[i + 2 * actualSpaces] = test[i];
        }
    }
    cout << ans << endl;
}