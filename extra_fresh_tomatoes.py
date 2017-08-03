import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Even Fresher Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            
            cursor: pointer
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        h3.movie-title{
            color:#1F618D;
        }
        #movieinfo {
            top:30%;    
        }
        #movieinfo .modal-title {
            font-size: 20px; 
            font-weight: bold;
            text-align: left;
        }
        #movieinfo .modal-body {
            padding: 32px;
            padding-top: 20px;

        }
        #myHeader.container{
            font-size:27px;
            font-weight:bold;
            text-aligh:left;
            color:#1F618D;
        }


    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.poster-img', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Show the relevant movie information when modal is opened.
        $(document).on('click','h3.movie-title', function (event) {
          var movieTitle = $(this).attr('data-movie-title')
          var movieReleased = $(this).attr('data-movie-released')
          var movieStory = $(this).attr('data-movie-story')
          var movieDirector = $(this).attr('data-movie-director')
          var movieCast = $(this).attr('data-movie-cast')
          $('#movieModalLabel.modal-title').text(movieTitle + ' (' +movieReleased + ')')
          $('#movieDirector.row').text('Director: '+movieDirector)
          $('#movieCast.row').text('Stars: '+movieCast)
          $('#movieStory.row').text(movieStory)
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

      <!-- Movie Info Modal -->
    <div class="modal" id="movieinfo" role="dialog" area-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
              <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
            <div class="modal-title" id="movieModalLabel">
            </div>
          </div>
          <div class="modal-body">
            <div class="row" id="movieDirector">
            </div>
            <div class="row" id="movieCast">
            </div>
            <br>
            <div class="row" id="movieStory">
            </div>

          </div>
        </div>
      </div>
    </div>


    <!-- Main Page Content -->

    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Even Fresher Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container" id="myHeader">
      <h2 > Please click poster images and movie names to see what happens!</h2>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
# Changed open youtube trailer event by clicking only poster image.
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img class="poster-img" data-trailer-youtube-id="{trailer_youtube_id}"  data-toggle="modal" data-target="#trailer" src="{poster_image_url}" width="220" height="342">
    <h3 class="movie-title" data-toggle="modal" data-target="#movieinfo" data-movie-title="{movie_title}" data-movie-director="{movie_director}" data-movie-cast="{movie_cast}" data-movie-released="{year_released}" data-movie-story="{movie_storyline}">{movie_title}
    </h3>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            movie_director=movie.director,
            movie_cast=movie.main_cast,
            year_released=movie.released
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('even_fresher_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
