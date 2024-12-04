class Movie:
    
    title:str
    
    rating:int
    
    runtime:int
    
    director:str
    
    genre:str
    
    def set_movie(self,title,rating,runtime,director,genre):
        
        self.title=title
        
        self.rating=rating
        
        self.runtime=runtime
        
        self.director=director
        
        self.genre=genre
        
    def movie_display(self):
        
        print(self.title,self.rating,self.genre)
        
Movie_instance1=Movie()

Movie_instance2=Movie()

Movie_instance1.set_movie("kgf",4.3,2,"revi","horror")
Movie_instance1.movie_display()