import webbrowser

path = '/home/huecogirl/pearlHacks/output.txt'
days_file = open(path,'r')

emotion = days_file.read()
emotion = int(emotion)

mood=['happy','sad', 'angry']
art_h = 'https://jamesclear.com/eat-healthy'
art_s = 'https://www.lifehack.org/articles/communication/overcome-sadness-19-simple-things-you-didnt-realize-you-can.html'
art_a = 'https://www.lifehack.org/articles/communication/20-things-when-you-feel-extremely-angry.html'

articles = [art_h, art_s, art_a]

mus_h = 'https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC?si=cSdiTgAyR2eu8JWC4x63Yg'
mus_s = 'https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx'
mus_a = 'https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6'

music = [mus_h, mus_s, mus_a]

vid_h = 'https://youtu.be/8KkKuTCFvzI'
vid_s = 'https://www.youtube.com/watch?time_continue=4&v=mYUQ_nlZgWE&feature=emb_title'
vid_a = 'https://www.youtube.com/watch?v=BsVq5R_F6RA'

video = [vid_h, vid_s, vid_a]

quo_h = 'https://www.pinterest.com/rachelmaser/being-happy-quotes/'
quo_s = 'https://www.pinterest.com/search/pins/?rs=ac&len=2&q=uplifting%20quotes%20for%20hard%20times&eq=UPLIFTI&etslf=8059'
quo_a = 'https://www.pinterest.com/search/pins/?rs=ac&len=2&q=calming%20quotes&eq=CALMIN&etslf=7578'

quotes = [quo_h, quo_s, quo_a]

def showRes(emotion):
    a=0
    while(a<5): 
        print('\n')
        val = input("Do you want to: \n 1) read a article \n 2) listen to music \n 3) watch a video \n 4) read quotes \n 5) done for the day \n Enter the number:  ")
        val = int(val)
        a+=1 
        if val == 1:
            webbrowser.open(articles[emotion])
        elif val == 2:
            webbrowser.open(music[emotion])
        elif val == 3:
            webbrowser.open(video[emotion])
        elif val == 4:
            webbrowser.open(quotes[emotion])
        else:
            print('\n')
            print('*********************************************************')
            print('*********************************************************')
            print("Have a mindful day!")
            exit()

def main():
    print('\n')
    print('*********************************************************')
    print('*********************************************************')
    print("\nYou seem " + mood[emotion]) 
    print('\n')
    showRes(emotion)

if __name__ == '__main__':
    main() 