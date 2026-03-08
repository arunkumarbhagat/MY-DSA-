#include <vector>
using namespace std;

class Solution {
public:
    void findCombinations(int index, int target, vector<int>& arr, vector<vector<int>>& ans, vector<int>& ds) {
        if (index == arr.size()) {
            if (target == 0) {
                ans.push_back(ds);
            }
            return;
        }

        // Pick the element (if it's less than or equal to target)
        if (arr[index] <= target) {
            ds.push_back(arr[index]);
            // Notice we don't do 'index + 1' here because we can reuse the same element
            findCombinations(index, target - arr[index], arr, ans, ds);
            ds.pop_back(); // Backtrack
        }

        // Don't pick the element
        findCombinations(index + 1, target, arr, ans, ds);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> ds;
        findCombinations(0, target, candidates, ans, ds);
        return ans;
    }
};