class Nothing():
    def __del__(self):
        print("del Nothing")
a=Nothing()
b=Nothing()