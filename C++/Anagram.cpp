#include <iostream>
#include <algorithm>

bool areAnagrams(std::string str1, std::string str2) {
    if (str1.length() != str2.length())
        return false;

    std::sort(str1.begin(), str1.end());
    std::sort(str2.begin(), str2.end());

    return str1 == str2;
}

int main() {
    std::string str1 = "listen";
    std::string str2 = "silent";

    if (areAnagrams(str1, str2))
        std::cout << "The strings are anagrams." << std::endl;
    else
        std::cout << "The strings are not anagrams." << std::endl;

    return 0;
}
