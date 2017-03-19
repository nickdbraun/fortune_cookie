from post import post

class VideoPost(Post):

    def __init__(self,title,author,url):
        super().__init__(title, author, None)
        self.video_url = url
        self.plays = 0

    def play(self):
        self.plays +=1

    def __str__(self):
        return "Title: " + self.title + "Author: " + self.author + "URL: " + self.video_url

samplePost = Post("I like cates", "Nick Braun", "duh")
sampleVideo = VideoPost("Cat video", "Nick Braun","www.catvideos.com")

samplePost.like()
sampleVideo.like()

print(samplePost)
print(sampleVideo)
