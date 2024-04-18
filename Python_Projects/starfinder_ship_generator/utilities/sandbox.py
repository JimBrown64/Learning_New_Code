import sqlite3
import sql_interactions as sql
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import app.bootup as bootup

def connect():
    con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return(con)

def createText():
    text =''
    for table in bootup.tableList:
        columns = '","'.join(bootup.tableList[table])
        newInsert = 'sql.tableInsert("'+ table+'","'+ columns+'","'+ columns+'",cur,con)\n'
        text = text + newInsert
    return text
file = open("Python_Projects/starfinder_ship_generator/utilities/inserts.txt", "w")
file.write( createText())
file.close()

# con = connect()
# cur = con.cursor()


# # sql.tableInsert("Frames",'"id","Name","Size","Maneuverability","HP","DT","CT","Expansion_Bays",\
#                 # "Minimum_Crew","Maximum_Crew","Cost"',
#                 # '1,"Racer",1,5,20,0,4,0,1,1,4',cur,con)
# # sql.tableInsert("Frames",'"id","Name","Size","Maneuverability","HP","DT","CT","Expansion_Bays",\
# #                 "Minimum_Crew","Maximum_Crew","Cost"',
# #                 '2,"Interceptor",1,5,30,0,6,0,1,1,6',cur,con)
# # sql.tableInsert("Frames",'"id","Name","Size","Maneuverability","HP","DT","CT","Expansion_Bays",\
# #                 "Minimum_Crew","Maximum_Crew","Cost"',
# #                 '3,"Fighter",1,4,35,0,7,0,1,2,8',cur,con)

# # cur.execute("SELECT * FROM Frames;")
# # result = cur.fetchall()
# # print(result)

# # sql.tableInsert("Size",'"id","size","modifier"','1,"Tiny",2',cur,con)
# # sql.tableInsert("Size",'"id","size","modifier"','2,"Small",1',cur,con)
# # sql.tableInsert("Size",'"id","size","modifier"','3,"Medium",0',cur,con)
# # sql.tableInsert("Size",'"id","size","modifier"','4,"Large",-1',cur,con)
# # sql.tableInsert("Size",'"id","size","modifier"','5,"Huge",-2',cur,con)
# # sql.tableInsert("Size",'"id","size","modifier"','6,"Gargantuan",-3',cur,con)
# # sql.tableInsert("Size",'"id","size","modifier"','7,"Colossal",-4',cur,con)

# cur.execute("SELECT * FROM Size;")
# result = cur.fetchall()
# print(result)

# #sql.tableInsert("Maneuverability",'"id","manueverability","modifier","turn"','1,"clumsy",-2,4',cur,con)
# # sql.tableInsert("Maneuverability",'"id","manueverability","modifier","turn"','2,"poor",-1,3',cur,con)
# # sql.tableInsert("Maneuverability",'"id","manueverability","modifier","turn"','3,"average",0,2',cur,con)
# # sql.tableInsert("Maneuverability",'"id","manueverability","modifier","turn"','4,"good",1,1',cur,con)
# # sql.tableInsert("Maneuverability",'"id","manueverability","modifier","turn"','5,"perfect",2,0',cur,con)

# cur.execute("SELECT * FROM Maneuverability;")
# result = cur.fetchall()
# print(result)

# sql.tableInsert("Frame_Mounts",'"id","frame_id","forward_light","forward_heavy","forward_capital",\
#                 "aft_light","aft_heavy","aft_capital","starboard_light","starboard_heavy",\
#                 "starboard_capital","port_light","port_heavy","port_capital"',
#                 '1,1,"forward_light","forward_heavy","forward_capital","aft_light", \
#                 "aft_heavy","aft_capital","starboard_light","starboard_heavy","starboard_capital", \
#                 "port_light","port_heavy","port_capital"',cur,con)
# sql.tableInsert("Frame_Mounts",'"id","frame_id","forward_light","forward_heavy","forward_capital",\
#                 "aft_light","aft_heavy","aft_capital","starboard_light","starboard_heavy",\
#                 "starboard_capital","port_light","port_heavy","port_capital"',
#                 '2,2,"forward_light","forward_heavy","forward_capital","aft_light", \
#                 "aft_heavy","aft_capital","starboard_light","starboard_heavy","starboard_capital", \
#                 "port_light","port_heavy","port_capital"',cur,con)
# sql.tableInsert("Frame_Mounts",'"id","frame_id","forward_light","forward_heavy","forward_capital",\
#                 "aft_light","aft_heavy","aft_capital","starboard_light","starboard_heavy",\
#                 "starboard_capital","port_light","port_heavy","port_capital"',
#                 '3,3,"forward_light","forward_heavy","forward_capital","aft_light", \
#                 "aft_heavy","aft_capital","starboard_light","starboard_heavy","starboard_capital", \
#                 "port_light","port_heavy","port_capital"',cur,con)




# sql.tableInsert("Power_Cores","id","Name","Size","PCU","Cost","id","Name","Size","PCU","Cost",cur,con)
# sql.tableInsert("Thrusters","id","Name","Size","Speed","Piloting_Modifier","PCU","Cost","id","Name","Size","Speed","Piloting_Modifier","PCU","Cost",cur,con)
# sql.tableInsert("Armor","id","Name","Bonus_to_AC","Special","Cost","id","Name","Bonus_to_AC","Special","Cost",cur,con)
# sql.tableInsert("Computer","id","Name","Bonus","Nodes","PCU","Cost","id","Name","Bonus","Nodes","PCU","Cost",cur,con)
# sql.tableInsert("Defensive_Countermeasures","id","Name","Bonus_to_TL","PCU","Cost","id","Name","Bonus_to_TL","PCU","Cost",cur,con)
# sql.tableInsert("Drift_Engines","id","Name","Engine_Rating","PCU","Max_Size","Cost","id","Name","Engine_Rating","PCU","Max_Size","Cost",cur,con)
# sql.tableInsert("Security","id","Name","Cost","id","Name","Cost",cur,con)
# sql.tableInsert("Sensors","id","Name","Range","Modifier","Cost","id","Name","Range","Modifier","Cost",cur,con)
# sql.tableInsert("Shields","id","Name","Total_SP","Regen","PCU","Cost","id","Name","Total_SP","Regen","PCU","Cost",cur,con)
# sql.tableInsert("Weapons","id","Name","Range","Speed","Damage","PCU","Special","Cost","id","Name","Range","Speed","Damage","PCU","Special","Cost",cur,con)
# sql.tableInsert("Expansion_Bays","id","Name","PCU","Cost","id","Name","PCU","Cost",cur,con)








# 'Frames':[
#                         'id',
#                         'Name', 
#                         'Size', 
#                         'Maneuverability', 
#                         'HP', 
#                         'DT', 
#                         'CT',  
#                         'Expansion_Bays', 
#                         'Minimum_Crew', 
#                         'Maximum_Crew', 
#                         'Cost'],





# def verifyTables(): #checks if tables exists, if it doesn't, creates a new one and sets a row into the table as a placeholder
#         #item        #list
#     for table in bootup.tableList:
#             Frames
#         if sql.tableCheck(table,cur) != 1:


#             columns = ",".join([ 'id',
#                         'Name', 
#                         'Size', 
#                         'Maneuverability', 
#                         'HP', 
#                         'DT', 
#                         'CT',  
#                         'Expansion_Bays', 
#                         'Minimum_Crew', 
#                         'Maximum_Crew', 
#                         'Cost'],)


#             sql.tableConstructor(table,cur,con,columns)
#             print("Table ",table," created!")
#         else:
#             print("table confirmed.")













#make a ship tier 1 
 #- 55 build points 

 # - frame is required        10 bp
 # - can only have guns that the frame can equip 
 # - power core is required   15
 # - thrusters are required    5
 # - at least 1 gun            8
 

 # -    armor +2              4
 # -    secuirty              6

