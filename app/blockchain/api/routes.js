//import express and body parser modules
const express = require('express');
const bodyParser = require ('body-parser');

const {get, post } = require('./controller')

//get acces to express
const app = express();

//use bodyParser
app.use(bodyParser.json());



// GET ROUTE
app.get('/', (req,res) =>{
    get(req,res)
});

// POST ROUTE
app.post('/', (req,res) =>{
    post(req,res)
});

//expose express
module.exports = { app };
