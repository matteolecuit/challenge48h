// here we get data from the api 
const XMLHttpRequest = require("xmlhttprequest")

const sendHttpRequest = (method, url, data) => {
    const promise = new Promise((resolve, reject) => {
    const getRequest = new XMLHttpRequest();
    getRequest.open(method, url);
    getRequest.responseType = 'json';
    if (data) {
        getRequest.setRequestHeader('Content-Type', 'application/json');
    }
    getRequest.onload = () => {
        if (getRequest.status >= 400) {
            reject(getRequest.response);
        } else {
            resolve(getRequest.response);
        }
    };
    getRequest.onerror = () => {
        reject('Something went wrong!');
    };
    getRequest.send(JSON.stringify(data));
    });
    return promise;
};

const getBlock = (req) => {
    sendHttpRequest('GET', 'http://localhost:3000/', req).then(responseData => {
        return responseData;
    });
};

module.exports = { getBlock }