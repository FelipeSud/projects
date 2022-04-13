const prompt = require('prompt-sync')();

var tweet = prompt("Compose your tweet");
tweet.slice(0, 141)
console.log("You have written " + tweet.length + " characters, you have " + (140 - tweet.length) + " characters remaining. ");
