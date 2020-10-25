'''
This script prompts a user to pass the internal and external links and outputs 
the number of valid images present in the website.
'''

def number_of_images(*args) -> int:
    '''
    Returns the number of images in the passed urls.
    '''
    count = 0
    image_format = ('png', 'jpg', 'jpeg', '.tif', '.tiff', '.bmp', '.gif')
    for arg in args:
        links = arg['ref']
        for link in links:
            if link.endswith(image_format):
                count += 1
    return count
