# Screentone-Remover

A basic web application using streamlit for removing manga screentones. Based on the [original project](https://github.com/natethegreate/Screentone-Remover) by natethegreate.
The algorithm remains the same as the original.

Gaussian blur is applied to an image, then an averaging blur afterwards. This removes high frequency signals (screentones).
The output of this is sharpened with a Laplacian kernel, to retain some edge.

Here is a visual example:
![srsfwexample](screentoneexsfw.jpg)
NOTE: More blurring will remove heavier screentones, but will result in more loss of quality from the image. You may need to experiment with the 3 blurring levels depending on the artists screentone usage.

## Usage
Upload your png/jpg/jpeg image into the app, and wait for the output.
It can then be downloaded.

Note: Do not upload coloured panels

<!-- ### Prerequisites
Windows, tested on windows 10.

Python 3 if you want to run the source codes. Uses opencv (cv2) libs, numpy, and tkinter for the UI.

Note that the .exe file is quite large. The signal processing utilizes a large library of signal processing related functions, opencv. -->



<!-- ## Deployment

You should use this in tandem with my other project, hent-AI, and [DeepCreamPy](https://github.com/deeppomf/DeepCreamPy), by deeppomf. -->

## Contributing

Contributions/suggestions are most welcome of course :)
To contribute please make a pull request from your fork of the repository

To clone the project 
```
$ git clone https://github.com/infernalsaber/screentone-cure.git
```

Install the dependencies
```
$ pip install -r requirements.txt
```

Run the project
```
$ streamlit run stremove.py
```



## Versioning

- 0.1: Basic test web version
<!-- 
## Todo

* Allow custom kernel types for blurring and sharpening
* Parameterize Bilateral Filtering inputs for Sigma Space
* Better UI
* Find optimal default values
* Remember and autofill Input/Output directories
* Somehow reduce file size -->

## Credits

- Original Algorithm and GUI: [Nathan Cueto](https://github.com/natethegreate)
- Sample Image: soranosuzume
- Web Interface: infernalsaber

## License

As with the original project, this project is licensed under the MIT license
