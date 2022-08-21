#Learning about 2D arrays

TwoDe_array = [["Jeff",21,"League of Legends"],["Chad",23,"Apex Legends"],["Brad",19,"Minecraft"]]

print(TwoDe_array)

#print names only 
print(TwoDe_array[0][0]) #Jeff
print(TwoDe_array[1][0]) #Chad
print(TwoDe_array[2][0]) #Brad

#print age using negative
print(TwoDe_array[-3][-2]) #21
print(TwoDe_array[-2][-2]) #23
print(TwoDe_array[-1][-2]) #19

#print favorite games
print(TwoDe_array[-3][2]) #League Of Legends
print(TwoDe_array[-2][2]) #Apex Legends
print(TwoDe_array[-1][2]) #Minecraft