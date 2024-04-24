import sqlite3

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import utilities.sql_interactions as sql


tableList = {'Frames':[
                        'Name', 
                        'Size', 
                        'Maneuverability', 
                        'HP', 
                        'DT', 
                        'CT',  
                        'Expansion_Bays', 
                        'Minimum_Crew', 
                        'Maximum_Crew', 
                        'Cost'],
            'Frame_Mounts':[  
                        'frame_id',
                        'arc',
                        'weight',
                        'count'],
            'Power_Cores': [
                        'Name',  
                        'PCU', 
                        'Cost'],
            'Power_Core_Size':[
                        'Power_Core_id',
                        'Size'
            ],
            'Thrusters':[
                        'Name', 
                        'Size', 
                        'Speed', 
                        'Piloting_Modifier', 
                        'PCU', 
                        'Cost'],
            'Armor':[
                        'Name', 
                        'Bonus_to_AC', 
                        'Special', 
                        'Cost'],
            'Computer':[   
                        'Name', 
                        'Bonus', 
                        'Nodes', 
                        'PCU', 
                        'Cost'],
            'Defensive_Countermeasures':[
                        'Name', 
                        'Bonus_to_TL', 
                        'PCU', 
                        'Cost'],
            'Drift_Engines':[
                        'Name', 
                        'Engine_Rating', 
                        'PCU', 
                        'Max_Size', 
                        'Cost'],
            'Security':[
                        'Name', 
                        'Cost'],
            'Sensors':[ 
                        'Name', 
                        'Range', 
                        'Modifier', 
                        'Cost'],
            'Shields':[  
                        'Name', 
                        'Total_SP', 
                        'Regen', 
                        'PCU', 
                        'Cost'],
            'Weapons':[  
                        'Name', 
                        'Weight',
                        'Range', 
                        'Speed', 
                        'Damage', 
                        'PCU', 
                        'Special', 
                        'Cost'],
            'Expansion_Bays':[  
                        'Name', 
                        'PCU', 
                        'Cost'],
            'Size':[
                        'Size',
                        'Modifier'],
            'Maneuverability':[    
                        'Manueverability',
                        'Modifier',
                        'Turn'],
            'Special':[
                        'TL',
                        'Turn_Distance',
                        'Effect'
            ],
            'Tier':[
                        'Tier',
                        'Build_Points'
            ]
            }


def insertData():
    answer = input("Do you want to populate table? (Y/N)")
    if answer == 'Y':
        def connect():
            con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
            return(con)
        con = connect()
        cur = con.cursor()


        sql.tableInsert("Frames",'"Name","Size","Maneuverability","HP","DT","CT","Expansion_Bays",\
                        "Minimum_Crew","Maximum_Crew","Cost"',
                        '"Racer",1,5,20,0,4,0,1,1,4',cur,con)
        sql.tableInsert("Frames",'"Name","Size","Maneuverability","HP","DT","CT","Expansion_Bays",\
                        "Minimum_Crew","Maximum_Crew","Cost"',
                        '"Interceptor",1,5,30,0,6,0,1,1,6',cur,con)
        sql.tableInsert("Frames",'"Name","Size","Maneuverability","HP","DT","CT","Expansion_Bays",\
                        "Minimum_Crew","Maximum_Crew","Cost"',
                        '"Fighter",1,4,35,0,7,0,1,2,8',cur,con)

        cur.execute("SELECT * FROM Frames;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Size",'"size","modifier"','"Tiny",2',cur,con)
        sql.tableInsert("Size",'"size","modifier"','"Small",1',cur,con)
        sql.tableInsert("Size",'"size","modifier"','"Medium",0',cur,con)
        sql.tableInsert("Size",'"size","modifier"','"Large",-1',cur,con)
        sql.tableInsert("Size",'"size","modifier"','"Huge",-2',cur,con)
        sql.tableInsert("Size",'"size","modifier"','"Gargantuan",-3',cur,con)
        sql.tableInsert("Size",'"size","modifier"','"Colossal",-4',cur,con)

        cur.execute("SELECT * FROM Size;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Maneuverability",'"manueverability","modifier","turn"','"clumsy",-2,4',cur,con)
        sql.tableInsert("Maneuverability",'"manueverability","modifier","turn"','"poor",-1,3',cur,con)
        sql.tableInsert("Maneuverability",'"manueverability","modifier","turn"','"average",0,2',cur,con)
        sql.tableInsert("Maneuverability",'"manueverability","modifier","turn"','"good",1,1',cur,con)
        sql.tableInsert("Maneuverability",'"manueverability","modifier","turn"','"perfect",2,0',cur,con)

        cur.execute("SELECT * FROM Maneuverability;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Frame_Mounts",'"frame_id","arc","weight","count"',
                        '1,"Forward","Light",1' ,cur,con)
        sql.tableInsert("Frame_Mounts",'"frame_id","arc","weight","count"',
                        '1,"Aft","Light",1' ,cur,con)    
        sql.tableInsert("Frame_Mounts",'"frame_id","arc","weight","count"',
                        '2,"Forward","Light",2' ,cur,con)
        sql.tableInsert("Frame_Mounts",'"frame_id","arc","weight","count"',
                        '3,"Forward","Light",2' ,cur,con)
        sql.tableInsert("Frame_Mounts",'"frame_id","arc","weight","count"',
                        '3,"Aft","Light",1' ,cur,con)
        



        cur.execute("SELECT * FROM Frame_Mounts;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Power_Cores",'"Name","PCU","Cost"',
                        '"Micron Light",50,4',cur,con)
        sql.tableInsert("Power_Cores",'"Name","PCU","Cost"',
                        '"Micron Heavy",70,6',cur,con)
        sql.tableInsert("Power_Cores",'"Name","PCU","Cost"',
                        '"Micron Ultra",80,8',cur,con)
        sql.tableInsert("Power_Cores",'"Name","PCU","Cost"',
                        '"Arcus Light",75,7',cur,con)

        cur.execute("SELECT * FROM Power_Cores;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Power_Core_Size",'"Power_Core_id","Size"',
                        '1,1',cur,con)
        sql.tableInsert("Power_Core_Size",'"Power_Core_id","Size"',
                        '2,1',cur,con)
        sql.tableInsert("Power_Core_Size",'"Power_Core_id","Size"',
                        '3,1',cur,con)
        sql.tableInsert("Power_Core_Size",'"Power_Core_id","Size"',
                        '4,1',cur,con)
        sql.tableInsert("Power_Core_Size",'"Power_Core_id","Size"',
                        '4,2',cur,con)

        cur.execute("SELECT * FROM Power_Core_Size;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Thrusters",'"Name","Size","Speed","Piloting_Modifier","PCU","Cost"',
                        '"T6",1,6,1,20,3',cur,con)
        sql.tableInsert("Thrusters",'"Name","Size","Speed","Piloting_Modifier","PCU","Cost"',
                        '"T8",1,8,0,25,4',cur,con)
        sql.tableInsert("Thrusters",'"Name","Size","Speed","Piloting_Modifier","PCU","Cost"',
                        '"T10",1,10,0,30,5',cur,con)

        cur.execute("SELECT * FROM Thrusters;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Armor",'"Name","Bonus_to_AC","Special","Cost"',
                        '"MK1",1,0,"Frame.Size * 1"',cur,con)
        sql.tableInsert("Armor",'"Name","Bonus_to_AC","Special","Cost"',
                        '"MK2",2,0,"Frame.Size * 2"',cur,con)
        sql.tableInsert("Armor",'"Name","Bonus_to_AC","Special","Cost"',
                        '"MK3",3,0,"Frame.Size * 3"',cur,con)

        cur.execute("SELECT * FROM Armor;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
                        '"Basic",0,0,0,0',cur,con)
        sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
                        '"Mk1 Mononode",1,1,10,1',cur,con)
        sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
                        '"Mk1 Duonode",1,2,10,2',cur,con)
        sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
                        '"Mk1 Trinode",1,3,10,3',cur,con)

        cur.execute("SELECT * FROM Computer;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Defensive_Countermeasures",'"Name","Bonus_to_TL","PCU","Cost"',
                        '"Mk1 Defenses",1,1,2',cur,con)
        sql.tableInsert("Defensive_Countermeasures",'"Name","Bonus_to_TL","PCU","Cost"',
                        '"Mk2 Defenses",2,1,3',cur,con)
        sql.tableInsert("Defensive_Countermeasures",'"Name","Bonus_to_TL","PCU","Cost"',
                        '"Mk3 Defenses",3,2,4',cur,con)

        cur.execute("SELECT * FROM Defensive_Countermeasures;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
                        '"Signal Basic",1,75,7,"Frame.size *2"',cur,con)
        sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
                        '"Signal Booster",2,100,5,"Frame.size *5"',cur,con)
        sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
                        '"Signal Major",3,150,4,"Frame.size *10"',cur,con)
        sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
                        '"Signal Superior",4,175,4,"Frame.size *15"',cur,con)
        sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
                        '"Signal Ultra",5,200,3,"Frame.size *20"',cur,con)

        cur.execute("SELECT * FROM Drift_Engines;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Security",'"Name","Cost"','"Anti-hacking Systems",3',cur,con)
        sql.tableInsert("Security",'"Name","Cost"','"Antipersonnel weapon (heavy)","5 + item level of weapon"',cur,con)
        sql.tableInsert("Security",'"Name","Cost"','"Antipersonnel weapon (longarm)","item level of weapon"',cur,con)
        sql.tableInsert("Security",'"Name","Cost"','"Biometric Locks",5',cur,con)
        sql.tableInsert("Security",'"Name","Cost"','"Computer countermeasures","tier of computer"',cur,con)
        sql.tableInsert("Security",'"Name","Cost"','"Self-destruct system","Frame.size *5"',cur,con)

        cur.execute("SELECT * FROM Security;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Sensors",'"Name","Range","Modifier","Cost"',
                        '"Cut-rate","Short(5)",-2,1',cur,con)
        sql.tableInsert("Sensors",'"Name","Range","Modifier","Cost"',
                        '"Budget Short-range","Short(5)",0,2',cur,con)
        sql.tableInsert("Sensors",'"Name","Range","Modifier","Cost"',
                        '"Basic Short-range","Short(5)",2,3',cur,con)

        cur.execute("SELECT * FROM Sensors;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Shields",'"Name","Total_SP","Regen","PCU","Cost"',
                        '"Basic Shields 10",10,"1/min",5,2',cur,con)
        sql.tableInsert("Shields",'"Name","Total_SP","Regen","PCU","Cost"',
                        '"Basic Shields 20",20,"1/min",10,3',cur,con)
        sql.tableInsert("Shields",'"Name","Total_SP","Regen","PCU","Cost"',
                        '"Basic Shields 30",30,"1/min",15,4',cur,con)

        cur.execute("SELECT * FROM Shields;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
                        '"Chain Cannon","Light","Short(5)",0,"6d4",15,1,10',cur,con)
        sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
                        '"Grazer","Heavy","Short(5)",0,"7d10",40,2,35',cur,con)
        sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
                        '"Gravity Cannon","Capital","Long(20)",0,"2d6*10",40,3,50',cur,con)
        sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
                        '"Coil Gun","Light","Long(20)",0,"4d4",10,0,10',cur,con)        
        sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
                        '"Flak Thrower","Light","Short(5)",0,"3d4",10,6,5',cur,con)
        
        cur.execute("SELECT * FROM Weapons;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Expansion_Bays",'"Name","PCU","Cost"',
                        '"Arcane Laboratory",1,1',cur,con)
        sql.tableInsert("Expansion_Bays",'"Name","PCU","Cost"',
                        '"Cargo Hold",0,0',cur,con)
        sql.tableInsert("Expansion_Bays",'"Name","PCU","Cost"',
                        '"Escape Pods",2,1',cur,con)

        cur.execute("SELECT * FROM Expansion_Bays;")
        result = cur.fetchall()
        print(result)

        sql.tableInsert("Tier",'"Tier","Build_Points"',
                    '0.25,25',cur,con)
        sql.tableInsert("Tier",'"Tier","Build_Points"',
                    '0.33,30',cur,con)
        sql.tableInsert("Tier",'"Tier","Build_Points"',
                    '0.5,40',cur,con)
        sql.tableInsert("Tier",'"Tier","Build_Points"',
                    '1,55',cur,con)
        
        cur.execute("SELECT * FROM Tier;")
        result = cur.fetchall()
        print(result)    


