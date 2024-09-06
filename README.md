# Global-local Fourier Neural Operator for Accelerating Coronal Magnetic Field Model
GL-FNO - an enhanced Fourier neural operator-based deep-learning model for Accelerating Coronal Magnetic Field Model
GL-FNO, or Global-Local Fourier Neural Operator, is a deep learning model designed to accelerate coronal magnetic field simulations, particularly focusing on the complex interactions in the solar outer atmosphere. The model consists of two branches:

1. **Global FNO Branch**: Processes downsampled input data to capture and reconstruct global features of the system.
2. **Local FNO Branch**: Works with high-resolution input to capture fine details and local features.

By combining these two branches, GL-FNO aims to improve the accuracy and efficiency of predicting magnetic field structures, achieving significant computational speed-ups compared to traditional methods like magnetohydrodynamics (MHD) simulations. GL-FNO outperforms other models like CNN-RNN, CNN-LSTM, Vision Transformer in accuracy. Similarly we compare GL-FNO with other FNO-based models (UNO, U-FNO) and again outperform these models.
The following figure shows the structure of GL-FNO.
