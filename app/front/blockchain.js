/*
const Http = new XMLHttpRequest();
const url='localhost:3000/';
Http.open("GET", url,true);
Http.setRequestHeader('Content-Type','application/json');

Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
*/


// here we get all the data of our blockchain 
let blockchainHistory = document.getElementById("blockchainHistory")


// here we slice the hashs because they are too long for our tab 
function Stringslice(hash,previousHash) {
  
  let rawPreviousHash = document.getElementById("previousHash");
  let rawHash = document.getElementById("hash");
  
  // str2.substring(8);
//str2 = str2.toString().slice(0,3);
rawHash.value = hash // get the value from the api 
let hashSliced = rawHash.value.slice(0,4);
document.getElementById("hash").innerHTML = hashSliced;
console.log("Ceci est le hash entier "+ rawHash.value);
console.log("Ceci est le hash découpé "+ hashSliced);
}

document.onload = Stringslice("Bonjour");


