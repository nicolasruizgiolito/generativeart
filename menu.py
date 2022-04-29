# Inspired and based on pixegami's project:    https://github.com/pixegami-team/machine-psychology-python-art
# -----------------------------------------------------------------------------------------------------------


import art_generator_src

def menu():

    print("""
    
    WELCOME TO THE ART GENERATOR

    1. Enter how many images you want to crate (max. 50): 
    2. Enter your name or any word: 

    
    """)


if __name__ == '__main__':
    menu()

    images_number = input('1: ')
    try:
        images_number = int(images_number)
    except ValueError:
        print('Invalid option. Enter a number')
        images_number = input('1: ')
    if images_number > 50:
        print('The maximun images allowed to be created is 50')
        images_number = input('1: ')
    name = input('2: ')

    for i in range(1, images_number + 1):
        art_generator_src.generate(f'generated_art_image_{i}.png', name)
        print(f'Art # {i} Generated succesfully')
        


    