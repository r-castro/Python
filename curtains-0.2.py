__version__ = 0.2
__maintainer__ = "maintainer@website.com"
__status__ = "Prototype"

roll_width = 140
price_per_metre = 5

window_height = input('Enter the height of the window (cm): ')
window_width = input('Enter the width of the window (cm): ')

print()
print('\twidth\theight\twidths\ttotal\tprice\tshorter?\twider?')

curtain_width = (float(window_width) * 0.75) + 2
                
