#应该是对的，系统bug了     
        num_zeros = 0
        x = len(nums)
        for i in range(x):
            if nums[i-num_zeros] == 0:
                nums = nums[0:i-num_zeros] + nums[i-num_zeros+1:]
                nums.append(0)
                num_zeros += 1
        return None

#双指针（c++），个人感觉时间空间复杂度都跟我写的差不多。
 void moveZeroes(vector<int>& nums) {
        for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
        if (nums[cur] != 0) {
            swap(nums[lastNonZeroFoundAt++], nums[cur]);
        }
    }

    }
