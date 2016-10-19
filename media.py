class movie():
    def __init__(self,title,main_actor,image,trailer):
        self.title = title
        self.main_actor = main_actor
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
    def print_all(self):
        print ("Movie name: " + self.title)
        print ("Main Actor: " + self.main_actor)
