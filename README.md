# Movie Trailer

This repository contains files to creat **two** different movie trailer HTML pages. Each page includes six movie poster images and titles. To create the relevant html file, keep all the files in the same folder and run the following command in terminal.
```
$ python entertainment_center.py
```
## Versions

1. _Basic version_ (fresh_tomatoes.html) 
: The youtube movie trailer of each poster image will be automatically played when the poster image is clicked. To use this version, make sure unhash the code including extra_fresh_tomatoes on top (line 2,3) and at the bottom (line 54, 55) of the entertainment_center.py.

    ```
    2 import fresh_tomatoes
    3 #import extra_fresh_tomatoes
    ```
    ```
   54 fresh_tomatoes.open_movies_page(movies)
   55 #extra_fresh_tomatoes.open_movies_page(movies)
    ```
2. _Extra version_ (even_fresher_tomatoes.html)
: In addition to the basic version, it provides relevant information about the movie when the movie title is clicked. To use this version, make sure unhash the code including fresh_tomatoes on top (line 2,3) and the bottom(line 54, 55) of the entertainment_center.py. 
   ```
    2 #import fresh_tomatoes
    3 import extra_fresh_tomatoes
    ```
    ```
    54 #fresh_tomatoes.open_movies_page(movies)
    55 extra_fresh_tomatoes.open_movies_page(movies)
    ```

## Notice

fresh_tomatoes.py is forked from [here](https://github.com/udacity/ud036_StarterCode) and extra_fresh_tomatoes.py is written based on fresh_tomatoes.py by myself. 
