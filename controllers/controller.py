from models.chrome_web_driver import chr_driver

class controller:
    def __init__(self):
        self.web_driver = chr_driver()
    
    def open(self,to_open):
        self.web_driver.open(to_open)
    
    def end(self):
        self.web_driver.close()