#antglo 7/10/2023
#Still developing
#I intend for this program to contain a bunch of different conversion formulas/rates, I am using this for practice as I work towards my PCEP

#conversion for miles to kilometers
def miles_to_kilometers(miles):
    miles *= 1.609
    miles_converted = miles
    print(round(init_miles, 2), "miles is equal to:",  round(miles_converted, 2), "kilometers.")
    
#conversion for kilometers to miles
def kilometeters_to_miles(km):
    km /= 1.609
    km_converted = km
    print(round(init_km, 2), "kilometers is equal to:", round(km_converted, 2), "miles.")
    
#conversion for feet to miles
def feet_to_miles(ft):
    ft /= 5280
    ft_converted = ft
    print(round(init_ft, 3), "feet is equal to:", round(ft_converted, 3), "miles")
    
#conversion for miles to feet
def miles_to_feet(miles_2_ft):
    miles_2_ft *= 5280
    m_2_ft_converted = miles_2_ft
    print(round(init_miles_2_ft, 2), "miles is equal to:", round(m_2_ft_converted, 2), "feet")
    

if __name__ == "__main__":
    #init_km = float(input("Enter the amount of km you would like to convert: "))
    # miles_to_kilometers(init_miles)
    init_miles_2_ft = float(input("Enter the amount of miles: "))
    miles_to_feet(init_miles_2_ft)