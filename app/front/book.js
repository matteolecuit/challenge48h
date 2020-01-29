const getBtn = document.getElementById('get-btn');

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

const getData = () => {
    sendHttpRequest('GET', 'http://localhost:3000/').then(responseData => {
    console.log(responseData);
    });
};

getBtn.addEventListener('click', getData);