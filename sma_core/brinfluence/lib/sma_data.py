from brinfluence.lib import data

print("Enter path to a dataset directory such as C:\\Users\hp\Desktop\Instagram Dataset")
print("This directory should contain directories of different users/brands with their Instagram data inside it.")
root_dir = input('Enter a path :')

data.generate_sma_data(root_dir)

data_matrix = data.retrieve_sma_data(root_dir, 'Brands')

print('\n')
for row in data_matrix:
    print("Username: " + row[0])
    print("Media: " + row[1])
    print("Comments: " + row[2])
    print("Media emojis: " + row[3])
    print("Comments emojis: " + row[4])
    print('\n')

