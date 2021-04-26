from pytube import YouTube #install the required module
# "pip install pytube" on terminal

link = input("enter ur youtube url : ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))
for i in video:
  print(i)

print("enter the desired option to download the format ")
dn_option = int(input("enter the option : "))
#ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download()

print (" download successfully ")
