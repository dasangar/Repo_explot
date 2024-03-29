**This README is English version.**
**If you want to view Japanese version, please check the [README_JAPANESE.md](README_JAPANESE.md).**

<img src="banner.png" width="300">

[![GitHub Release](https://img.shields.io/github/release/detexploit/DetExploit.svg)](https://github.com/detexploit/DetExploit/releases/latest)
[![License: GPLv2](https://img.shields.io/badge/license-GPL--3.0-blue)](www.gnu.org/licenses/gpl-3.0.en.html)

## Info (Last Update: 2019/09/23)

Hi, thank you for visiting this repository.  
You may know that there is no commit for a while...... but development is still going on !!!  
Currently, I am re-writing whole program into C++ to reduce binary size and more advantages.  
This is very important procedure to release our program, so please understand it... :)  
I've prepared some milestone, so you may check out it!!  

```
Schedule

1. Python to C++ to resuce binary size
2. Release binary from GitHub Releases
3. Publish demo movies of client/server
4. Publish slides on DetExploit
```

## Table of contents

<!-- TOC -->

- [DetExploit v1.3α](#detexploit-v13α)
    - [Table of contents](#table-of-contents)
    - [Abstract](#abstract)
    - [Demo](#demo)
    - [Requirements](#requirements)
    - [How to run](#how-to-run)
    - [Supported Database](#supported-database)
    - [License](#license)
    - [Contact to developer](#contact-to-developer)

<!-- /TOC -->

## Abstract

DetExploit is software that detect vulnerable applications and not-installed important OS updates on the system, and notify them to user.

As we know, most of cyberattacks uses vulnerability that is released out year before.

I thought this is huge problem, and this kind of technology should be more powerful than technology that will detect unknown malwares or exploits.

Also this project is my theme of [Mitou Jr](https://jr.mitou.org/index_en.html) project in Japan.

I wish and work hard to make this an huge OSS (Open Source Software) project, to help these days society.

## Demo

+ Demo Video Clip (v0.5, English, Click and jump to YouTube to play video)

[![Alt text](https://img.youtube.com/vi/VBev9dtGtEM/0.jpg)](https://www.youtube.com/watch?v=VBev9dtGtEM)

## Requirements

+ Windows Platform (Tested on Windows 10)
+ Python 3.x (Tested on 3.7)
+ Modules written in requirements.txt (pip install -r requirements.txt)
+ [Win32Com (PyWin32: Python for Windows extensions)](https://github.com/mhammond/pywin32/releases)

## How to run

Executable Build is not available now.  
It is planned to be availble on stable release.

```
# Install requirements
C:\path\to\DetExlopit>pip install -r requirements.txt
# Move to src directory
C:\path\to\DetExlopit>cd src
# Run CUI version using python (PATH needs to be configured if not.)
C:\path\to\DetExlopit\src>python main.py
# Run GUI version using python (PATH needs to be configured if not.)
C:\path\to\DetExploit\src>python gui.py
```

## Supported Database

+ [ExploitDB](https://exploit-db.com/)
+ [JVN (Japan Vulnerability Notes)](https://jvn.jp/)
+ [NVD (National Vulnerability Database)](https://nvd.nist.gov/)
+ [US-CERT](https://www.us-cert.gov/)
+ [JPCERT](https://www.jpcert.or.jp/)
+ More on further version

## License

GNU GPLv3 License

## Contact to developer

+ MOPI (Email: [moppoi5168@gmail.com](mailto:moppoi5168@gmail.com) / Twitter: [@moppoi5168](https://twitter.com/moppoi5168))
