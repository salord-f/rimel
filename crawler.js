const github = require('octonode');

const client = github.client();

client.get('/repos/salord-f/rimel', {}, function (err, status, body, headers) {
  console.log(body); //json object
});

const ghsearch = client.search();

ghsearch.repos({
  q: 'language:java',
  sort: 'stars',
  order: 'desc'
}, console.log); //array of search results