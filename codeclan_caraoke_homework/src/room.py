class Room:

    def __init__(self, name, songs, guests, capacity, guests_spending):
        self.name = name
        self.songs = songs
        self.guests = guests
        self.capacity = capacity
        self.entrance_fee = 12
        self.guests_spending = guests_spending

    def check_capacity(self):
        if len(self.guests) < self.capacity:
            return "Room has spaces"
        return "Room is full"
    
    def check_in(self, guest):
        self.guests.append(guest)
        return self.guests

    def check_out(self, guest_leaving):
        for guest in self.guests:
            if guest == guest_leaving:
                self.guests.remove(guest)
        return self.guests

    def check_for_song(self, song):
        for song in self.songs:
            if song == song:
                return "We have that song!"
                
    def add_song(self, song):
        self.songs.append(song)
        return self.songs

    def add_entry_fees_to_room(self):
        for guest in self.guests:
            self.guests_spending += self.entrance_fee
        return self.guests_spending

    def add_drink_to_room(self, bar):
        self.guests_spending += bar.drink
        return self.guests_spending

    def add_food_to_room(self, bar):
        self.guests_spending += bar.food
        return self.guests_spending
