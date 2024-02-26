# STEGosaurus - LSB Steganography Tool

To access Start-Up Instructions and the Usage Guide, go [here](https://github.com/ChrisMikhail/STEGosaurus?tab=readme-ov-file#start-up-and-usage-guide).

# What is LSB Steganography? 
Steganography is the method of encoding data inside an image, while making it hard to detect with the naked eye. The most popular way to do this is by changing the least significant bit(s) of a colour channel (so either the R, G, and/or B channels of a pixel's colour) in a pixel to contain parts of information of the data you want to hide. The result is a minimal change as we are changing the LEAST significant bits of the 8-bit channel value. Like changing 255 to 254 - the change is small but to us it can be used to store bits of information that can be re-pieced together to create a message. Optionally, as an extra layer of security, the data is first encrypted before undergoing this process. 

# Start-up and Usage Guide
1. Clone the repository
```
git clone -b app https://github.com/ChrisMikhail/STEGosaurus.git
```
2. Run ```App.exe``` with the ```example``` folder in the same directory and enjoy!
