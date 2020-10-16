#include <bits/stdc++.h>
#include <math.h>

bool divChecker(int num) {
    for (int i = 1; i <= 9; i++) {
        if (num / (int)pow(10, 9 - i) % i != 0) return false;
    }
    return true;
}

void permute(std::string input, std::string output) {
    if (input.size() == 0 && divChecker(stoi(output))) {
        std::cout << "Number found! " << output << "0" << std::endl;
    }
    for (unsigned int i = 0; i < input.size(); i++) {
        permute(input.substr(1), output + input[0]);
        std::rotate(input.begin(), input.begin() + 1, input.end());
    }
}

int main() {
    permute("123456789", "");
}
