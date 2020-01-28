const { getBlock } = require('./controller/bookController');

const express = require('express');

const app = express();

//get pages
app.get('/home', (req, res) => {
    res.sendFile(__dirname + '/index.html')
});

app.get('/blockchain', (req, res) => {
    res.sendFile(__dirname + '/blockchain.html')
});

app.get('/book', (req, res) => {
    getBlock().then(responseData => {
        console.log(responseData);
    
    res.sendFile(__dirname + '/book.html');   
    }
});

app.get('/chov', (req, res) => {
    res.sendFile(__dirname + '/images/chov.png')
});



//app.use(express.static(__dirname + '/images'));
//app.use(favicon(path.join(__dirname,'images',"chov.png")));

module.exports = {
    app
}