import random
import copy

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for i in range(v)]
        self.cp = copy.copy(self.contents)
    
    def draw(self, num):
        list1 = self.contents
        list2 = self.cp
        c = False
        if num <= len(list1):
            c = True
            x = [list1.pop(list1.index(random.choice(list1))) for i in range(num)]
        elif (num > len(list1)) and c == True:
            list1 = copy.copy(list2)
            self.contents = list1
            x = [list1.pop(list1.index(random.choice(list1))) for i in range(num)]
        else:
            x = self.contents
        return x
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        x, y = {}, []
        drawn = hat.draw(num_balls_drawn)
        for item in drawn:
            x[item] = drawn.count(item)
        for key in expected_balls.keys():
            if key in x.keys():
                if expected_balls[key] <= x[key]:
                    y.append(True)
                else:
                    y.append(False)
            else:
                y.append(False)
        if all(y) == True:
            m += 1
        
    return (m / num_experiments)
