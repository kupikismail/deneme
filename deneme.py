class Date:   
    def __init__(self,Year,Month,Day):   
        self._Year=1970   
        self._Month= 1   
        self._Day=1    
        self.set_date(Year,Month,Day)   
 
    def set_date(self,Year,Month,Day):   
        if Year > 0 and Month >0 and Month <= 12 and Day <= 31 and Day >0:   
            self._Year=Year   
            self._Month = Month   
            self._Day = Day    
        else:   
            print("Invalid value")   
    def print(self):   
        print("The date is: {}/{}/{}".format(self._Day,self._Month,self._Year))   

class Movie:
    def __init__(self,name,release_year,release_month,release_day) ->None:
        self._name = name
        #Böyle de yapabiliriz ama date fonksiyonu varken gerek yok
        #self._releaseyear = release_year
        #self._releasemonth = release_month
        #self._releaseday = release_day
        self._ReleaseDate = Date(release_year,release_month,release_day)

    def print(self):
        # Violation of data encapsulation principle: _Year should not be accessed from outside of Date class, burada self._ReleaseDate._Year kullanmamız bu Date classına ait olduğu için ve _ kullanıldığı için violate encapsulation ama Date'den fonksiyon çağırırsak sorun yok. 
        #print("Movie " + self._name + " was released on "+ str(self._ReleaseDate._Year))
        print("Movie "+ self._name + "was released on ")
        self._ReleaseDate.print()

        
m = Movie("The matrix ",2021,12,15)
m.print()
m2 = Movie("The Dune ",2021,9,15)
m2.print()