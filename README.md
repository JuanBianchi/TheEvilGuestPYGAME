<a name="readme-top"></a>
<!--
*** Project: Made in Pygame - Python
*** License: MIT License
*** Author: Juan Pablo Bianchi

[![LinkedIn][linedin_img]][linkedin_link] [![Github][github_img]][github_link] 

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="https://raw.githubusercontent.com/pygame/pygame/main/docs/reST/_static/pygame_logo.svg" alt="Logo">
  </a>
  <br />  <br />  <br />
  <h1 align="center">The Evil Guest</h1>

  <p align="center">
    A project made in pygame!
  </p>
</div>


<br />
<br />
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#game-installation">Game installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#debug-mode">Debug mode</a></li>
    <li><a href="#game-previews">Game previews</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the project

This is a first quarter project for the Programming Technicature at the National Technological University.
It is a 2D platform videogame made in Pygame (Python), where the player has to avoid different types of traps, defeat enemies and recolect points from the map to win

Some conceptual features:
* OOP (Object-oriented programming)
* Try/Except
* SQL queries
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built with

* [![Python][python_img]][python_url]
* [![Pygame][python_img]][pygame_url] (Pygame)
* [![Sqlite][sqlite_img]][sqlite_url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Next, these are the steps for downloading repo files and executing it locally

### Prerequisites

To play this game, it must be installed the following:

* _Python - Download Python from Microsoft Store or in Python web page_
  ```sh
  Microsoft Store: https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5
  Python web page: https://www.python.org/
  ```
* _Pygame_
  ```sh
  pip install pygame
  ```

### Game installation

1. _Clone the repo_
   ```sh
   git clone https://github.com/JuanBianchi/TheEvilGuestPYGAME.git
   ```
2. _Download the source files (music & images)_
   ```sh
   https://drive.google.com/drive/folders/1bvIRg1jlNxRt7-T1IrUdtDsbjOOqbaEf?usp=drive_link
   ```
3. _Move "assets" folder with "images" and "sounds" files to the directory repo:_
   ```sh
   TheEvilGuest/src/
   ```
4. _In your CLI, change directory to `/TheEvilGuest/src` and execute_
   ```sh
   python main.py
   ```
5. _Enjoy!_
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### Menu:
In the game menu, buttons are click selected

### Game: 
Playing any level, the controls are:

* Keys `W`, `A`, `D`: Player movement
* Hold Key `SHIFT`: Run
* Hold Key `SPACE`: Jump
* Key `F`: Shoot
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] ADD - Moving platforms
- [x] ADD - Traps
- [x] UPD - The game will end when all the enemies are defeated and all coins are collected
- [ ] ADD - Loading screen
- [x] ADD - Defeat animations (players & enemies)
- [ ] ADD - Level editor
- [ ] ADD - Wider levels (beyond the screen)

Moew features in progress!


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, or found some bugs, please let me know as an issue in this repo!<br/><br/>
_Don't forget to give the project a star! Thanks again!_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Juan Pablo Bianchi - juampibianchi065@gmail.com

Project Link: [https://github.com/JuanBianchi/TheEvilGuestPYGAME](https://github.com/JuanBianchi/TheEvilGuestPYGAME)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[linedin_img]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin_link]: https://www.linkedin.com/in/juan-pablo-bianchi/
[github_img]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github_link]: https://github.com/JuanBianchi/
[python_img]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python_url]: https://www.python.org/
[pygame_url]: https://www.pygame.org/

[sqlite_img]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[sqlite_url]: https://www.sqlite.org/index.html
