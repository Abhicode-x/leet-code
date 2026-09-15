class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty())
            return {};

        vector<string> mp = {
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        vector<string> ans;

        function<void(int, string)> backtrack = [&](int index, string current) {
            if (index == digits.size()) {
                ans.push_back(current);
                return;
            }

            string letters = mp[digits[index] - '0'];

            for (char c : letters) {
                current.push_back(c);
                backtrack(index + 1, current);
                current.pop_back();
            }
        };

        backtrack(0, "");

        return ans;
    }
};