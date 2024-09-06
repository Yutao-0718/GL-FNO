import os
import numpy as np
import h5py
from astropy.io import fits

class FITSDataCube:
    def __init__(self, fits_dir, transform=None):
        self.fits_dir = fits_dir
        self.transform = transform
        # Filtering eligible .fits files
        self.fits_file_paths = [os.path.join(self.fits_dir, file) 
                                for file in os.listdir(self.fits_dir) 
                                if file.startswith('BIFROST_en024048_hion_bz_') and file.endswith('.fits')]
        self.dataset_length = len(self.fits_file_paths)

    def __len__(self):
        return self.dataset_length

    def __getitem__(self, idx):
        fits_file_path = self.fits_file_paths[idx]
        with fits.open(fits_file_path) as hdul:
            data = hdul[0].data.astype(np.float32)

        # Get the first slice as input
        input_data = data[0, :, :]
        
        # Get every 5th slice as output
        output_indices = list(range(5, 496, 5))
        output_data = data[output_indices, :, :]

        # If there is an incoming conversion method, the data is converted
        if self.transform:
            input_data = self.transform(input_data)
            output_data = np.array([self.transform(slice_data) for slice_data in output_data])

        return {'input': input_data, 'output': output_data}

def z_score_normalize(data):
    """ Z-score normalization."""
    mean = np.mean(data)
    std = np.std(data)
    return (data - mean) / std

# Set the path to the folder where the .fits file is located
fits_dir = "Data\\BIRROST\\en024048_hion\\atmos"

# Creating a FITS Dataset Object
fits_dataset = FITSDataCube(fits_dir=fits_dir, transform=z_score_normalize)

print(fits_dataset[0]['output'].shape)


# Save processed data using h5py
processed_data_path = "/MHD/wholecubedata_normlization_Bz99.h5"

# Get the path to the directory where the file is located
output_dir = os.path.dirname(processed_data_path)

# If the directory does not exist, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with h5py.File(processed_data_path, 'w') as hf:
    for i in range(len(fits_dataset)):
        sample = fits_dataset[i]
        hf.create_dataset(f'sample_{i}/input', data=sample['input'])
        hf.create_dataset(f'sample_{i}/output', data=sample['output'])

print(f"Processed data saved at: {processed_data_path}")


