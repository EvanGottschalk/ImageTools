<!--
*** Do a search and replace for the following:
*** EvanGottschalk, ImageTools, EvanOnEarth_eth, evan.blockchain@gmail.com, A simple set of functions for quickly editing groups of images
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--   <a href="https://github.com/EvanGottschalk/ImageTools">
    <img src="README_images/logo.png" alt="Logo" width="250" height="130">
  </a> -->
  <a href="https://github.com/EvanGottschalk/ImageTools">
    <img src="README_images/banner.png" alt="ImageTools" height="200">
  </a>

  <h3 align="center">ImageTools</h3>

  <p align="center">
    A simple set of functions for quickly editing groups of images
    <br />
    <a href="https://github.com/EvanGottschalk/ImageTools"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EvanGottschalk/ImageTools">View Demo</a>
    ·
    <a href="https://github.com/EvanGottschalk/ImageTools/issues">Report Bug</a>
    ·
    <a href="https://github.com/EvanGottschalk/ImageTools/issues">Request Feature</a>
  </p>
</p>




<br>





<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>





<br>






<!-- ABOUT THE PROJECT -->
## About The Project

`ImageTools` is a simple set of functions for quickly editing groups of images.

To be able to edit groups of thousands of images, this program was built off of some basic functions such as `crop()`, `resize()` and `append()`. These basic functions take simple inputs to make fundamental changes to individual images, as well as to combine pairs of images.

The most useful functions in `ImageTools` are `cropBatch()`, `resizeBatch()`, and other batch functions that iterate through folders of images to rapidly make many edits of various kinds.

By using the different `batch` functions in `ImageTools` sequentially, one can take groups of images with different sizes and dimensions, and make them uniform. Simultaneously, one can overlay or append other images to add logos, captions, branding, and other stylization uniformly.


<a href="https://github.com/EvanGottschalk/ImageTools">
  <img src="README_images/screenshot.PNG" alt="ImageTools in action" height="200">
</a>


<br>






### Built With

* [PIL (Pillow / Python Image Library)](https://pillow.readthedocs.io/en/stable/) - this library provides functions for creating and editing images with Python
* [MoviePy](https://pypi.org/project/moviepy/) - this library provides functions for opening and editing videos with Python






<br>







<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.




<br>





### Prerequisites

`ImageTools` requires Python version 3.10.0 or later.




<br>





### Installation

1. Clone this repository
   ```
   git clone https://github.com/EvanGottschalk/ImageTools
   ```
2. Install PIL
   ```
   pip install Pillow
   ```
3. Install MoviePy
   ```
   pip install moviepy
   ```
4. Run the program




<br>





<!-- USAGE EXAMPLES -->
## Usage

To get started, simply add images or image folders to the project folder. Then, run individual `batch` functions through the command line, or edit the end of the file to automatically run a series of functions.

You can see example setups for folder names, file names and function parameters at the bottom of the `ImageTools.py` file.




<br>





<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EvanGottschalk/ImageTools/issues) for a list of proposed features (and known issues).

### Upcoming Features

* More video editing options
* More image management library options
* AI-generated image capabilities



<br>





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request





<br>






<!-- LICENSE -->
## License

Distributed under the GNU GPL-3 License. See `LICENSE` for more information.





<br>






<!-- CONTACT -->
## Contact

Evan Gottschalk - [@EvanOnEarth_eth](https://twitter.com/EvanOnEarth_eth) - evan.blockchain@gmail.com

Project Link: [https://github.com/EvanGottschalk/ImageTools](https://github.com/EvanGottschalk/ImageTools)





<br>






<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Thinking about contributing to this project? Please do! Your Github username will then appear here.





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/EvanGottschalk/ImageTools.svg?style=for-the-badge
[contributors-url]: https://github.com/EvanGottschalk/ImageTools/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EvanGottschalk/ImageTools.svg?style=for-the-badge
[forks-url]: https://github.com/EvanGottschalk/ImageTools/network/members
[stars-shield]: https://img.shields.io/github/stars/EvanGottschalk/ImageTools.svg?style=for-the-badge
[stars-url]: https://github.com/EvanGottschalk/ImageTools/stargazers
[issues-shield]: https://img.shields.io/github/issues/EvanGottschalk/ImageTools.svg?style=for-the-badge
[issues-url]: https://github.com/EvanGottschalk/ImageTools/issues
[license-shield]: https://img.shields.io/github/license/EvanGottschalk/ImageTools.svg?style=for-the-badge
[license-url]: https://github.com/EvanGottschalk/ImageTools/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/EvanGottschalk
