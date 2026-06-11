class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> dif_map;
        int dif;

        for (int i = 0; i < nums.size(); i++) {
            dif = target - nums[i];
            if (dif_map.find(dif) != dif_map.end()) {
                return vector<int> {dif_map[dif], i};
            }
            else {
                dif_map[nums[i]] = i;
            }
        }
        return {};
    }
};