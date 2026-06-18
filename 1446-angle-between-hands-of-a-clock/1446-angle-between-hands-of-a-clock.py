class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourHand = (60*hour+minutes)*0.5
        minuteHand = minutes*6

        angle = abs(hourHand-minuteHand)
        if angle<=180:
            return angle
        else:
            return 360-angle 

        