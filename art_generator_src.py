from PIL import Image, ImageDraw, ImageShow, ImageFont
import random
import colorsys



#Get different HSV values and then convert them to RGB to use as the background color
def random_color():
    h = random.random()
    s = 1
    v = 1
    float_rbg = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rbg]

    return tuple(rgb)

#Set the padding value to get white space in the final image.
padding = 150

#Set random points for lines and letters 
def random_point():
    point = random.randint(padding, 1000 - padding)
    return point

#This function enables us to write a text
def write(img, name):
    text_font = ImageFont.truetype('arial.ttf', 46)
    add_text = ImageDraw.Draw(img)
    for letter in name:
        add_text.text((random.randint(100, 1000 - 100), random.randint(100, 1000 - 100)), letter, color= random_color(), font= text_font)

#Main function
def generate(path, name):
    #Set the image size
    img_size = 1000
    #Set the image color (black)
    img_color = 0, 0, 0 
    #Create the image
    img = Image.new('RGB', (img_size, img_size), (img_color))
    #Write in the image
    write(img, name)

    #Star writting the lines
    draw = ImageDraw.Draw(img)
    points_lists = []
    #For loop to create multiple lines (50)
    for i in range(50):
        points_lists.append(random_point())

    thickness = 0
    for i in range(0, len(points_lists), 2):
        if i != len(points_lists) - 2:
            line = (points_lists[i], points_lists[i + 1], points_lists[i + 2], points_lists[i + 3])
        else:
            line = (points_lists[i], points_lists[i + 1], points_lists[0], points_lists[1])

        line_color = random_color()
        thickness += 1
        draw.line(line, fill=(line_color), width= thickness)


    #Save the image
    img.save(path)
    #Display the image
    ImageShow.show(img)

    
    