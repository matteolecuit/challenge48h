const { app } = require('./routes.js.js');

const port = 3000;

// Start app on desired port
app.listen(port, () => {
    console.log('API was launched on port:' + port )
});