/*const Http = new XMLHttpRequest();
const url='localhost:3000';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}

*/

// here we get all the data of our blockchain 
let blockchainHistory = document.getElementById("blockchainHistory")


// here we slice the hashs because they are too long for our tab 
function Stringslice() {
  var str = document.getElementById("previousHash");
  var str2 = document.getElementById("hash");
  // str2.substring(8);
//str2 = str2.toString().slice(0,3);
str2.value = "test"
// document.getElementById("hash").innerHTML = str2;
document.getElementById("previousHash").innerHTML = str2.value;
console.log(str2.value);
}

window.onLoad = Stringslice();

