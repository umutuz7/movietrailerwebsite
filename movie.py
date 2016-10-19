class Movie():
    def __init__(self,title,main_actor):
        self.title = title
        self.main_actor = main_actor
    def print_all(self):
        print ("Movie name: " + self.title)
        print ("Main Actor: " + self.main_actor)
