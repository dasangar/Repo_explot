/* 
    nvd.cpp
    DetExploit program file related to NVD.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#include "detexploit.hpp"

std::map<std::string, std::string> nvd_download_vulndata(HANDLE hStdout) {
    std::string Url = "";
    std::string str = "";
    std::vector<std::string> tmp;
    std::map<std::string, std::string> product_dict;
    std::cout << NVD_DOWNLOAD_INTRO << std::endl;
    for (int y = 2010; y < 2020; y++) {
        Url = "https://raw.githubusercontent.com/moppoi5168/VulnData/cf6e0e47cf14ee8866c7ddbd1bd9fb226779a3da/NVD-DETEXPLOIT/NVDVULN_";
        Url += std::to_string(y);
        Url += ".detexploit";
        URLDownloadToFile(0, Url.c_str(), _T("nvd_temp.xml"), 0, 0);
        std::ifstream ifs("nvd_temp.xml");
        while (getline(ifs, str)) {
            tmp = split(str, "/,/,/,/");
            try {
                product_dict[tmp[0]] = tmp[1];
            } catch (...) {
                continue;
            }
        }
    }
    std::cout << NVD_DOWNLOAD_SUCCESS << std::endl;
    std::cout << "===========================================================" << std::endl;
    return product_dict;
}

std::map<std::string, VulnInfo> nvd_scan(std::map<std::string, std::string> nvd_vulndata, std::map<std::string, std::string> installed) {
    std::map<std::string, VulnInfo> resultdict;
    std::string level = "";
    VulnInfo vinfo;
    for (auto fit = nvd_vulndata.begin(); fit != nvd_vulndata.end(); fit++) {
        for (auto nit = installed.begin(); nit != installed.end(); nit++) {
            if ((*fit).first == (*nit).first && (*fit).second == (*nit).second) {
                level = determine_severity(NVD, "NOEXT");
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
                std::cout << DETECT_USING_NVD << std::endl;
                std::cout << OBJECT_LEVEL << level << " >>" << std::endl;
                std::cout << "===========================================================" << std::endl;
            }
        }
    }
    return resultdict;
}
