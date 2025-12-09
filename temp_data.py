class Temperature:

    def __init__(self, name, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec):
        self.name = name
        self.jan = jan
        self.feb = feb
        self.mar = mar
        self.apr = apr
        self.may = may
        self.jun = jun
        self.jul = jul
        self.aug = aug
        self.sep = sep
        self.oct = oct
        self.nov = nov
        self.dec = dec

alabama = Temperature("AL", 43.3, 52.7, 58.0, 64.2, 74.0, 79.0, 81.0, 80.9, 75.5, 66.4, 61.3, 48.3)
alaska = Temperature("AK", 3.2, 11.1, 14.3, 27.6, 38.3, 52.8, 52.8, 49.6, 42.2, 27.7, 13.5, 13.8)
arizona = Temperature("AZ", 42.1, 46.7, 49.8, 58.0, 66.5, 80.3, 84.5, 81.4, 76.4, 68.0, 48.4, 47.8)
arkansas = Temperature("AR", 36.1, 51.8, 55.3, 63.3, 72.8, 78.3, 79.7, 80.5, 73.4, 66.0, 56.5, 46.3)
california = Temperature("CA", 45.7, 46.4, 48.8, 55.2, 63.0, 74.0, 81.5, 76.1, 72.6, 65.5, 48.4, 48.4)
colorado = Temperature("CO", 24.7, 32.1, 36.2, 45.3, 51.4, 66.8, 68.3, 67.9, 61.7, 52.8, 33.1, 32.0)
connecticut = Temperature("CT", 31.2, 33.3, 42.3, 48.2, 61.0, 69.8, 74.4, 70.0, 63.5, 54.0, 45.8, 31.4)
delaware = Temperature("DE", 37.4, 39.6, 48.1, 55.7, 65.0, 74.8, 78.8, 75.0, 69.1, 59.2, 50.9, 38.3)
florida = Temperature("FL", 58.8, 60.6, 68.4, 70.4, 79.7, 82.6, 84.2, 83.7, 81.4, 74.4, 70.0, 60.7)
georgia = Temperature("GA", 46.2, 52.5, 59.3, 65.1, 73.6, 79.6, 82.0, 80.4, 75.3, 66.5, 61.5, 49.0)
hawaii = Temperature("HI", 64.8, 62.3, 63.7, 65.4, 66.5, 68.2, 69.1, 69.9, 69.4, 68.7, 66.7, 66.2)
idaho = Temperature("ID", 25.4, 30.5, 33.8, 42.3, 47.1, 60.2, 69.4, 65.6, 59.5, 48.4, 31.7, 30.2)
illinois = Temperature("IL", 26.5, 40.6, 46.8, 54.7, 67.0, 74.5, 74.0, 73.6, 68.7, 58.7, 46.6, 34.0)
indiana = Temperature("IN", 27.7, 39.6, 46.3, 54.8, 66.6, 72.9, 73.2, 73.1, 68.5, 57.7, 47.4, 34.6)
iowa = Temperature("IA", 20.1, 37.0, 40.6, 50.8, 62.1, 72.0, 72.2, 71.1, 66.7, 56.7, 40.5, 28.2)
kansas = Temperature("KS", 25.9, 43.8, 47.0, 57.2, 65.4, 77.2, 78.0, 77.7, 71.2, 62.5, 46.4, 38.1)
kentucky = Temperature("KY", 32.9, 45.2, 50.6, 59.2, 68.2, 74.4, 77.0, 75.5, 70.7, 59.9, 51.9, 40.2)
louisiana = Temperature("LA", 47.2, 57.8, 61.9, 69.1, 77.3, 81.6, 82.7, 84.2, 78.0, 70.8, 66.0, 55.4)
maine = Temperature("ME", 20.3, 23.7, 32.3, 40.7, 55.3, 63.9, 69.6, 65.5, 59.2, 47.6, 38.7, 22.9)
maryland = Temperature("MD", 36.6, 40.4, 48.3, 56.7, 66.0, 74.8, 79.1, 75.0, 68.6, 58.3, 50.5, 37.6)
massachusetts = Temperature("MA", 30.1, 32.8, 40.5, 47.2, 59.9, 68.9, 74.4, 69.4, 63.0, 52.5, 44.8, 30.7)
michigan = Temperature("MI", 24.4, 31.9, 36.5, 46.3, 58.2, 66.0, 68.9, 67.9, 63.9, 52.2, 41.3, 27.9)
minnesota = Temperature("MN", 15.5, 28.2, 30.6, 44.4, 56.4, 64.4, 69.8, 67.2, 65.1, 51.3, 33.8, 19.6)
mississippi = Temperature("MS", 42.6, 54.3, 58.4, 65.6, 75.4, 80.1, 82.1, 82.0, 76.0, 67.6, 62.4, 50.2)
missouri = Temperature("MO", 27.8, 45.3, 49.9, 58.6, 68.0, 75.8, 76.1, 75.8, 69.9, 61.4, 48.8, 37.9)
montana = Temperature("MT", 17.8, 28.1, 30.8, 43.6, 48.8, 58.9, 69.4, 65.8, 61.0, 48.4, 30.6, 28.8)
nebraska = Temperature("NE", 20.4, 37.9, 40.2, 50.1, 59.4, 71.5, 73.4, 73.1, 68.6, 56.2, 39.8, 33.0)
nevada = Temperature("NV", 34.3, 36.3, 39.9, 48.4, 55.3, 70.8, 77.2, 72.4, 65.8, 56.1, 37.0, 37.6)
new_hampshire = Temperature("NH", 24.7, 27.4, 35.2, 43.1, 57.4, 65.6, 71.4, 65.9, 59.9, 48.3, 40.0, 24.7)
new_jersey = Temperature("NJ", 34.7, 37.3, 46.0, 52.6, 63.6, 73.4, 77.8, 73.8, 66.8, 57.5, 49.0, 35.0)
new_mexico = Temperature("NM", 34.9, 41.6, 45.4, 53.2, 62.4, 74.8, 74.7, 75.2, 67.5, 60.7, 43.5, 40.8)
new_york = Temperature("NY", 26.6, 30.4, 37.5, 45.9, 60.0, 66.6, 71.2, 67.3, 62.3, 50.5, 41.6, 27.0)
north_carolina = Temperature("NC", 41.8, 46.8, 53.8, 61.0, 69.2, 75.6, 78.8, 75.8, 71.1, 61.2, 54.9, 43.6)
north_dakota = Temperature("ND", 12.4, 27.0, 25.8, 43.9, 54.0, 62.7, 70.8, 66.9, 64.9, 49.7, 29.2, 18.0)
ohio = Temperature("OH", 29.9, 39.0, 44.8, 54.8, 65.8, 71.8, 73.7, 73.0, 68.2, 56.3, 47.2, 34.6)
oklahoma = Temperature("OK", 33.9, 49.8, 54.3, 62.7, 70.7, 80.3, 81.4, 83.4, 74.8, 68.1, 53.3, 45.1)
oregon = Temperature("OR", 34.1, 36.7, 39.2, 44.7, 50.2, 60.6, 71.2, 65.6, 61.4, 50.8, 37.3, 36.6)
pennsylvania = Temperature("PA", 30.0, 35.2, 42.1, 50.8, 62.3, 69.1, 73.4, 69.6, 64.0, 53.1, 44.4, 31.0)
rhode_island = Temperature("RI", 32.3, 33.9, 42.5, 47.9, 59.1, 69.1, 74.3, 70.4, 63.7, 54.7, 46.8, 33.7)
south_carolina = Temperature("SC", 45.8, 50.6, 58.0, 64.4, 72.7, 78.6, 82.0, 79.1, 74.8, 64.8, 59.5, 47.5)
south_dakota = Temperature("SD", 16.4, 32.7, 34.1, 46.5, 56.5, 66.9, 72.9, 70.7, 68.2, 53.6, 34.3, 26.4)
tennessee = Temperature("TN", 34.8, 47.8, 52.9, 60.5, 69.4, 75.5, 78.3, 76.7, 71.4, 61.6, 54.8, 42.9)
texas = Temperature("TX", 44.3, 56.2, 60.4, 67.9, 76.9, 83.2, 82.8, 85.8, 77.5, 72.8, 60.8, 54.2)
utah = Temperature("UT", 29.9, 34.1, 38.8, 48.1, 53.7, 70.8, 75.2, 72.2, 65.5, 55.7, 34.8, 33.7)
vermont = Temperature("VT", 23.4, 26.7, 33.8, 42.3, 57.7, 64.8, 70.5, 65.6, 60.0, 48.1, 38.5, 23.5)
virginia = Temperature("VA", 37.1, 42.9, 50.1, 58.3, 66.6, 73.8, 77.5, 74.4, 68.2, 58.4, 51.5, 38.8)
washington = Temperature("WA", 30.0, 36.6, 40.6, 45.3, 51.2, 58.3, 69.4, 65.5, 61.8, 48.5, 38.1, 35.1)
west_virginia = Temperature("WV", 32.1, 40.8, 46.9, 55.9, 64.8, 70.2, 74.3, 72.1, 66.6, 55.3, 48.1, 35.4)
wisconsin = Temperature("WI", 21.0, 31.4, 35.2, 45.3, 57.7, 65.6, 68.8, 67.8, 64.0, 52.1, 38.3, 23.6)
wyoming = Temperature("WY", 20.1, 27.9, 32.2, 41.4, 46.5, 62.2, 66.7, 65.6, 60.1, 48.8, 30.0, 29.2)

states = [alabama, alaska, arizona, arkansas, california,colorado, connecticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachusetts, michigan, minnesota, mississippi, missouri, montana, nebraska, nevada, new_hampshire, new_jersey, new_mexico, new_york, north_carolina, north_dakota, ohio, oklahoma, oregon, pennsylvania, rhode_island, south_carolina, south_dakota, tennessee, texas, utah, vermont, virginia, washington, west_virginia, wisconsin, wyoming]

def find_destination(destination):
    for item in states:
        if item.name in destination:
            return item
        
def get_temp(month, temp_set):
    
    if month == "January":
        return temp_set.jan
    if month == "February":
        return temp_set.feb
    if month == "March":
        return temp_set.mar
    if month == "April":
        return temp_set.apr
    if month == "May":
        return temp_set.may
    if month == "June":
        return temp_set.jun
    if month == "July":
        return temp_set.jul
    if month == "August":
        return temp_set.aug
    if month == "September":
        return temp_set.sep
    if month == "October":
        return temp_set.oct
    if month == "November":
        return temp_set.nov
    if month == "December":
        return temp_set.dec