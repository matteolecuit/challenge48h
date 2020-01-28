// here we get data from the api 
const request = require('request');
const getBlock = () => {
    return new Promise((resolve, reject) => {
        request( {
            url: 'http://localhost:3000/',
            json: true
        }, (error, response, body) => {
            if(!body) {
                reject(error);
            } else {
                resolve(body); 
            }
            
        })
    });
}

module.exports = { getBlock }