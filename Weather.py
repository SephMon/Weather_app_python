class Weather:
    
    NAME = ["Gerry"]
    PASS = ["Cat"]
    DAY_OF_THE_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    MAX_LOGIN_ATTEMPTS = 3
    NUM_NUMS = 7
    #temps = []
    #rain_fall = []
    #humidity = []
    
    def __init__(self):
        self.temps = []
        self.rain_fall = []
        self.humidity = []
        
    def iterate(self):
        for i in Weather.DAY_OF_THE_WEEK:
            print(i)
        return i
        
    
    
        