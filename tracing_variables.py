__version__ = 0.2

roll_width = 140
price_per_metre = 5

window_height = input('Enter the height of the window (cm): ')
window_width = input('Enter the width of the window (cm): ')

print()
print('\twidth\theight\twidths\ttotal\tprice\tshorter?\ttwider?')

curtain_width = (float(window_width) * 0.75) + 20
print('\t', round(curtain_width, 2))
curtain_length = float(window_height) + 15
print('\t\t', round(curtain_length, 2))

print('\t\t\t\t\t\t', curtain_length < roll_width)
print('\t\t\t\t\t\t\t', curtain_width > roll_width)

if curtain_length < roll_width:
    total_length = (curtain_width * 2) / 100
elif curtain_width > roll_width:
    widths = int(curtain_width / roll_width)
    extra_material = curtain_width % roll_width
    if extra_material < (roll_width / 2):
        widths += 1
    if extra_material > (roll_width / 2):
        widths += 2
    print('\t\t\t', widths)
    total_length = (curtain_length * widths) / 100
else:
    total_length = (curtain_length * 2) / 100

print('\t\t\t\t', round(total_length, 2))

price = total_length * price_per_metre
print('\t\t\t\t\t', round(price, 2))

print("You need", round(total_length, 2), "meters of cloth, costing: ",
      round(price, 2))
