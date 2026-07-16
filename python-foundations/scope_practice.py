dataset_size = 1000
print(f"Initial datasize: {dataset_size}")

def augment_data(current_size):
    current_size *= 1.5
    print(f"local data size: {current_size}")
    return(current_size)

dataset_size = augment_data(dataset_size)
print(f"final data size: {dataset_size}")