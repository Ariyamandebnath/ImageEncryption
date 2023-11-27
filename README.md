# ImageEncryption
This just a basic Image Encrytion Algortihm doing just some simple pixel cooardinate manipulations.

Code Improvement:
python
Copy code
import time
from PIL import Image


Image Encryption and Decryption using Pixel Swapping
This Python script demonstrates a simple image encryption and decryption algorithm using pixel swapping. The algorithm divides the image into blocks and swaps pixels within each block based on specific conditions. Note that this example is for educational purposes and is not suitable for real-world security.

Usage:
Enter Image Path:

Run the script and enter the path of the image when prompted.
Encryption:

The script divides the image into blocks and swaps pixels based on the provided key.
The encrypted image is saved as "encrypted_image.png".
Decryption:

The script reverses the encryption process to decrypt the image.
The decrypted image is saved as "decrypted_image.png".
Timing:

The script measures and prints the time taken for both encryption and decryption.
