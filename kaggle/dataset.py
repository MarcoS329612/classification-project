import kagglehub

# Download latest version
path = kagglehub.dataset_download("tushar5harma/food-and-beverage-labels")

print("Path to dataset files:", path)