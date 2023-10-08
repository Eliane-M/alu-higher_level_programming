<script>
  $(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
      var movies = data.results;
      var listMovies = $("#list_movies");
      
      $.each(movies, function (index, movie) {
        var listItem = $("<li></li>").text(movie.title);
        listMovies.append(listItem);
      });
    });
  });
</script>
