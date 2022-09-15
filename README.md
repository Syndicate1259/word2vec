<!-- Original Template: https://github.com/othneildrew/Best-README-Template/ -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
-->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<h1 align="center">A Closer Look at Analogies in Word2Vec</h1>
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://www.csuchico.edu/stemconnections/_assets/images/stemsignature-engineering-400p.png" alt="Logo" width="200" height="100">
  </a>
  <h3>CSU, Chico CSC&#178; Apprenticeship</h3>
</div>


<!-- TABLE OF CONTENTS -->
<!-- <details> -->
<summary>Table of Contents</summary>
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
    <ul>
    </ul>
  </li>
  <li>
    <a href="#setup">Setup</a>
    <ul>
      <li><a href="#before-you-run">Before You Run</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>
<!-- </details> -->


<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center" >
  <img src="https://i0.wp.com/datascientest.com/wp-content/uploads/2020/09/word2vec.jpg" alt="Logo" width="700" height="300">
</div>
<p>Consider the question “man is to king as woman is to what”? Starting with the embedding of king, subtracting man, and adding woman, we end up near the embedding for queen. This is more or less what Word2Vec does with the generated embeddings to answer a variety of questions of the same type such as states and their capitals to adjectives and adverbs! Word2Vec generates semantically meaningful word embeddings and most of Word2Vec's correct guesses were at least 70% of the way to their intended resulting embedding!
</p>
<p>
This is great, but, it is not perfect. A significant amount of work has been done to understand how Word2Vec represents true analogies, but, little has been done to detect patterns using groups of words that do not represent true analogies. We seek to better define the relationship between random groups of words, in the context of Word2Vec embeddings, and to develop methods of recognizing true analogies using machine learning techniques. Furthermore, we hope to identify other potential relationships between words captured by Word2Vec embeddings.
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Setup
<ul>
  <li>We’ll be using Python 3.9.5 for the program.</li>
  <li>Gensim 4 for Word2Vec.</li> 
  <li>Google-news-300 dataset for the trained model.</li>
</ul>


### Before you run
  - Refer to the resources below
    + https://radimrehurek.com/gensim/auto_examples/index.html#core-tutorials-new-users-start-here
  - Make sure to read the top of the python file and look through file load/write functions to see what variables are hardcoded and can/need to be changed to ensure proper function of the program.
    + Hopefully the file is well commented and simple enough to understand by going through the code.


### Installation 
These instructions are for Ubuntu systems. Other systems may follow different instructions.
1. Update your local system's repository and install the latest version of Python
   ```sh
   sudo apt update
   ```
   ```sh
   sudo apt install python3
   ```
2. Install the latest version of gensim and matplotlib
   ```sh
   pip install --upgrade gensim
   ```
   ```sh
   pip install matplotlib
   ```
4. Create a folder for the project and change to that directory
   ```sh
   mkdir w2v_project
   ```
   ```sh
   cd w2v_project
   ```

3. Clone the repo
   ```sh
   git clone https://github.com/Syndicate1259/word2vec.git
   ```


### How to run
  ```sh
  python3 wordTOvec.py 
  ```


<!-- USAGE EXAMPLES 
## Usage
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->
<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AwesomeFeature`)
3. Commit your Changes (`git commit -m 'Added some awesome feature'`)
4. Push to the Branch (`git push origin feature/AwesomeFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Jose Sanchez - jose.sanchez849@gmail.com
``` Please add the subject [Word2Vec] on emails ```

Project Link: [https://github.com/Syndicate1259/word2vec](https://github.com/Syndicate1259/word2vec)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS 
## Acknowledgments

* []()
* []()
* []()
-->

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/Syndicate1259/exercise.svg?style=for-the-badge
[license-url]:     https://github.com/Syndicate1259/exercise/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jose-sanchez-9b7141140

<!-- License -->
<!-- 
MIT License

Copyright (c) 2021 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->
