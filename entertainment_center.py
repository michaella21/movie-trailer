import media
#import fresh_tomatoes
import extra_fresh_tomatoes

amelie = media.Movie("Amelie",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=sECzJY07oK4",
                     "A fanciful comedy about a young woman who discretely orchestrates the lives of the people around her, creating a world exclusively of her own making.",
                     "Jean-Pierre Jeunet",
                     "Audrey Tautou, Mathieu Kassovitz, Rufus",
                     "2001")

silver_lining = media.Movie("Silver Lining Playbook",
                            "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg",
                            "https://www.youtube.com/watch?v=Lj5_FhLaaQQ",
                            "After a stint in a mental institution, former teacher Pat Solitano moves back in with his parents and tries to reconcile with his ex-wife. Things get more challenging when Pat meets Tiffany, a mysterious girl with problems of her own.",
                            "David O. Russell",
                            "Bradley Cooper, Jennifer Lawrence, Robert De Niro",
                            "2012")


martian = media.Movie("The Martian",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8",
                      "An astronaut is mistakenly presumed dead and left behind on Mars, The film depicts his struggle to survive and others' efforts to rescue him.",
                      "Ridley Scott",
                      "Matt Damon, Jessica Chastain, Kristen Wiig",
                      "2015")

fifty_fifty = media.Movie("50/50",
                          "https://upload.wikimedia.org/wikipedia/en/5/51/50_50_Poster.jpg",
                          "https://www.youtube.com/watch?v=gsEOl7nlXcA",
                          "Inspired by a true story, a comedy centered on a 27-year-old guy who learns of his cancer diagnosis, and his subsequent struggle to beat the disease.",
                          "Jonathan Levine",
                          "Joseph Gordon-Levitt, Seth Rogen, Anna Kendrick",
                          "2011")

a_few_good_men = media.Movie("A Few Good Men",
                             "https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
                             "https://www.youtube.com/watch?v=ePo91pMcu94", "Neo military lawyer Kaffee defends Marines accused of murder; they contend they were acting under orders.",
                             "Rob Reiner",
                             "Tom Cruise, Jack Nicholson, Demi Moore",
                             "1992")

once = media.Movie("Once",
                   "https://upload.wikimedia.org/wikipedia/en/9/9d/Once_%282006_film%29poster.jpg",
                   "https://www.youtube.com/watch?v=726SFblz9Lk",
                   "A modern-day musical about a busker and an immigrant and their eventful week in Dublin, as they write, rehearse and record songs that tell their love story.",
                   "John Carney",
                   "Glen Hansard, Marketa Irglova, Hugh Walsh",
                   "2006")

movies = [amelie, silver_lining, once, martian, fifty_fifty, a_few_good_men]

# These two funcions call the list of movie instances as input to generate 
# an HTML file and open it in the browser. Use the proper function which
# matches with the imported module on top. 

#fresh_tomatoes.open_movies_page(movies)
extra_fresh_tomatoes.open_movies_page(movies)
