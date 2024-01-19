import vlc

import pafy

url = "https://www.youtube.com/watch?v=LA9tjiiAvN0&pp=ygUjcGFydGl0aWlvbmluZyBzdG9yYWdlIG9uIHdpbmRvd3MgMTE%3D"

video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)

media.play()