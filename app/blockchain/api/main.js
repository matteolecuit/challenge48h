const { app } = require('./routes.js');

const port = 3000;

// Start app on desired port
app.listen(port, () => {
    console.log('Started on port: ' + port )
});