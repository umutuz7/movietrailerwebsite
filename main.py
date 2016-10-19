import media
import fresh_tomatoes

titanic = media.movie("Titanic","Leonardo Di Caprio","http://images.allposters.com/images/59/003_titanicrip.jpg","https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
#print titanic.title
#print titanic.main_actor
movie_list = [titanic]
webpage = fresh_tomatoes.open_movies_page(movie_list)
#titanic.print_all()
