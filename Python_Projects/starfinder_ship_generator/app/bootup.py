"""Contains functions to populate tables for the app."""
import sqlite3
import sys
import os
import app.raw_data
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import utilities.sql_interactions as sql


def insert_data():
    """Run a series of bulk inserts based on data from raw_data.py"""
    answer = input("Do you want to populate tables? (Y/N)")
    if answer == 'Y':
        def connect():
            con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
            return con
        con = connect()
        cur = con.cursor()

        def insert_frames(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Frame"])+'"'+"'"
            for row in app.raw_data.frame_values:
                new_insert = 'sql.tableInsert("Frame",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_frames(cur,con)

        def insert_frame_mounts(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Frame_Mounts"])+'"'+"'"
            for row in app.raw_data.frame_mount_values:
                new_insert = 'sql.tableInsert("Frame_Mounts",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_frame_mounts(cur,con)

        def insert_power_cores(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Power_Core"])+'"'+"'"
            for row in app.raw_data.power_core_values:
                new_insert = 'sql.tableInsert("Power_Core",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_power_cores(cur,con)

        def insert_power_core_size(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Power_Core_Size"])+'"'+"'"
            for row in app.raw_data.power_core_size_values:
                new_insert = 'sql.tableInsert("Power_Core_Size",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_power_core_size(cur,con)

        def insert_thrusters(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Thrusters"])+'"'+"'"
            for row in app.raw_data.thruster_values:
                new_insert = 'sql.tableInsert("Thrusters",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_thrusters(cur,con)

        def insert_size(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Size"])+'"'+"'"
            for row in app.raw_data.size_values:
                new_insert = 'sql.tableInsert("Size",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_size(cur,con)

        def insert_maneuverability(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Maneuverability"])+'"'+"'"
            for row in app.raw_data.maneuverability_values:
                new_insert = 'sql.tableInsert("Maneuverability",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_maneuverability(cur,con)

        def insert_tier(cursor,connection):

            columns = "'"+'"'+'","'.join(app.raw_data.table_list["Tier"])+'"'+"'"
            for row in app.raw_data.tier_values:
                new_insert = 'sql.tableInsert("Tier",'+ columns+',"'+ str(row) +'",cursor,connection)'
                # print(new_insert)
                exec(new_insert)
        insert_tier(cur,con)

insert_data()

        # sql.tableInsert("Armor",'"Name","Bonus_to_AC","Special","Cost"',
        #                 '"MK1",1,0,"Frame.Size * 1"',cursor,connection)
        # sql.tableInsert("Armor",'"Name","Bonus_to_AC","Special","Cost"',
        #                 '"MK2",2,0,"Frame.Size * 2"',cursor,connection)
        # sql.tableInsert("Armor",'"Name","Bonus_to_AC","Special","Cost"',
        #                 '"MK3",3,0,"Frame.Size * 3"',cursor,connection)

        # cur.execute("SELECT * FROM Armor;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
        #                 '"Basic",0,0,0,0',cursor,connection)
        # sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
        #                 '"Mk1 Mononode",1,1,10,1',cursor,connection)
        # sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
        #                 '"Mk1 Duonode",1,2,10,2',cursor,connection)
        # sql.tableInsert("Computer",'"Name","Bonus","Nodes","PCU","Cost"',
        #                 '"Mk1 Trinode",1,3,10,3',cursor,connection)

        # cur.execute("SELECT * FROM Computer;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Defensive_Countermeasures",'"Name","Bonus_to_TL","PCU","Cost"',
        #                 '"Mk1 Defenses",1,1,2',cursor,connection)
        # sql.tableInsert("Defensive_Countermeasures",'"Name","Bonus_to_TL","PCU","Cost"',
        #                 '"Mk2 Defenses",2,1,3',cursor,connection)
        # sql.tableInsert("Defensive_Countermeasures",'"Name","Bonus_to_TL","PCU","Cost"',
        #                 '"Mk3 Defenses",3,2,4',cursor,connection)

        # cur.execute("SELECT * FROM Defensive_Countermeasures;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
        #                 '"Signal Basic",1,75,7,"Frame.size *2"',cursor,connection)
        # sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
        #                 '"Signal Booster",2,100,5,"Frame.size *5"',cursor,connection)
        # sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
        #                 '"Signal Major",3,150,4,"Frame.size *10"',cursor,connection)
        # sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
        #                 '"Signal Superior",4,175,4,"Frame.size *15"',cursor,connection)
        # sql.tableInsert("Drift_Engines",'"Name","Engine_Rating","PCU","Max_Size","Cost"',
        #                 '"Signal Ultra",5,200,3,"Frame.size *20"',cursor,connection)

        # cur.execute("SELECT * FROM Drift_Engines;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Security",'"Name","Cost"','"Anti-hacking Systems",3',cursor,connection)
        # sql.tableInsert("Security",'"Name","Cost"','"Antipersonnel weapon (heavy)","5 + item level of weapon"',cursor,connection)
        # sql.tableInsert("Security",'"Name","Cost"','"Antipersonnel weapon (longarm)","item level of weapon"',cursor,connection)
        # sql.tableInsert("Security",'"Name","Cost"','"Biometric Locks",5',cursor,connection)
        # sql.tableInsert("Security",'"Name","Cost"','"Computer countermeasures","tier of computer"',cursor,connection)
        # sql.tableInsert("Security",'"Name","Cost"','"Self-destruct system","Frame.size *5"',cursor,connection)

        # cur.execute("SELECT * FROM Security;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Sensors",'"Name","Range","Modifier","Cost"',
        #                 '"Cut-rate","Short(5)",-2,1',cursor,connection)
        # sql.tableInsert("Sensors",'"Name","Range","Modifier","Cost"',
        #                 '"Budget Short-range","Short(5)",0,2',cursor,connection)
        # sql.tableInsert("Sensors",'"Name","Range","Modifier","Cost"',
        #                 '"Basic Short-range","Short(5)",2,3',cursor,connection)

        # cur.execute("SELECT * FROM Sensors;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Shields",'"Name","Total_SP","Regen","PCU","Cost"',
        #                 '"Basic Shields 10",10,"1/min",5,2',cursor,connection)
        # sql.tableInsert("Shields",'"Name","Total_SP","Regen","PCU","Cost"',
        #                 '"Basic Shields 20",20,"1/min",10,3',cursor,connection)
        # sql.tableInsert("Shields",'"Name","Total_SP","Regen","PCU","Cost"',
        #                 '"Basic Shields 30",30,"1/min",15,4',cursor,connection)

        # cur.execute("SELECT * FROM Shields;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
        #                 '"Chain Cannon","Light","Short(5)",0,"6d4",15,1,10',cursor,connection)
        # sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
        #                 '"Grazer","Heavy","Short(5)",0,"7d10",40,2,35',cursor,connection)
        # sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
        #                 '"Gravity Cannon","Capital","Long(20)",0,"2d6*10",40,3,50',cursor,connection)
        # sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
        #                 '"Coil Gun","Light","Long(20)",0,"4d4",10,0,10',cursor,connection)
        # sql.tableInsert("Weapons",'"Name","Weight","Range","Speed","Damage","PCU","Special","Cost"',
        #                 '"Flak Thrower","Light","Short(5)",0,"3d4",10,6,5',cursor,connection)

        # cur.execute("SELECT * FROM Weapons;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Expansion_Bays",'"Name","PCU","Cost"',
        #                 '"Arcane Laboratory",1,1',cursor,connection)
        # sql.tableInsert("Expansion_Bays",'"Name","PCU","Cost"',
        #                 '"Cargo Hold",0,0',cursor,connection)
        # sql.tableInsert("Expansion_Bays",'"Name","PCU","Cost"',
        #                 '"Escape Pods",2,1',cursor,connection)

        # cur.execute("SELECT * FROM Expansion_Bays;")
        # result = cur.fetchall()
        # print(result)

        # sql.tableInsert("Tier",'"Tier","Build_Points"',
        #             '0.25,25',cursor,connection)
        # sql.tableInsert("Tier",'"Tier","Build_Points"',
        #             '0.33,30',cursor,connection)
        # sql.tableInsert("Tier",'"Tier","Build_Points"',
        #             '0.5,40',cursor,connection)
        # sql.tableInsert("Tier",'"Tier","Build_Points"',
        #             '1,55',cursor,connection)

        # cur.execute("SELECT * FROM Tier;")
        # result = cur.fetchall()
        # print(result)
