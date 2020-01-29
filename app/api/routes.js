//import express and body parser modules
const express = require('express');
const bodyParser = require ('body-parser');
const Cors = require("cors");

const { getById, post, getHistory } = require('./controller')

//get acces to express
const app = express();
//use Cors
app.use(Cors());
//use bodyParser
app.use(bodyParser.json());




// GET ROUTE
app.get('/', (req,res) => {
    getHistory(req,res)
});

app.get('/block/:id', (req,res) =>{
    getById(req,res)
});

app.post('/block', (req,res) =>{
    post(req,res)
});
// POST ROUTE
app.post('/', (req,res) =>{
    post(req,res)
});

//expose express
module.exports = { app };
