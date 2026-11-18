class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        
        for(int i = nums.length - 1, q = 1; i >= 0; i--){
            res[i] = q;
            q = q * nums[i];
        }

        for(int i = 0, p = 1; i < res.length; i++){
            res[i] = p * res[i];
            p = p * nums[i];
        }

        return res;
    }
}  