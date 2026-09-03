class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] suf = new int[nums.length];
        for(int i = nums.length - 1, q = 1; i >= 0; i--){
            suf[i] = q;
            q = q * nums[i];
        }

        int[] res = new int[nums.length];
        for(int i = 0, p = 1; i < res.length; i++){
            res[i] = p * suf[i];
            p = p * nums[i];
        }

        return res;
    }
}  