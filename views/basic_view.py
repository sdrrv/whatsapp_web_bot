from controllers.controller import controller

class basic_view:
    def __init__(self):
        self.controller= controller()
        self.controller.open("https://web.whatsapp.com/")
        while True:
            try:
                self.run()
            except Exception as e:
                print('\033[93m'+str(e)+'\033[0m')

    def run(self):
        line=input()
        command=line.split()

        if not line:
            self.controller.end()
            exit(0)
        
        if command[0] == "print":
            word= input(":")
            self.controller.printer(word,int(command[1]))