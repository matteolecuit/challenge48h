const http = require('http');
const { app } = require('./routes')
const bodyParser = require('body-parser');

const Port = 3001;

http.Server(app)

app.listen(Port, () => {
    console.log('app served on port: ' + Port)
});


const urlencodedParser = bodyParser.urlencoded({ extended: false })


// app.post('/api/fournisseur', urlencodedParser, function (req, res) {
//     postFournisseur;
//     console.log(req.body);
//     res.sendFile(__dirname + '/fournisseurs.html')
// })