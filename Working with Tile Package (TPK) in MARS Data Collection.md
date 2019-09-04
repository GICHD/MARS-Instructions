# Working with Tile Package (TPK) in MARS Data Collection.
---- 
Tile Package  is the way that MARS mobile application (APK) manages offline maps for areas that are not covered by network coverage. There are different ways to create your tiles files and one of the direct ways is to use the Tile Package Kreator from Esri. It is available for Windows, Mac and Ubuntu Linux.  

## Getting started with Tile Package Kreator

You can download the Tile Package Kreator from the [ArcGIS MarketPlace][1]  

[The Tile Package Kreator guide][2] will give you a great overview of all the things you can do with Tile Package Kreator. Once you are logged in with your ArcGIS Online account, you will find creating and managing your Tile Packages quite straight-forward.

When you start using Tile Package Kreator, you will notice that there are limits to the overall number of tiles that you can have included in the output Tile Package file.  The size of the package is determined by the owner of the tiled service, who can set limits to the maximum number of tiles that can be extracted into a Tile Package. Specifically for Esri basemaps, this limit is set at 100,000 tiles.  You will need to reduce the area of interest or number of levels to prevent hitting that limit, or otherwise you will get an error 001564: Requested tile count exceeds the maximum allowed number of tiles to be exported.

## Using Tile Packages with Collector and MARS Data Collection
 
You can use the created Tile Packages with MARS. A MARS project requires a TPK otherwise you will not be able to provision (download) your mobile devices with the project forms. Downloading large tile package to the mobile devices or tablets can create an issue when using slow internet connection. This will be more challenging when dealing with large number of devices, not to mention time consuming. That is why you can load your tiles to the device with direct link, like copying to your USB device.
 
### Loading Tile Package files into the device directly you do the following:
  * plug your device into a computer.
  * open file explorer and goto the android device
  * navigate to the following location:
	```bash
	\ANDROID\_DEVICE\_NAME\Internalstorage\Android\data\com.gichd.mars\_app\files
	```
  * rename your TPK to "mars.tpk"
  * copy the renamed file to the above location and replace the existing file
  * now when you open a map you will be using the new TPK file

If you are unable to access the file system on the device you will need to turn on "USB debugging" via developer mode. This is very simple and a quick google search will give you detailed instructions on how to activate this mode on the device.

Let us know if you have any issues and remember that the TPK must be below **3GB** or android will not allow the file transfer. 

_This process will work with Raster Tile Packages as well in the future with Victor Tile Packages._

[1]:	https://marketplace.arcgis.com/listing.html?id=9c9ddae83e5549bb88a2c22e87a18ba1
[2]:	https://github.com/GICHD/MARS-instructions/blob/master/FeatureGuide.pdf