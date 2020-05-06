# A mini project by Hoang Nguyen (hoangdesu@gmail.com)

import requests
import math

def LookupActress():
    url = 'https://jav-rest-api-htpvmrzjet.now.sh/api/actress?name='
    actressName = input("Search for an actress: ")
    actressURL = url + actressName
    # print(actressURL)
    actressRequest = requests.get(actressURL).json()

    counts = len(actressRequest['result'])
    print("{:<3} | {:<7} | {:17} | {}\t".format("#", "ID", "Actress Name", "Japanese Name"))
    print("=======================================================")

    for i in range(counts):
        actress_id = actressRequest['result'][i]['id']
        actress_name = actressRequest['result'][i]['name']
        actress_japName = actressRequest['result'][i]['japanName']
        print("{:>3} | {:<7} | {:17} | {}\t".format(i+1, actress_id, actress_name, actress_japName))
    print('Found {} babes named "{}"'.format(counts, actressName))
    print()

def LookUpMovies():
    video_url = 'https://jav-rest-api-htpvmrzjet.now.sh/api/videos/' 
    actress_id = input("Enter actress ID: ")
    vidURL = video_url + actress_id
    videoRequest = requests.get(vidURL).json()
    video_counts = len(videoRequest['result'])
    total_videos_count = videoRequest['total']
    loop_times = math.ceil(total_videos_count / 99)
    
    actress_name = videoRequest['result'][0]['actress'][0]['name']
    print("{:<3} | {} | {}\t| {:<15} | {}".format("#", "Year", "Name", "Code", "Title"))
    print("=============================================================================")  
    
    for _loop in range(loop_times):
        if _loop > 0:
            vidURL = video_url + actress_id + "?hits=99&offset=" + str(_loop*99)
        else:
            vidURL = video_url + actress_id + "?hits=99"
        print(vidURL)
        videoRequest = requests.get(vidURL).json()
        video_counts = len(videoRequest['result'])

        for i in range(video_counts):
            video_title = videoRequest['result'][i]['name']

            if len(videoRequest['result'][i]['name']) > 50:
                video_title = video_title.replace(video_title[49:], '...')
            else:
                video_title = videoRequest['result'][i]['name']
            
            siteUrl = videoRequest['result'][i]['siteUrl']
            video_code = siteUrl[(siteUrl.find("cid=") + 4):(len(siteUrl) - 1)].replace('00', '-', 1).upper()
            year = videoRequest['result'][i]['date'][:4]

            message = "{:>3} | {} | {}\t| {:<15} | {}".format(_loop*99+i+1, year, actress_name, video_code, video_title)
            print(message)
    print("Found {} videos for {}".format(total_videos_count, actress_name))
    print()
        
def programLoop():
    while True:
        LookupActress()
        LookUpMovies()
        cont = input("Do you wish to continue?[Y/N]: ")
        if cont.lower() == 'n':
            print('Enjoy ;)')
            break

def SuggestAnActress():
    #work in progress
    pass

def SuggestAMovie():
    #work in progress
    pass

if __name__ == "__main__":
    programLoop()

    #Thanks anh Hoàng toidicodedao for the Jav API :v

# if len(actress_name) > 11:
        #     print("{}\t | {} \t| {}\t".format(actress_id, actress_name, actress_japName))
        # else:
        #     print("{}\t | {}\t\t| {}\t".format(actress_id, actress_name, actress_japName))
