/* 
    jvn.cpp
    DetExploit program file related to JVN.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#include "detexploit.hpp"

std::map<std::string, std::string> jvn_download_vulndata(HANDLE hStdout) {
    std::map<std::string, std::string> product_dict;
    std::string Url = "";
    std::string str = "";
    std::cout << JVN_DOWNLOAD_INTRO << std::endl;
    std::cout << JVN_DOWNLOAD_ALERT_ONE << std::endl;
    std::cout << JVN_DOWNLOAD_ALERT_TWO << "\n\n";
    for (int y = 2019; y < 2020; y++) { // int y = 2010
        for (int m = 1; m < 13; m++) {
            Url = "https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=";
            Url += std::to_string(y);
            Url += "&datePublicStartM=";
            Url += std::to_string(m);
            Url += "&datePublicEmdY=";
            Url += std::to_string(y);
            Url += "&datePublicEmdM=";
            Url += std::to_string(m);
            URLDownloadToFile(0, Url.c_str(), _T("jvn_temp.xml"), 0, 0);
            std::ifstream ifs("jvn_temp.xml");
            while (getline(ifs, str)) {
                if (str.find("sec:cpe") != std::string::npos) {
                    std::vector<std::string> splitted = split(str.substr(6), " ");
                    try {
                        std::string name = splitted[3].substr(9);
                        std::string va = splitted[1].substr(9);
                        std::string version = va.erase(va.size() - 1);
                        product_dict[name] = version;
                    } catch (...) {
                        continue;
                    }
                }
            }
        }
        std::cout << JVN_DOWNLOAD_PROGRESS << std::to_string(y) << std::endl;
    }
    SetConsoleTextAttribute(hStdout, FOREGROUND_GREEN);
    std::cout << JVN_DOWNLOAD_SUCCESS << std::endl;
    SetConsoleTextAttribute(hStdout, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
    std::cout << "===========================================================" << std::endl;
    return product_dict;
}

std::map<std::string, VulnInfo> jvn_scan(std::map<std::string, std::string> jvn_vulndata, std::map<std::string, std::string> installed) {
    std::map<std::string, VulnInfo> resultdict;
    std::string level = "";
    VulnInfo vinfo;
    for (auto fit = jvn_vulndata.begin(); fit != jvn_vulndata.end(); fit++) {
        for (auto nit = installed.begin(); nit != installed.end(); nit++) {
            if ((*fit).first == (*nit).first && (*fit).second == (*nit).second) {
                level = determine_severity(JVN, "NOEXT");
                vinfo.version = (*fit).second;
                vinfo.is_edb = true;
                vinfo.is_jvn = false;
                vinfo.is_nvd = false;
                vinfo.is_winupd = false;
                vinfo.severity = level;
                resultdict[(*fit).first] = vinfo;
                std::cout << "===========================================================" << std::endl;
                std::cout << DETECT_ALERT << std::endl;
                std::cout << APP_NAME << (*fit).first << " >>" << std::endl;
                std::cout << APP_VERSION << (*fit).second << " >>" << std::endl;
                std::cout << DETECT_USING_JVN << std::endl;
                std::cout << OBJECT_LEVEL << level << " >>" << std::endl;
                std::cout << "===========================================================" << std::endl;
            }
        }
    }
    return resultdict;
}

