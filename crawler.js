const github = require('octonode');

const client = github.client();

client.get('/repos/salord-f/rimel', {}, function (err, status, body, headers) {
  console.log(body); //json object
});

const ghsearch = client.search();

ghsearch.repos({
  q: 'hub+language:go',
  sort: 'created',
  order: 'asc'
}, console.log); //array of search results