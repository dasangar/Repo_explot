i686-w64-mingw32-g++ -c main.cpp -o main.detexploit -I./include
i686-w64-mingw32-g++ -c exploitdb.cpp -o exploitdb.detexploit -I./include
i686-w64-mingw32-g++ -c jvn.cpp -o jvn.detexploit -I./include
i686-w64-mingw32-g++ -c nvd.cpp -o nvd.detexploit -I./include
i686-w64-mingw32-g++ -c winupdate.cpp -o winupdate.detexploit -I./include
i686-w64-mingw32-g++ -c utils.cpp -o utils.detexploit -I./include
i686-w64-mingw32-g++ -c report.cpp -o report.detexploit -I./include
i686-w64-mingw32-g++ -c local_app.cpp -o local_app.detexploit -I./include
i686-w64-mingw32-g++ -c INIReader/INIReader.cpp -o INIReader.detexploit -I./include
i686-w64-mingw32-gcc -c INIReader/ini.c -o ini.detexploit -I./include
i686-w64-mingw32-g++ -std=c++11 main.detexploit exploitdb.detexploit jvn.detexploit nvd.detexploit winupdate.detexploit utils.detexploit report.detexploit local_app.detexploit INIReader.detexploit ini.detexploit -o DetExploit.exe -s -lws2_32 -lurlmon -lwininet -Wno-write-strings -I./include -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc
rm *.detexploit