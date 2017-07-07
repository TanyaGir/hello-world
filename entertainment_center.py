import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "The story about a boy whose toys come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "Story of a marine on a alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()


finding_nemo = media.Movie("Finding Nemo",
                           "The story about how a lost fish finds his way back home",
                           "https://en.wikipedia.org/wiki/Finding_Nemo#/media/File:Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")
#finding_nemo.show_trailer()

midnight_in_paris = media.Movie("Midnight in Paris",
                                "The story about going back in time to meet authors",
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")


ratatouille = media.Movie("Ratatouille",
                          "The story about a rat",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

kung_fu_panda = media.Movie ("Kung Fu Panda",
                 "The story about a Panda",
                 "https://en.wikipedia.org/wiki/Kung_Fu_Panda#/media/File:Kungfupanda.jpg",
                 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

movies = [toy_story, avatar, finding_nemo, midnight_in_paris, ratatouille, kung_fu_panda]

fresh_tomatoes.open_movies_page(movies)


