/* 
    report.cpp
    DetExploit program file related to scan result report.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#include "detexploit.hpp"

std::string determine_severity(std::string data_src, std::string ext) {
    if (data_src == "ExploitDB") {
        std::string rv = LEVEL_DANGER;
        return rv;
    } else if (data_src == "WinUpdate") {
        if (ext == "NOEXT" || ext.find("KB") == std::string::npos) {
            std::string rv = LEVEL_WARNING;
            return rv;
        }
        /* TODO: Retrieve informations from Windows Update Catalog, to determine update is important or not. */
        std::string rv = LEVEL_WARNING;
        return rv;
    } else if (data_src == "JVN") {
        std::string rv = LEVEL_CAUTION;
        return rv;
    } else if (data_src == "NVD") {
        std::string rv = LEVEL_CAUTION;
        return rv;
    } else {
        std::string rv = "Error";
        return rv;
    }
}

void generate_report(INIReader cp, std::string session_id, std::string scan_starttime, std::string scan_endtime, std::map<std::string, VulnInfo> resultdict) {
    std::string rformat = std::string(cp.Get("general", "report_format", "HTML"));
    std::string hostname = ghostname();
    std::string templ = "";
    if (rformat == "HTML") {
        std::ifstream ifs("resources/report_template.html");
        if (ifs.fail()) {
            std::cerr << "Error: Cannot load resources/report_template.html" << std::endl;
            exit(1);
        }
        std::string templ((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    } else if (rformat == "Markdown") {
        std::ifstream ifs("resources/report_template.md");
        if (ifs.fail()) {
            std::cerr << "Error: Cannot load resources/report_template.md" << std::endl;
            exit(1);
        }
        std::string templ((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    } else if (rformat == "PlainText") {
        std::ifstream ifs("resources/report_template.txt");
        if (ifs.fail()) {
            std::cerr << "Error: Cannot load resources/report_template.txt" << std::endl;
            exit(1);
        }
        std::string templ((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    } else {
        std::cout << REPORT_FORMAT_READ_ERROR_ONE << std::endl;
        std::cout << REPORT_FORMAT_READ_ERROR_TWO << std::endl;
        std::ifstream ifs("resources/report_template.html");
        if (ifs.fail()) {
            std::cerr << "Error: Cannot load resources/report_template.html" << std::endl;
            exit(1);
        }
        std::string templ((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    }
    std::string row = "";
    std::string detect_using_exploitdb = "";
    std::string attack_code_exists = "";
    std::string detect_using_jvn = "";
    std::string detect_using_nvd = "";
    std::string is_windows_update = "";
    std::string tdid = "";
    for (auto it = resultdict.begin(); it != resultdict.end(); it++) {
        VulnInfo vuln_i = (*it).second;
        std::string app_name = (*it).first;
        std::string app_version = vuln_i.version;
        if ((*it).second.is_edb) {
            detect_using_exploitdb = "〇";
            attack_code_exists = "〇";
        } else {
            detect_using_exploitdb = "×";
            attack_code_exists = "Unknown";
        }
        if ((*it).second.is_jvn) {
            detect_using_jvn = "〇";
        } else {
            detect_using_jvn = "×";
        }
        if ((*it).second.is_nvd) {
            detect_using_nvd = "〇";
        } else {
            detect_using_nvd = "×";
        }
        if ((*it).second.is_winupd) {
            is_windows_update = "〇";
        } else {
            is_windows_update = "×";
        }
        if ((*it).second.severity == "DANGER") {
            tdid = "danger";
        } else if ((*it).second.severity == "WARINING") {
            tdid = "warning";
        } else if ((*it).second.severity == "CAUTION") {
            tdid = "caution";
        } else {
            tdid = "unknown";
        }
        std::string ext = "";
        std::string conts = "";
        if (rformat == "PlainText") {
            ext = ".txt";
            conts = "!!CONTS_PlainText!!";
            // conts{boost::format("\n            [%1% v%2%] - %3%\n            Detected using ExploitDB: %4%\n            Detected using JVN: %5%\n            Detected using NVD: %6%\n            Is it Windows Update: %7%\n            Attack Code Existence: %8%\n            ") % app_name % app_version % (*it).second.severity % detect_using_exploitdb % detect_using_jvn % detect_using_nvd % is_windows_update % attack_code_exists};
            row = row + conts;
        } else if (rformat == "Markdown") {
            ext = ".md";
            conts = "!!CONTS_Markdown!!";
            // conts{boost::format("\n            ### %1% v%2%\n            - Level: %3%\n            - Detected by ExploitDB: %4%\n            - Detected by JVN: %5%\n            - Detected by NVD: %6%\n            - Is it Windows Update: %7%\n            - Attack Code Existence: %8%\n            ") % app_name % app_version % (*it).second.severity % detect_using_exploitdb % detect_using_jvn % detect_using_nvd % is_windows_update % attack_code_exists};
            row = row + conts;
        } else {
            ext = ".html";
            conts = "!!CONTS_HTML!!";
            // conts{boost::format("\n            <tr>\n                <td id=\"%1%\">%2%</td>\n                <td id=\"vulnapp_name\">%3%</td>\n                <td id=\"vulnapp_version\">%4%</td>\n                <td id=\"vulnapp_exploitdb\">%5%</td>\n                <td id=\"vulnapp_jvn\">%6%</td>\n                <td id=\"vulnapp_nvd\">%7%</td>\n                <td id=\"vulnupdate\">%8%</td>\n                <td id=\"vulnapp_attackcode\">%9%</td>\n            </tr>\n            ") % tdid % (*it).second.severity % app_name % app_version % detect_using_exploitdb % detect_using_jvn % detect_using_nvd % is_windows_update % attack_code_exists};
            row = row + conts;
        }
        // std::string report = boost::format(templ) % DETEXPLOIT_VERSION % hostname % scan_starttime % scan_endtime % "NOTAVAIL" % session_id % LANGPACK_SIGNATURE % row;
        std::string report = "!!REPORT!!" + conts;
        std::string filename = "detexploit_report_" + session_id + ext;
        std::ofstream rfile;
        rfile.open(filename, std::ios::out);
        if (!rfile) {
            std::cout << "Error: Cannot generate report. Please check permission settings, and retry." << std::endl;
            exit(1);
        }
        rfile << report << std::endl;
    }
}
