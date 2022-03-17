const express = require("express")
const app = express()
const http = require("http")

app.use(express.static("public"))
app.use(express.json())
const server = http.createServer(app)

server.listen(3000, "localhost", () => {
    console.log("Server started")
})

app.get("*", (req, res) => {
    res.sendFile(__dirname + "/public/index.html")
})