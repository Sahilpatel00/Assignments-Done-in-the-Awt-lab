var express = require("express");
var app = express();
var port = 3000;
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

var mongoose = require("mongoose");
mongoose.Promise = global.Promise;
mongoose.connect("mongodb://127.0.0.1:27017/mydb");
var nameSchema = new mongoose.Schema({
    name: String,
    email: String,
    address: String,
    hobby1: String,
    hobby2: String,
    hobby3: String,
    hobby4: String,
});
var User = mongoose.model("users", nameSchema);

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.post("/addname", (req, res) => {
    var myData = new User(req.body);
    myData.save()
        .then(item => {
            res.send("Name saved to database");
        })
        .catch(err => {
            res.status(400).send("Unable to save to database");
        });
});
app.get("/getdata", (req, res) => {
    User.find({})
        .then((data) => {
            res.render("data.ejs", { users: data });
        })
        .catch((err) => {
            res.status(500).send({
                message: err.message || "Some error occurred while retrieving users.",
            });
        });
});
app.set("view engine", "ejs");
app.set("views", __dirname + "/views");
app.listen(port, () => {
    console.log("Server listening on port " + port);
});