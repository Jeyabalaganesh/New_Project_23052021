class carmodel:

    def __init__(self,car, what, capa, fuel_type = "Diesel"):
        self.model =car
        self.type = what
        self.cc = capa
        self.fuel = fuel_type

    # def Setdata(self, car, what, capa):
    #     self.model =car
    #     self.type = what
    #     self.cc = capa

    def Printdata(self):
        print("{0},{1},{2}:{3}".format(self.model, self.type, self.cc, self.fuel))

tiago = carmodel("Tiagao", "HB", "1000", "Petrol")
tiago.Printdata()
tiago = carmodel("KUV", "HB", "1000")
tiago.Printdata()