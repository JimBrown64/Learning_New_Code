"""Module to utilize other app components to build a ship"""
import sqlite3
import random
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import utilities.sql_interactions as sql
# import bootup
import app.raw_data

def connect():
    """create connection to database"""
    connection = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return connection

def verify_tables():
    """checks if tables exists, if they don't, creates a them"""                
    for table, column_set in app.raw_data.table_list.items():
        if sql.tableCheck(table,cur) != 1:
            columns = ",".join(column_set)
            sql.tableConstructor(table,cur,con,columns)
            print("Table ",table," created!")
        else:
            print("table confirmed.")



total_bp = 0
total_pcu = 0
frame_id = 0
ship_size = 0
frame_mounts = {'Light':0, 'Heavy':0, 'Capital':0}
weapons = []

def base_set(tier,frame,power_core,cursor):
    """take in base info, assign bp, pcu, frame_id, and ship_size, which will be utilized throughout"""
    try:
        bp_statement = "SELECT Tier.Build_Points \
                    FROM Tier \
                    WHERE tier = " + str(tier)+";"
        frame_statement = "SELECT Frames.id,Frames.size,Frames.Cost, Frame_Mounts.weight, Frame_Mounts.count \
                        FROM Frames \
                        JOIN Frame_Mounts ON Frames.id = Frame_Mounts.frame_id\
                        WHERE Name = '" + frame +"';"
        power_core_statement = "SELECT Power_Core_Size.size, Power_Cores.Cost, Power_Cores.PCU \
                            FROM power_cores \
                            JOIN Power_Core_Size ON Power_Cores.id = Power_Core_Size.Power_Core_Id \
                            WHERE Power_Cores.name = '" + power_core +"';"
        cursor.execute(bp_statement)
        bp_result = cursor.fetchall()
        cursor.execute(frame_statement)
        frame_result = cursor.fetchall()
        cursor.execute(power_core_statement)
        pc_result = cursor.fetchall()
        for record in frame_result:
            globals()["frame_mounts"][record[3]] += record[4]
        print("allowedMounts: ",globals()["frame_mounts"])
        base_bp = bp_result[0][0]
        frame_size = frame_result[0][1]
        core_size = pc_result[0][0]
        base_pcu = pc_result[0][2]
        frame_cost = frame_result[0][2]
        pc_cost = pc_result[0][1]
        total_cost = frame_cost + pc_cost

        if frame_size != core_size:
            print("Core size incorrect for the selected frame!")
        else:
            remaining_bp = base_bp - total_cost
            globals()["total_bp"] = remaining_bp
            globals()["total_pcu"] = base_pcu
            globals()["frame_id"] = frame_result[0][0]
            globals()["ship_size"] = frame_size
    except ValueError as error:
        print("error in baseSet: ", error)


def select_thrusters(bp,size,pcu,cursor):
    """choose thrusters based on size, remaining pcu, and remaining BP"""
    try:
        thruster_statement = "SELECT Thrusters.Name, Thrusters.size, Thrusters.pcu, Thrusters.Cost \
                            FROM Thrusters\
                            WHERE Thrusters.size = " + str(size) +" AND Thrusters.Cost < "+ str(bp)+ \
                                " AND Thrusters.pcu < "+str(pcu)+";"
        cursor.execute(thruster_statement)
        thruster_result = cursor.fetchall()
        thruster_selection = random.choice(thruster_result)
        print("thruster_selection: ",thruster_selection)
        thruster_pcu = thruster_selection[2]
        thruster_cost = thruster_selection[3]

        remaining_pcu = globals()["total_pcu"] - thruster_pcu
        print("Starting PCU(",globals()["total_pcu"],") - thrusterPCU(",thruster_pcu,") = ", thruster_pcu)
        remaining_bp = globals()["total_bp"] - thruster_cost
        print("Starting BP(",globals()["total_bp"],") - thruster_cost(",thruster_cost,") = ", remaining_bp)
        globals()["total_pcu"] = remaining_pcu
        globals()["total_bp"] = remaining_bp

        return thruster_selection[0]
    except ValueError as error:
        print("error in select_thrusters: ",error)

def select_weapon(bp,pcu,size,cursor):
    """Selects a weapon based on remaining bp, pcu, and what mounts are available"""
    try:
        mounts = globals()["frame_mounts"]
        if mounts[size] != 0:
            weapons_statement = "SELECT weapons.id, weapons.Name, weapons.pcu, weapons.Cost \
                                FROM weapons \
                                WHERE weapons.Weight IN ('"+ size+"')\
                                    AND weapons.Cost < "+ str(bp) + \
                                    " AND weapons.pcu < " + str(pcu) +";" # only checking less than to ensure 
                                                                          # there is some budget left for both
                                                                          # PCU and BP
            cursor.execute(weapons_statement)
            weapons_result = cursor.fetchall()
            weapon_selection = random.choice(weapons_result)
            weapon_pcu = weapon_selection[2]
            weapon_cost = weapon_selection[3]
            remaining_pcu = globals()["total_pcu"] - weapon_pcu
            print("Starting PCU(",globals()["total_pcu"],") - weaponPCU(",weapon_pcu,") = ", remaining_pcu)
            remaining_bp = globals()["total_bp"] - weapon_cost
            print("Starting BP(",globals()["total_bp"],") - weaponCost(",weapon_cost,") = ", remaining_bp)
            globals()["total_pcu"] = remaining_pcu
            globals()["total_bp"] = remaining_bp
            mounts[size] -= 1
            print("frame_mounts: ", frame_mounts)
            print("weapons_result: ",weapons_result)
            return weapon_selection[1]

        print("No available mounts of this size")
        return 0
    except ValueError as error:
        print("error in select_weapon: ",error)


def fill_weapons(bp,pcu,mounts,cursor):
    """Select weapons until all mounts are used, or the budget is used up"""
    try:
        if bp > 0 and pcu > 0:
            for size in mounts:
                while mounts[size] > 0 and bp >0 and pcu >0:
                    new_weapon = select_weapon(bp,pcu,size,cursor)
                    if new_weapon != 0:
                        globals()["weapons"].append(new_weapon)
                        print("new_weapon: ", new_weapon)
    except ValueError as error:
        print("error in fill_weapons: ", error)

def select_shields(bp,pcu,cursor):
    """select a shield to use based on remaining bp and pcu"""
    try:
        if bp > 0 and pcu > 0:

            shield_statement = "SELECT Shields.Name, Shields.pcu, Shields.Cost \
                        FROM Shields\
                        WHERE Shields.Cost < "+ str(bp)+ \
                            " AND Shields.pcu < "+str(pcu)+";"
            cursor.execute(shield_statement)
            shield_result = cursor.fetchall()
            shield_selection = random.choice(shield_result)
            print("shield_selection: ",shield_selection)
            shield_pcu = shield_selection[1]
            shield_cost = shield_selection[2]

            remaining_pcu = globals()["total_pcu"] - shield_pcu
            print("Starting pcu(",globals()["total_pcu"],") - shield_pcu(",shield_pcu,") = ", remaining_pcu)
            remaining_bp = globals()["total_bp"] - shield_cost
            print("Starting BP(",globals()["total_bp"],") - shield_cost(",shield_cost,") = ", remaining_bp)
            globals()["total_pcu"] = remaining_pcu
            globals()["total_bp"] = remaining_bp
            return shield_selection[0]
        print("No more alotted budget")
        return 0

    except ValueError as error:
        print("error in select_shields: ", error)




def print_values():
    """prints final values. meant for testing"""
    print("BP: ",globals()["total_bp"], " PCU: ", globals()["total_pcu"], " size: ",
          globals()["ship_size"]," thrusters: ", globals()['thrusters']," weapons: ", globals()["weapons"])


con = connect()
cur = con.cursor()
verify_tables()
# bootup.insertData()
# baseSet(1,"Fighter","Micron Heavy",cur)
# thrusters = select_thrusters(BP,ship_size,PCU,cur)
# shields = select_shields(BP,PCU)
# fill_weapons(BP,PCU,frame_mounts)
# print_values()
