# Auto requirements script

## created by Paweł Perenc

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Python script allowing for quickly entering the necessary requirements into the requirements.txt file.
By using "reqs.py", the program will execute "pip freeze > requirements.txt".
However, when using "reqs.py template", the program will open the reqs-template.txt file and based on the library names entered there, it will trace pip freeze and save libraries with the right versions.

Without template:

1. Run the following command:

'''powershell
reqs.py
'''

Using the template:

1. Open the reqs-template.txt file.
2. Enter the names of the libraries you want to include in the requirements.txt file, each on a new line.
3. Save the changes to the reqs-template.txt file.
4. Run the following command:
   '''powershell
   reqs.py template
   '''

### Built With

- [Python](https://www.python.org/)

<!-- LICENSE -->

## License

Distributed under the MIT License.

<!-- CONTACT -->

## Contact

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/pawe%C5%82-perenc-51b39315a/
