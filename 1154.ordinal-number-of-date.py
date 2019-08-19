class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(i) for i in date.split("-")]
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and year % 100 != 0:
            days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days_in_month[:month - 1]) + day
