class Solution {
public:
    string countAndSay(int n) {
        string result = "1";

        for (int i = 2; i <= n; i++) {
            string next = "";

            int j = 0;

            while (j < result.size()) {
                int count = 1;

                while (j + count < result.size() &&
                       result[j] == result[j + count]) {
                    count++;
                }

                next += to_string(count);
                next += result[j];

                j += count;
            }

            result = next;
        }

        return result;
    }
};