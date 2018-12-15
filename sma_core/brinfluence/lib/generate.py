from brinfluence.lib import data, static_data


print("Generating list of brands and users...")
root_dir = static_data.get_dataset_root_dir()
data.generate_user_brand_list(root_dir)
print("List of brands and users has been generated\n"
      "and can be found at dataset/<usertype>.txt")

