from brinfluence.lib import data, static_data

option = input("For generating list of brands and users enter 0\nFor generating common words enter 1"
               "\nEnter your value: ")

if option == '0':
    print("Generating list of brands and users...")
    root_dir = static_data.get_dataset_root_dir()
    data.generate_user_brand_list(root_dir)
    print("List of brands and users has been generated\n"
        "and can be found at dataset/<usertype>.txt")
elif option == '1':
    model_type = input("\nPlease enter model type (full, user, or brand): ")
    count = input("Please eneter number of common words to be generated: ")
    print("Generating list of common_words...")
    data.generate_most_common_words(model_type, count)
    print("\nList of common words has been generated\n"
        "and can be found at dataset/common_words_" + model_type + ".txt")
