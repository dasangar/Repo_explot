/* 
    utils.cpp
    DetExploit program file for utilities used in entire program.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#define MAX_KEY_LENGTH 255
#define MAX_VALUE_NAME 16383

#include "detexploit.hpp"

static const std::string base64_chars = 
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "abcdefghijklmnopqrstuvwxyz"
             "0123456789+/";

std::string ghostname() {
    char hostname[256];
    DWORD hostnameLength = 256;
    GetComputerName(hostname, &hostnameLength);
    return std::string(hostname);
}

bool checkFileExistence(const std::string& str) {
    std::ifstream ifs(str);
    return ifs.is_open();
}

std::vector<std::string> split(const std::string& src, const char* delim) {
    std::vector<std::string> vec;
    std::string::size_type len = src.length();

    for (std::string::size_type i = 0, n; i < len; i = n + 1) {
        n = src.find_first_of(delim, i);
        if (n == std::string::npos) {
            n = len;
        }
        vec.push_back(src.substr(i, n - i));
    }

    return vec;
}

std::string join(const std::vector<std::string>& v, const char* delim) {
  std::string s = "";
  if (!v.empty()) {
    s += v[0];
    for (decltype(v.size()) i = 1, c = v.size(); i < c; ++i) {
      if (delim) s += delim;
      s += v[i];
    }
  }
  return s;
}

std::string base64_encode(unsigned char const* bytes_to_encode, unsigned int in_len) {
    std::string ret = "";
    int i = 0;
    int j = 0;
    unsigned char char_array_3[3];
    unsigned char char_array_4[4];

    while (in_len--) {
        char_array_3[i++] = *(bytes_to_encode++);
        if (i == 3) {
            char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
            char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
            char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
            char_array_4[3] = char_array_3[2] & 0x3f;
            for(i = 0; (i <4) ; i++)
                ret += base64_chars[char_array_4[i]];
            i = 0;
        }
    }
    if (i) {
        for(j = i; j < 3; j++)
            char_array_3[j] = '\0';
        char_array_4[0] = ( char_array_3[0] & 0xfc) >> 2;
        char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
        char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
        for (j = 0; (j < i + 1); j++)
            ret += base64_chars[char_array_4[j]];
        while((i++ < 3))
            ret += '=';
    }
    return ret;
}

bool config_test() {
    return false;
}
