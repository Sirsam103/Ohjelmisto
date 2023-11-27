document.getElementById('form').addEventListener('submit', function(event) {
  event.preventDefault();
  const query = document.getElementById('query').value;
  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
    .then(response => response.json())
    .then(data => {console.log('Search Results:', data)});
});