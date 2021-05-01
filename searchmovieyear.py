# Python 3.9.4
# Cool way to search for the year a movie came out using the IMDbPY module. 

import imdb
   
imdb = imdb.IMDb()
   

# Searching the movie, not case-sensitive.
search = imdb.search_movie("Drive")
  
year = search[0]['year']
  
print(search[0]['title'] + " : " + str(year))

