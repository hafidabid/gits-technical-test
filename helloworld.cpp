#include<iostream>

//HAFID ABI DANISWARA
//SOAL NO 1, DIBUAT DENGAN CPP

using namespace std;
int main(){
    int i;
    cin >> i;

    if(i%15 == 0){
        // jika habis dibagi 3&5 atau 15 maka print hello world
        cout << "Hello World" << endl;
    }else if(i%5==0){
        // jika habis dibagi 5 maka print world
        cout << "World" << endl;
    }else if(i%3==0){
        // jika habis dibagi 3 maka print hello
        cout << "Hello" << endl;
    }

    return 0;
}