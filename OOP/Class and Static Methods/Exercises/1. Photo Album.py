from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [list() for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return f"No more free slots"

    def display(self):
        result = ['[] ' * len(photo) if photo else '' for photo in self.photos]
        result = [x.strip() for x in result]
        return "-----------\n" + "-----------\n".join([f'{chars}\n' for chars in result]) + "-----------"


pa = PhotoAlbum(3)
print(pa.display())