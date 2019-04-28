# DetExploit v0.5 (Alpha Version)

![ScreenShot1](sshot.png)

+ Demo Video Clip (v0.5, English, Click to play)

[![Alt text](https://img.youtube.com/vi/VBev9dtGtEM/0.jpg)](https://www.youtube.com/watch?v=VBev9dtGtEM)

+ デモ映像 (v0.5, 日本語, クリックするとYouTubeにジャンプします))

[![Alt text](https://img.youtube.com/vi/aIMhaA_ysUY/0.jpg)](https://www.youtube.com/watch?v=aIMhaA_ysUY)

## Abstract

DetExploit is software that detect vulnerable applications on the system, and notify them to user.

As we know, most of cyberattacks uses vulnerability that is released out year before.

I thought this is huge problem, and this kind of technology should be more powerful than technology that will detect unknown malwares or exploits.

Also this project is also planned to be my theme of Mitou Jr project in Japan.

I wish and work hard to make this an huge OSS (Open Source Software) project, to help these days society.

## Requirements

+ Windows Platform (Tested on Windows 10)
+ Python 3.x (Tested on 3.7)
+ Modules written in requirements.txt (pip install -r requirements.txt)
+ [Win32Com (PyWin32: Python for Windows extensions)](https://github.com/mhammond/pywin32/releases)

## How to run

```
# Install requirements
C:\path\to\detexlopit>pip install -r requirements.txt
# Run CUI version by python (PATH needs to be configured if not.)
C:\path\to\detexlopit>python main.py
# Run GUI version by python (PATH needs to be configured if not.)
C:\path\to\detexploit>python gui.py
```

## How to run (for MSYS2:mintty Users, EXPERIMENTAL)

Copy following to .bashrc (or something like .zshrc).

```
# Easy Setup Script for DetExploit
# Remember to replace example path to real path

envsetup () {
    winpty /PATH/TO/PIP/pip.exe install -r ~/PATH/TO/DETEXPLOIT/DetExploit/requirements.txt
    wget https://github.com/mhammond/pywin32/releases/download/b224/pywin32-224.win-amd64-py3.7.exe
    pywin32 = "$(pwd)/pywin32-224.win-amd64-py3.7.exe"
    winpty ${pywin32}
}

alias envsetup_dexploit=envsetup
alias run_dexploit='winpty /PATH/TO/PYTHON/python.exe ~/PATH/TO/DETEXPLOIT/DetExploit/main.py'
```

Then execute 'envsetup_dexploit' for environment setup, and execute 'run_dexploit' to run DetExploit. :>

## Supported Database

+ [ExploitDB](exploit-db.com/)
+ [JVN (Japan Vulnerability Notes)](https://jvn.jp/)

## License

GPL License

## Contact to developer

+ MOPI (Email: moppoi5168@gmail.com / Twitter: @naogramer)

