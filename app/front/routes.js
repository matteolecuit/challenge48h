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
    res.sendFile(__dirname + '/book.html')
});

module.exports = {
    app
}