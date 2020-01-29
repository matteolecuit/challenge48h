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

// here we get data from the api 
function getData () {
  
}


// here we slice the hashs because they are too long for our tab 
function Stringslice(hash,previousHash) {
  
  var rawPreviousHash = document.getElementById("previousHash");
  var rawHash = document.getElementById("hash");


rawHash.value = hash; // get the value from the api 
let hashSliced = rawHash.value.slice(0,8);
document.getElementById("hash").innerHTML = hash;

rawPreviousHash.value = previousHash;
let previousHashSliced = previousHash.slice(0,8);
document.getElementById("previousHash").innerHTML = previousHash;


// Tests 
console.log("This is theraw hash"+ rawHash.value);
console.log("This is the spliced hash"+ hashSliced);

// Tests 
console.log("This is the raw previous_hash  "+ rawPreviousHash.value);
console.log("This is the spliced previous_hash "+ previousHashSliced);


}

function showFullPreviousHash(){
document.all.texte.innerText=rawPrevioushash;
console.log('Test ecriture');
}

document.onload = Stringslice("63b74860ef72735b5e3a01a5aff884952484da32c37c0c6c351d8ecaabd18d3d","b10b22134bc01558c79a936b9e5873a881bd9dbf294a242de4430739a52dba3c");

window.onload = getData()

