from brinfluence.lib import data, static_data

print("Root dir is a path to a dataset directory such as C:\\Users\hp\Desktop\Instagram Dataset")
print("This directory should contain directories of different Users/Brands with their Instagram data inside it.")
root_dir = static_data.get_dataset_root_dir()

print("\nEnter Y for yes. Any other key for no.")
option = input("Do you want to delete old sma_data first? ")

if option == 'Y':
    data.delete_sma_data(root_dir)
    print("Old sma_data has been deleted.")

print("\nGenerating sma_data for all users/brands...\n")
data.generate_sma_data(root_dir)
print("\nsma_data has been successfully generated.")

'''
data_matrix = data.retrieve_sma_data(root_dir, 'Brands')

print('\n')
for row in data_matrix:
    print("Username: " + row[0])
    print("Media: " + row[1])
    print("Comments: " + row[2])
    print("Media emojis: " + row[3])
    print("Comments emojis: " + row[4])
    print('\n')
'''

