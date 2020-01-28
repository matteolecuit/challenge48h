// here we get data from the api 
const sendHttpRequest = (method, url, data) => {
    const promise = new Promise((resolve, reject) => {
    const getRequest = new XMLHttpRequest();
    getRequest.open(method, url);
    getRequest.responseType = 'json';
    if (data) {
        getRequest.setRequestHeader('Content-Type', 'application/json');
    }
    getRequest.onload = () => {
        if (xhr.status >= 400) {
            reject(xhr.response);
        } else {
            resolve(xhr.response);
        }
    };
    getRequest.onerror = () => {
        reject('Something went wrong!');
    };
    getRequest.send(JSON.stringify(data));
    });
    return promise;
};

const getBlock = () => {
    sendHttpRequest('GET', 'http://localhost:3000/').then(responseData => {
    console.log(responseData);
    });
};

module.exports = { getBlock }