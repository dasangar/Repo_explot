/* 
    main.cpp
    Main C++ program file of DetExploit.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#include "detexploit.hpp"

int main(int argc, char *argv[]) {
    INIReader cp = init_cp(argv[1]);
    std::cout << cp.Get("jvn", "data_from", "0000") << std::endl;
    int count = 0;
    char scan_starttime[128] = "";
    char scan_endtime[128] = "";
    HANDLE hStdout;
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    hStdout = GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleScreenBufferInfo(hStdout, &csbi);
    SetConsoleTextAttribute(hStdout, FOREGROUND_RED);
    std::cout << R"(
    ____       _   _____            _       _ _   
   |  _ \  ___| |_| ____|_  ___ __ | | ___ (_) |_ 
   | | | |/ _ \ __|  _| \ \/ / '_ \| |/ _ \| | __|
   | |_| |  __/ |_| |___ >  <| |_) | | (_) | | |_ 
   |____/ \___|\__|_____/_/\_\ .__/|_|\___/|_|\__|
                             |_|                  
    )" << std::endl;
    SetConsoleTextAttribute(hStdout, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
    std::cout << "===========================================================" << std::endl;
    std::cout << WELCOME_MESSAGE << std::endl;
    std::cout << "===========================================================" << std::endl;

    time_t start = time(NULL);
    struct tm *pstart = localtime(&start);
    sprintf(scan_starttime, "%d/%d/%d %d:%d:%d", pstart->tm_year+1900, pstart->tm_mon+1, pstart->tm_mday, pstart->tm_hour, pstart->tm_min, pstart->tm_sec);
    std::string stime_str = std::string(scan_starttime);
    std::string session_id = base64_encode(reinterpret_cast<const unsigned char*>(stime_str.c_str()), stime_str.length());

    std::map<std::string, std::string> edb_vulndata = proc_edb(hStdout);
    std::map<std::string, std::string> jvn_vulndata = jvn_download_vulndata(hStdout);
    std::map<std::string, std::string> nvd_vulndata = nvd_download_vulndata(hStdout);

    std::map<std::string, std::string> installed = getapp_all();

    std::map<std::string, VulnInfo> result;

    std::map<std::string, VulnInfo> scanret_exploitdb = edb_scan(edb_vulndata, installed);
    std::map<std::string, VulnInfo> scanret_jvn = jvn_scan(jvn_vulndata, installed);
    std::map<std::string, VulnInfo> scanret_nvd = nvd_scan(nvd_vulndata, installed);
    // std::map<std::string, VulnInfo> scanret_winupdate = windowsupdate_scan();

    result.insert(scanret_exploitdb.begin(), scanret_exploitdb.end());
    result.insert(scanret_jvn.begin(), scanret_jvn.end());
    result.insert(scanret_nvd.begin(), scanret_nvd.end());
    // result.insert(scanret_winupdate.begin(), scanret_winupdate.end());

    time_t end = time(NULL);
    struct tm *pend = localtime(&end);
    sprintf(scan_endtime, "%d/%d/%d %d:%d:%d", pend->tm_year+1900, pend->tm_mon+1, pend->tm_mday, pend->tm_hour, pend->tm_min, pend->tm_sec);
    std::string history = "\n";
    history += "Session ID: " + session_id;
    history += "\n";
    history += "Scan started at: " + std::string(scan_starttime);
    history += "\n";
    history += "Scan ended at: " + std::string(scan_endtime);
    history += "\n";
    history += "Found vulnerable application and available update: " + std::to_string(count);
    history += "\n";
    history += "DetExploit Version: ";
    history += DETEXPLOIT_VERSION;
    history += "\n\n#####################################################################\n\n";
    std::ofstream writeFile;
    writeFile.open("history.detexploit");
    writeFile << history;

    generate_report(cp, session_id, std::string(scan_starttime), std::string(scan_endtime), result);

    SetConsoleTextAttribute(hStdout, FOREGROUND_RED);
    std::cout << "===========================================================" << std::endl;
    std::string resmsg = RESONE;
    resmsg += std::to_string(count);
    resmsg += RESTWO;
    std::cout << resmsg << std::endl;
    std::cout << "===========================================================" << std::endl;
    SetConsoleTextAttribute(hStdout, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
    
    return 0;
}

INIReader init_cp(char *arg) {
    INIReader cp(arg);
    if (cp.ParseError() < 0) {
        std::cout << "Error: Cannot parse this config file.\n" << std::endl;
        exit(1);
    }
    return cp;
}
