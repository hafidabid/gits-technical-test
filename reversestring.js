//HAFID ABI DANISWARA
//SOAL NO 4, DIBUAT DENGAN NODE.JS

const readline = require('readline'); //import fungsi untuk baca inputan keyboard

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
}); //inisialisasi interface untuk readline

const reverse = (sebuahString) => {
    //fungsi untuk membalikkan string dengan cara membuat string kosong lalu mengisi dengan char dari belakang string lama
    let r = ""
    let i;
    for(i=sebuahString.length-1;i>=0;i--){
        r = r + sebuahString[i];
    }
    return r;
}

// const string_input = prompt('Masukkan string yang ingin dibalik = ');
// console.log("hasil string setelah dibalik = "+reverse(string_input));

rl.question("Masukkan string yang ingin dibalik = ", (inputan) =>{
    console.log("hasil string setelah dibalik = "+reverse(inputan));

    rl.close();
})