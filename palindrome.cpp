#include<iostream>
using namespace std;

//HAFID ABI DANISWARA
//SOAL NO 5, DIBUAT DENGAN CPP

bool palindrom(string s1){
    int i = 0;
    int n = s1.length();

    //melakukan iterasi dari depan dan mencocokan dengan char paling belakang
    //kemudian i bertambah dan mencocokan dengan char ke-i dari depan dengan char ke-i dari belakang 
    while (i < s1.length()/2)
    {
        if(s1[i]!=s1[n-1-i]){
            //kalau berbeda return false
            return false;
        }else{
            i++;
        }

    }

    //jika tidak ada yang berbeda, alias ketika dibalik sama semua return true
    return true;
}

int main(){
    string mystr;
    cin >> mystr;
    if(palindrom(mystr)){
        //jika memenuhi palindrom maka print true
        cout<<"True";
    }else{
        //jika sebaliknya print false
        cout<<"False";
    }
    cout<<endl;
    return 0;
}