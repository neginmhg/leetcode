# Q1

# We are building a cloud-based music player, like Spotify.
# Let's start with the following functionality:

# * `add_song (song_title [string])`
#    - A song is given an incremental integer ID when it's added, starting with 1

# * `play_song (song_ID [integer], user_ID [integer])`
#    - Assume any user ID is valid, and that the given song ID will have been added

# * `print_analytics_summary ()`
#    - This is used for a report, created once per day for our company's Analytics department.
#    - The summary should be sorted (descending) by the number of unique users who have played each song.
#    - The summary should include the song titles, and the number of unique users, but the formatting does not matter.

# For our MVP, consider performance as we will eventually support millions of songs and users.
# However, let's not worry about thread safety or persistence for now - store data in memory.


#add_song('song_1') # 1
#add_song('song_2') # 2

#play_song(1, 0)
#play_song(1, 1)
#play_song(2, 0)




import collections
class Playlist:
    def __init__(self):
        self.lastSongId=0
        self.songs = {}         #songid : title
        self.played =collections.defaultdict(set) #{(songid: {userids}}
        self.userIDs = set()
    def add_song(self,title: str) -> int:
        #create a unique song id
        self.lastSongId += 1   
        #add it to songs
        self.songs[self.lastSongId] = title   
        return self.lastSongId
    
    def play_song(self, songId: int, userId: int):
        #check if the songId exists
        if songId in self.songs:
            self.played[songId].add(userId)
        # show an error
        
    
    def print_analytics_summary(self):
        #for each song
        result =[]
        for k,v in self.played.items():
            title = self.songs[k]
            userId = v
            #number of users that plated the song
            numUsers=len(userId)
            result.append((numUsers,title))
        
        result.sort(reverse=True)
        print(result)
            
            



playlist = Playlist()
id1 =playlist.add_song('song_1')
id2 =playlist.add_song('song_2')



playlist.play_song(2, 0)
playlist.play_song(1, 0)
playlist.play_song(1, 1)


playlist.print_analytics_summary() # 2,1 









