## Project Purpose 

Display a list of movies with poster images in a website. 
User can click on images to see trailer video.  
<br />
<br />
<br />


## Modules Included:

* media.py: 
* entertainment_center.py: 
* fresh_tomatoes.py
<br />
<br />
<br />


## Usage:

First, make sure python is already installed on your computer. <br />
In command window, navigate to the folder where entertainment_enter.py
is located, <br />
then type ```python entertainment_center.py```

 ##### How to customize the code for use:
The Movie class is defined in media.py and instances of Movie
class are generated in entertainment_center.py. Construct a list
of Movie instances and use API from fresh_tomatoes.py to create and
open a website.
<br />
<br />
<br />

 ##### Example: entertainment_center.py
```
import media
import fresh_tomatoes

movieA = media.Movie(var1,var2,var3,var4)
movieB = media.Movie(var1,var2,var3,var4)
  .
  .
  .
movies = [movieA, movieB,…]
fresh_tomatoes.open_movies_page(movies)
```

