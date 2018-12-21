import os
from brinfluence.lib import static_data


def rename_metadata(root_dir):
    for subdir in os.listdir(root_dir):
        if subdir == 'Brands':
            path = root_dir + "\\Brands"
            for brand in os.listdir(path):
                path_to_brand = path + "\\" + brand

                if '@' not in brand:
                    new_brand = path + "\\@" + brand
                else:
                    new_brand = path_to_brand

                path_to_file = path_to_brand + "\\" + brand + ".json"
                new_file = path_to_brand + "\\metadata.json"

                path_to_profile = path_to_brand + "\\download.json"
                new_profile = path_to_brand + "\\profile.json"

                try:
                    os.rename(path_to_file, new_file)
                except FileNotFoundError:
                    pass

                try:
                    os.rename(path_to_profile, new_profile)
                except FileNotFoundError:
                    path_to_profile = path_to_brand + "\\download (1).json"
                    try:
                        os.rename(path_to_profile, new_profile)
                    except FileNotFoundError:
                        pass

                try:
                    os.rename(path_to_brand, new_brand)
                except FileNotFoundError:
                    pass

        if subdir == 'Users':
            path = root_dir + "\\Users"
            for user in os.listdir(path):
                path_to_user = path + "\\" + user

                if '@' not in user:
                    new_user = path + "\\@" + user
                else:
                    new_user = path_to_user

                path_to_file = path_to_user + "\\" + user + ".json"
                new_file = path_to_user + "\\metadata.json"

                path_to_profile = path_to_user + "\\download.json"
                new_profile = path_to_user + "\\profile.json"

                try:
                    os.rename(path_to_file, new_file)
                except FileNotFoundError:
                    pass

                try:
                    os.rename(path_to_profile, new_profile)
                except FileNotFoundError:
                    path_to_profile = path_to_user + "\\download (1).json"
                    try:
                        os.rename(path_to_profile, new_profile)
                    except FileNotFoundError:
                        pass

                try:
                    os.rename(path_to_user, new_user)
                except FileNotFoundError:
                    pass


root_dir = static_data.get_dataset_root_dir()
rename_metadata(root_dir)
