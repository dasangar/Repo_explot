/* 
    en_langdata.hpp
    English language pack of DetExploit.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#define WELCOME_MESSAGE "   Hello, W0rld!! Welcome to DetExploit v1.4-alpha :D"

/* Used in exploitdb.py */
#define EXPLOITDB_DOWNLOAD_INTRO "   Downloading vulnerability data from ExploitDB GitHub repo."
#define EXPLOITDB_DOWNLOAD_SUCCESS "   Download complete."
#define EXPLOITDB_DOWNLOAD_FAILED "   Error: ExploitDB vulnerability data download has failed!!!"
#define EXPLOITDB_EXTRACT_WIN "   Extracting Windows platform exploit from "
#define EXPLOITDB_EXTRACT_SUCCESS "   Extracted successfully."

/* Used in jvn.py */
#define JVN_DOWNLOAD_INTRO "   Downloading vulnerability data from JVN."
#define JVN_DOWNLOAD_ALERT_ONE "   This may need a long time to process."
#define JVN_DOWNLOAD_ALERT_TWO "   Do not exit the program."
#define JVN_DOWNLOAD_PROGRESS "   Successfully Downloaded: "
#define JVN_DOWNLOAD_SUCCESS "   Download complete."

/* Used in nvd.py */
#define NVD_DOWNLOAD_INTRO "   Downloading vulnerability data from NVD."
#define NVD_DOWNLOAD_SUCCESS "   Download complete."

/* Used in winupdate.py */
#define WINUPD_SCAN_INTRO "   Running update searcher script to gather not-installed update."

/* Used in * (Scan Phase) */
#define DETECT_ALERT "   << ALERT :: VULNERABLE APPLICATION DETECTED >>"
#define DETECT_UPDATE_ALERT "   << ALERT :: AVAILABLE WINDOWS UPDATE DETECTED >>"
#define APP_NAME "   << Application Name: "
#define APP_VERSION "   << Application Version:"
#define UPDATE_NAME "   << Update Name:  "
#define DETECT_USING_EXPLOITDB "   << Used database: ExploitDB >>"
#define DETECT_USING_JVN "   << Used database: Japan Vulnerability Notes >>"
#define DETECT_USING_NVD "   << Used database: National Vulnerability Database >>"
#define OBJECT_LEVEL "   << Level:"

/* Used in report.py */
#define LEVEL_DANGER "DANGER"
#define LEVEL_WARNING "WARNING"
#define LEVEL_CAUTION "CAUTION"
#define EDB "ExploitDB"
#define JVN "JVN"
#define NVD "NVD"
#define REPORT_FORMAT_READ_ERROR_ONE "Error: Scan report format detemination failed. (Check config.ini)"
#define REPORT_FORMAT_READ_ERROR_TWO "Error: Default value will be used (HTML)."
#define REPORT_OUTPUT_INFO_ONE "   Report has been saved at ../reports/detexploit_report_"
#define REPORT_OUTPUT_INFO_TWO " !!!"

/* GUI */
#define FIRST_MSG "Please click scan button to start."
#define OP_START "Operation has been started."
#define EXPLOITDB_EXTRACT_GUI "Extracting Windows vulnerability from data."
#define EXPLOITDB_PARSE "Parsing vulnerability data."
#define WMI_APP_RET "Retrieving application data from WMI."
#define REG_APP_RET "Retrieving application data from Windows Registry."
#define SCAN_MSG_ONE "Comparing fetched data and installed application list."
#define SCAN_MSG_TWO "Checking available Windows Updates."
#define SCAN_END "Done."
#define GEN_REPORT "Generating report in specified format."

#define RESONE "   RESULT: "
#define RESTWO " vulnerable application or update detected!!"

#define LANGPACK_SIGNATURE "DetExploit English LP"
