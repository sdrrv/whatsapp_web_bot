from models.chrome_web_driver import chr_driver

class controller:
    def __init__(self):
        self.web_driver = chr_driver()
    
    def open(self,to_open):
        self.web_driver.get_driver().get(to_open)
    
    def end(self):
        self.web_driver.close()
    
    def printer(self,word,times):
        for i in range(times):
            tmp= self.web_driver.get_driver().find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            tmp.send_keys(word)
            tmp.send_keys("\n")
