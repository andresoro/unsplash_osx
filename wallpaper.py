from appscript import app, mactypes

file = "/path/to/file"

# return a random photo from unsplash.com of certain x, y dim
def get_unsplash_pic(x, y):
    pass

app('Finder').desktop_picture.set(mactypes.File(file))