class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = sorted(zip(heights, names), reverse = True)
        return [names for heights, names in people]