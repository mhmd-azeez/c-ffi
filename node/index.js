const sqlite = require("./binding.js");
const fs = require("fs");

const connection = sqlite.open('../sample.db');
const schema = fs.readFileSync("../schema.sql", "utf-8");
sqlite.exec(connection, schema);
sqlite.exec(connection, "INSERT INTO logs (text) VALUES ('hello from NodeJS!');");