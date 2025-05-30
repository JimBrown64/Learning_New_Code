"""list of tables and values to be stored in them. Planning to replace with JSON at a later time."""
table_list = {'Frame':[
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
            'Power_Core': [
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
            'Drift_Engine':[
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
                        'Maneuverability',
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



frame_values =[
    "'Racer',1,5,20,0,4,0,1,1,4",
    "'Interceptor',1,5,30,0,6,0,1,1,6",
    "'Fighter',1,4,35,0,7,0,1,2,8",
    "'Shuttle',2,5,35,0,7,3,1,4,6",
    "'Light Freighter',2,4,40,0,8,3,1,6,10",
    "'Explorer',3,4,55,0,11,4,1,6,12",
    "'Transport',3,3,70,0,14,5,1,6,15",
    "'Destroyer',4,3,150,0,30,4,6,20,30",
    "'Heavy Freighter',4,3,120,0,24,8,6,20,40",
    "'Bulk Freighter',5,2,160,5,32,10,20,50,55",
    "'Cruiser',5,3,180,5,36,6,20,100,60",
    "'Carrier',6,2,240,10,48,10,75,200,120",
    "'Battleship',6,3,280,10,56,8,100,300,150",
    "'Dreadnought',7,1,400,15,80,20,100,300,200"
]



frame_mount_values = [
    "1,'Forward','Light',1",
    "1,'Aft','Light',1",
    "2,'Forward','Light',2",
    "3,'Forward','Light',2",
    "3,'Aft','Light',1",
    "4,'Forward','Light',1",
    "5,'Forward','Light',2",
    "5,'Port','Light',1",
    "5,'Starboard','Light',1",
    "6,'Forward','Light',1",
    "6,'Port','Light',1",
    "6,'Starboard','Light',1",
    "6,'Turret','Light',1",
    "7,'Forward','Light',1",
    "7,'Forward','Heavy',1",
    "7,'Forward','Light',1",
    "7,'Aft','Light',1",
    "7,'Turret','Light',2",
    "8,'Forward','Heavy',2",
    "8,'Port','Light',1",
    "8,'Starboard','Light',1",
    "8,'Aft','Light',1",
    "8,'Turret','Light',1",
    "9,'Forward','Heavy',1",
    "9,'Forward','Light',2",
    "9,'Port','Heavy',1",
    "9,'Starboard','Heavy',1",
    "10,'Forward','Heavy',1",
    "10,'Aft','Heavy',1",
    "10,'Turret','Light',2",
    "11,'Forward','Capital',1",
    "11,'Port','Light',1",
    "11,'Starboard','Light',1",
    "11,'Turret','Heavy',1",
    "12,'Forward','Capital',1",
    "12,'Port','Heavy',3",
    "12,'Starboard','Heavy',3",
    "12,'Turret','Light',2",
    "13,'Forward','Capital',1",
    "13,'Forward','Heavy',2",
    "13,'Port','Heavy',2",
    "13,'Port','Light',1",
    "13,'Starboard','Heavy',2",
    "13,'Starboard','Light',1",
    "13,'Aft','Light',1",
    "13,'Turret','Heavy',2",
    "14,'Forward','Capital',2",
    "14,'Forward','Heavy',2",
    "14,'Port','Capital',1",
    "14,'Port','Heavy',3",
    "14,'Starboard','Capital',1",
    "14,'Starboard','Heavy',3",
    "14,'Turret','Light',4"
]

power_core_values = [
    "'Micron Light',50,4",
    "'Micron Heavy',70,6",
    "'Micron Ultra',80,8",
    "'Arcus Light',75,7",
    "'Arcus Heavy',130,13",
    "'Arcus Ultra',150,15",
    "'Arcus Maximum',200,20",
    "'Pulse Brown',90,9",
    "'Pulse Black',120,12",
    "'Pulse White',140,14",
    "'Pulse Gray',100,10",
    "'Pulse Green',150,15",
    "'Pulse Red',175,17",
    "'Pulse Blue',200,20",
    "'Pulse Orange',250,25",
    "'Pulse Prismatic',300,30",
    "'Nova Light',150,15",
    "'Nova Heavy',200,20",
    "'Nova Ultra',300,30",
    "'Gateway Light',300,30",
    "'Gateway Heavy',400,40",
    "'Gateway Ultra',500,50"
]

power_core_size_values = [
    "1,1",
    "2,1",
    "3,1",
    "4,1",
    "4,2",
    "5,1",
    "5,2",
    "5,3",
    "6,2",
    "6,3",
    "6,4",
    "7,2",
    "7,3",
    "7,4",
    "8,1",
    "8,2",
    "9,1",
    "9,2",
    "10,1",
    "10,2",
    "11,1",
    "11,2",
    "11,3",
    "12,1",
    "12,2",
    "12,3",
    "13,1",
    "13,2",
    "13,3",
    "14,1",
    "14,2",
    "14,3",
    "15,2",
    "15,3",
    "15,4",
    "16,2",
    "16,3",
    "16,4",
    "17,3",
    "17,4",
    "17,5",  
    "18,3",
    "18,4",
    "18,5",
    "19,3",
    "19,4",
    "19,5",
    "20,4",
    "20,5",
    "20,6",
    "21,4",
    "21,5",
    "21,6",
    "22,4",
    "22,5",
    "22,6"
]

thruster_values=[
    "'T6',1,6,1,20,3",
    "'T8',1,8,0,25,4",
    "'T10',1,10,0,30,5",
    "'T12',1,12,-1,35,6",
    "'T14',1,14,-2,40,7",
    "'S6',2,6,1,30,3",
    "'S8',2,8,0,40,4",
    "'S10',2,10,0,50,5",
    "'S12',2,12,-1,60,6",
    "'M4',3,4,2,40,2",
    "'M6',3,6,1,50,3",
    "'M8',3,8,0,60,4",
    "'M10',3,10,0,70,5",
    "'M12',3,12,-1,80,6",
    "'L4',4,4,2,60,4",
    "'L6',4,6,1,80,6",
    "'L8',4,8,0,100,8",
    "'L10',4,10,0,120,10",
    "'H4',5,4,2,80,4",
    "'H6',5,6,1,120,6",
    "'H8',5,8,0,140,8",
    "'H10',5,10,0,160,10",
    "'G4',6,4,2,120,8",
    "'G6',6,6,1,180,12",
    "'G8',6,8,0,240,16",
    "'C4',7,4,2,200,8",
    "'C6',7,6,1,300,12",
    "'C8',7,8,0,400,16"
]

size_values = [
    "'Tiny',2",
    "'Small',1",
    "'Medium',0",
    "'Large',-1",
    "'Huge',-2",
    "'Gargantuan',-4",
    "'Colossal',-8"
]

maneuverability_values = [
    "'Clumsy',-2,4",
    "'Poor',-1,3",
    "'Average',0,2",
    "'Good',1,1",
    "'Perfect',2,0"
]

tier_values = [
    ".25,25",
    ".3,30",
    ".5,40",
    "1,55",
    "2,75",
    "3,95",
    "4,115",
    "5,135",
    "6,155",
    "7,180",
    "8,205",
    "9,230",
    "10,270",
    "11,310",
    "12,350",
    "13,400",
    "14,450",
    "15,500",
    "16,600",
    "17,700",
    "18,800",
    "19,900",
    "20,1000"
]
