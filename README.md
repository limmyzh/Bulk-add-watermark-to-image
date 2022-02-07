# Bulk-add-watermark-to-image
Script for bulk adding of watermark logo to images.

### Guidelines
The "watermark logo" image file is stored in the root folder and is named "water.png" and has to be a .png file.
To replace with another image, ensure that the file is named "water.png" or change the value for the "watermarkFile" variable in the code. 

Images in the input file need to be .jpg files. Images that are not .jpg will simply not be processed.
Images that have completed the process will be saved as .png files. 

#### Limitations 
Existing image should have a <strong>white background</strong>, as a white border will be added to each image when pasting the watermark. 
This is to prevent the logo from clashing with the product. 

## Example

### Before
![ffd6a0cd733a82fb2dff3f35e7b64302](https://user-images.githubusercontent.com/57295582/152694956-822cb93b-573e-4313-81b7-9460b517fd5d.jpg)
### After
![ffd6a0cd733a82fb2dff3f35e7b64302 jpg_watermarked](https://user-images.githubusercontent.com/57295582/152694951-c753cf46-b8fc-4ff1-9098-b51dc92dde2a.png)
