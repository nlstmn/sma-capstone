from brinfluence.lib import static_data, data, doc2vec

root_dir = static_data.get_dataset_root_dir()

print("Retrieving users data...")
users_data = data.retrieve_sma_data(root_dir, "Users")
print("Retrieving brands data...")
brands_data = data.retrieve_sma_data(root_dir, "Brands")

print("\nShuffling data...")
data_matrix = data.shuffle_data(users_data, brands_data)

print("\nCreating tagged documents...")
tagged_docs = list(doc2vec.create_tagged_document(data_matrix))

print("\nTraining all users & brands:")
full_model = doc2vec.train_data(tagged_docs, 100, 1, 20, 1)
print("Training finished successfully.")

full_model.save("models/full_model")

print("\nTrained all data saved into model at brinfluence/lib/models as full_model")





'''
print("Creating tagged documents for users...")
tagged_users = list(doc2vec.create_tagged_document(users_data))
print("Creating tagged documents for brands...")
tagged_brands = list(doc2vec.create_tagged_document(brands_data))

print("\nTraining users data:")
user_model = doc2vec.train_data(tagged_users, 100, 1, 10, 1)
print("User data training finished successfully.")

print("\nTraining brands data:")
brand_model = doc2vec.train_data(tagged_brands, 100, 1, 10, 1)
print("Brand data training finished successfully.")

user_model.save('models/user_model')
brand_model.save('models/brand_model')

print("\nTrained user and brand data saved into model at brinfluence/lib/models.")
'''