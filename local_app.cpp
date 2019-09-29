/* 
    local_app.cpp
    DetExploit program file related to local application info.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#include "detexploit.hpp"

std::map<std::string, std::string> getapp_all() {
    std::map<std::string, std::string> data;
    std::map<std::string, std::string> wmi_data = getapp_from_wmi();
    std::map<std::string, std::string> hklm_data = getapp_from_hklm();
    std::map<std::string, std::string> hklmwow64_data = getapp_from_hklmwow64();
    std::map<std::string, std::string> hkcu_data = getapp_from_hkcu();
    data.insert(wmi_data.begin(), wmi_data.end());
    data.insert(wmi_data.begin(), hklm_data.end());
    data.insert(wmi_data.begin(), hklmwow64_data.end());
    data.insert(wmi_data.begin(), hkcu_data.end());
    return data;
}

std::map<std::string, std::string> getapp_from_wmi() {
    std::map<std::string, std::string> data;
    std::system("powershell.exe Get-WmiObject -class Win32_Product > WMIRET.detexploit");
    // ファイルを開いて中身をstd::stringに流し込む
    // NameとVersionだけ上手く取り出して、mapに入れる
    if (!(DeleteFileA("WMIRET.detexploit"))) {
        std::cout << "Warning: Failed to delete HKLMRET.detexploit" << std::endl;
    }
    return data;
}

std::map<std::string, std::string> getapp_from_hklm() {
    std::map<std::string, std::string> data;
    // reg query "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall" /s | findstr "DisplayName DisplayVersion"
    // DisplayNameより先にDisplayVersionが表示されることがある
    // DisplayNameが来る前にDisplayVersionが来たらそれを次DisplayNameが来るまで保持する感じで
    std::system("powershell.exe Get-WmiObject -class Win32_Product > HKLMRET.detexploit");
    // ファイルを開いて中身をstd::stringに流し込む
    // for文を回して上に書いていた機構を実装する
    if (!(DeleteFileA("HKLMRET.detexploit"))) {
        std::cout << "Warning: Failed to delete HKLMRET.detexploit" << std::endl;
    }
    return data;
}

std::map<std::string, std::string> getapp_from_hklmwow64() {
    std::map<std::string, std::string> data;
    return data;
}

std::map<std::string, std::string> getapp_from_hkcu() {
    std::map<std::string, std::string> data;
    return data;
}
