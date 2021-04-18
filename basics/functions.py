# def make_album(artist,album_name,length=None):
#     album = {'artist': str(artist), 'album': str(album_name)}
#     if length: album['length'] = length
#     return album

# album_list = []

# while True:
#     artist = input('artist: ')
#     album_name = input('album name: ')
#     length = input('length: ')
#     album = make_album(artist, album_name, length)
#     album_list.append(album)
#     print(album_list)


# # passing a list to a function

# def greet_users(names):
#     new_list = []
#     for name in names:
#         name = name * 2
#         new_list.append(name)
#     return new_list

# users = ['jo', 'alex', 'steph']
# greet_users(users)

# print(greet_users(users))


# passing an arbitrary number of arguments to a function

def build_profile(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car_profile = build_profile('renault', 'clio', color='grey', option='baby seat')

print(car_profile)