process.env.PATH = '../sqlite;' + process.env.PATH;

const sqlite = require('./build/Release/sqlite3-native');
console.log(sqlite);

module.exports = sqlite

