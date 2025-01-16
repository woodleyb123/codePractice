class Gravity:
    def falling(time, velo):
        a = 9.8
        return velo * time + 0.5 * a * time * time
    
print(Gravity.falling(3, 5))