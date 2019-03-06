def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice ={}
        for i,v in enumerate(nums):
            if v in indice:
                return [indice[v],i]
            indice [target-v] = i
        