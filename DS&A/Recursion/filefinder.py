# Write a function, fileFinder(directories, targetFile), that accepts an object representing directories and a string representing a filename.
# The function should return true, if the file is contained anywhere in the given directories.
# Note that directory names will begin with '/', but file names will not.



desktop = {
    '/images': {
        'app_academy_logo.svg': None,
        '/parks': {'yosemite.jpeg': None,'acadia.jpeg': None, 'yellowstone.png': None },
        '/pets': {
            'trixie_lou.jpeg': None,
            'rolo.jpeg': None,
            'opal.jpeg': None,
            'diana.jpeg': None,
        }
    },
    '/music': {

        'hey_programmers.mp3': None,

        '/genres': {
            '/rock': {
                'everlong.flac': None,
                'livin_on_a_prayer.mp3': None
            },
            '/hip_hop': {
                'express_yourself.wav': None,
                'ny_state_of_mind.mp3': None
            }
        }
    }
};


def fileFinder(directories, targetFile):
    for directory in directories:
        if directory == targetFile:
            return "/" + directory
        if directory[0]=="/":
            path = fileFinder(directories[directory], targetFile)
            # print(path)
            if path !=None:
                return directory + path
    return None

# print(fileFinder(desktop, 'app_academy_logo.svg'));     ##=> true
# print(fileFinder(desktop, 'everlong.flac'));            ##=> true
# print(fileFinder(desktop, 'sequoia.jpeg'));             ##=> false
