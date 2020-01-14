var github = require('octonode');

var client = github.client();

client.get('/repos/salord-f/rimel', {}, function (err, status, body, headers) {
  console.log(body); //json object
});