from project.song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        current_song = next(filter(lambda x: x.name == song_name, self.songs))
        if current_song not in self.songs:
            return f"Song is not in the album."

        self.songs.remove(current_song)
        return f"Removed song {current_song.name} from album {self.name}."

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        song_details = [f'== {song.get_info()}' for song in self.songs]
        return f'Album {self.name}\n' + '\n'.join(song_details)

