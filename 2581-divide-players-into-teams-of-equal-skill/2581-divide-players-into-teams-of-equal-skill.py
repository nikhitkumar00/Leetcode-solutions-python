class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        chemistry = skill[0] * skill[-1]

        for i in range(1, len(skill) // 2):
            if target != skill[i] + skill[-i - 1]:
                return -1
            chemistry += skill[i] * skill[-i - 1]

        return chemistry
