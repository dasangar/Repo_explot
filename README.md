# DetExploit v1.0α

![ScreenShot1](resources/sshot_v0.9-alpha.png)

** Screenshot of DetExploit v0.9α **

[日本語版のREADMEを表示 (View Japanese version README)](README_JAPANESE.md)

## Table of contents

<!-- TOC -->

- [DetExploit v1.0α](#detexploit-v10α)
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

Also this project is also planned to be my theme of [Mitou Jr](https://jr.mitou.org/) project in Japan.

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
+ More on further version

## License

GNU GPLv3 License

## Contact to developer

+ MOPI (Email: [moppoi5168@gmail.com](mailto:moppoi5168@gmail.com) / Twitter: [@naogramer](https://twitter.com/naogramer))
