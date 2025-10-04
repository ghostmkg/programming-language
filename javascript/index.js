const express = require("express");
const dotenv = require("dotenv").config();
const app = express();
const path = require("path");
const port = process.env.PORT;

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "/views"));

app.use("/hi", (req, res) => {
  res.send("Hello!");
});
app.use("/sidd", (req, res) => {
  res.send("I am Here");
});

app.get("/rolldice", (req, res) => {
  let dice = Math.floor(Math.random()*6) + 1;
  res.render("rolldice", { dice});
});

app.get('/ig/:username', (req, res) => {
  let {username} = req.params;
  res.render("instagram.ejs", {username});
})

app.get("/home", (req, res) => {
  res.render("home.ejs");
});

app.use("/:username/:id", (req, res) => {
  let { username, id } = req.params;
  res.send(`welcome to page @${username}`);
});

app.get("/search", (req, res) => {
  console.log(req.query);
  let { q } = req.query;
  if (!q) {
    res.send("Nothing Searched");
  }
  res.send(`<h1>no results for : ${q}</h1>`);
});

app.listen(port, () => {
  console.log("server running on port");
});
