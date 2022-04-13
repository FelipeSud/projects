

var tweet = prompt("Compose your tweet");
var tweetUnder140 = tweet.slice(0, 140)
console.log("You have written " + tweet.length + " characters, you have " + (140 - tweet.length) + " characters remaining. ");
