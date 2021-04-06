import movie
import fresh_tomatoes

toy_story=movie.Movies("Toy Story","This is the story of boy and his toy",
                       "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0114709%2F&psig=AOvVaw28ZqM_KcoocdUz57CLTk1W&ust=1617778643141000&source=images&cd=vfe&ved=2ahUKEwjww4ichenvAhVFcH0KHcZdBFgQr4kDegUIARDVAQ",
                       "https://www.youtube.com/watch?v=wmiIUN-7qhE")
#print(toy_story.title)
bahubali=movie.Movies("Bahubali","bahubali movie","https://en.wikipedia.org/wiki/File:Baahubali_The_Beginning_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=Eo7DRhdfiQE")

avengers=movie.Movies("Avengers","avengers movie","https://en.wikipedia.org/wiki/File:The_Avengers_(2012_film)_poster.jpg",
                      "https://www.youtube.com/watch?v=eOrNdBpGMv8")

msdhoni=movie.Movies("M.S.Dhoni","m.s.dhoni movie","https://en.wikipedia.org/wiki/File:M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                       "https://www.youtube.com/watch?v=6L6XqWoS8tw")
roohi=movie.Movies("Roohi","roohi","https://en.wikipedia.org/wiki/File:Roohi_film_poster.jpg",
                   "https://www.youtube.com/watch?v=mTT_V0t89MI")
chhichhore=movie.Movies("Chhichhore","chhichhore","https://en.wikipedia.org/wiki/File:Chhichhore_Poster.jpg",
                        "https://www.youtube.com/watch?v=tsxemFX0a7k")

#print(bahubali.movie_line)
movies=[toy_story,bahubali,avengers,msdhoni,roohi,chhichhore]
fresh_tomatoes.open_movies_page(movies)


