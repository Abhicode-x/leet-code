class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ans;

        if (s.empty() || words.empty())
            return ans;

        int wordLen = words[0].size();
        int wordCount = words.size();
        int totalLen = wordLen * wordCount;

        if (s.size() < totalLen)
            return ans;

        unordered_map<string, int> target;

        for (string word : words)
            target[word]++;

        for (int offset = 0; offset < wordLen; offset++) {
            int left = offset;
            int right = offset;
            int count = 0;

            unordered_map<string, int> current;

            while (right + wordLen <= s.size()) {
                string word = s.substr(right, wordLen);
                right += wordLen;

                if (target.find(word) != target.end()) {
                    current[word]++;
                    count++;

                    while (current[word] > target[word]) {
                        string leftWord = s.substr(left, wordLen);
                        current[leftWord]--;
                        left += wordLen;
                        count--;
                    }

                    if (count == wordCount) {
                        ans.push_back(left);

                        string leftWord = s.substr(left, wordLen);
                        current[leftWord]--;
                        left += wordLen;
                        count--;
                    }
                }
                else {
                    current.clear();
                    count = 0;
                    left = right;
                }
            }
        }

        return ans;
    }
};