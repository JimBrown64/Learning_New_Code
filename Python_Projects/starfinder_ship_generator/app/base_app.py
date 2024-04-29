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
import raw_data


def connect():
    con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return(con)

def verifyTables(): #checks if tables exists, if they don't, 
                    #creates a them
    for table in raw_data.tableList:
        if sql.tableCheck(table,cur) != 1:
            columns = ",".join(raw_data.tableList[table])
            sql.tableConstructor(table,cur,con,columns)
            print("Table ",table," created!")
        else:
            print("table confirmed.")



BP = 0
PCU = 0
frameId = 0
shipSize = 0
frameMounts = {'Light':0, 'Heavy':0, 'Capital':0}
weapons = []

def baseSet(tier,frame,powerCore,cur): #take in base info, assign bp, pcu, frameid, and shipSize, 
    try:                                   #which will be utilized throughout
        bpStatement = "SELECT Tier.Build_Points \
                    FROM Tier \
                    WHERE tier = " + str(tier)+";"
        frameStatement = "SELECT Frames.id,Frames.size,Frames.Cost, Frame_Mounts.weight, Frame_Mounts.count \
                        FROM Frames \
                        JOIN Frame_Mounts ON Frames.id = Frame_Mounts.frame_id\
                        WHERE Name = '" + frame +"';"
        powerCoreStatement = "SELECT Power_Core_Size.size, Power_Cores.Cost, Power_Cores.PCU \
                            FROM power_cores \
                            JOIN Power_Core_Size ON Power_Cores.id = Power_Core_Size.Power_Core_Id \
                            WHERE Power_Cores.name = '" + powerCore +"';"
        cur.execute(bpStatement)
        bpResult = cur.fetchall()
        cur.execute(frameStatement)
        frameResult = cur.fetchall()
        print("FrameResult: ",frameResult)
        cur.execute(powerCoreStatement)
        pcResult = cur.fetchall()
        for record in frameResult:
            globals()["frameMounts"][record[3]] += record[4]
        print("allowedMounts: ",globals()["frameMounts"])
        baseBP = bpResult[0][0]
        frameSize = frameResult[0][1]
        coreSize = pcResult[0][0]
        basePCU = pcResult[0][2]
        frameCost = frameResult[0][2]
        pcCost = pcResult[0][1]
        totalCost = frameCost + pcCost

        if frameSize != coreSize:
            print("Core size incorrect for the selected frame!")
        else:
            remainingBP = baseBP - totalCost 
            globals()["BP"] = remainingBP
            globals()["PCU"] = basePCU
            globals()["frameId"] = frameResult[0][0]
            globals()["shipSize"] = frameSize
    except ValueError as error:
        print("error in baseSet: ", error)


def selectThrusters(BP,Size,PCU,cur): #choose thrusters based on size, remaining pcu, and remaining BP
    try:
        thrusterStatement = "SELECT Thrusters.Name, Thrusters.Size, Thrusters.PCU, Thrusters.Cost \
                            FROM Thrusters\
                            WHERE Thrusters.Size = " + str(Size) +" AND Thrusters.Cost < "+ str(BP)+ \
                                " AND Thrusters.PCU < "+str(PCU)+";"
        cur.execute(thrusterStatement)
        thrusterResult = cur.fetchall()
        thrusterSelection = random.choice(thrusterResult)
        print("thrusterSelection: ",thrusterSelection)
        thrusterPCU = thrusterSelection[2]
        thrusterCost = thrusterSelection[3]

        remainingPCU = globals()["PCU"] - thrusterPCU
        print("Starting PCU(",globals()["PCU"],") - thrusterPCU(",thrusterPCU,") = ", remainingPCU)
        remainingBP = globals()["BP"] - thrusterCost
        print("Starting BP(",globals()["BP"],") - thrusterCost(",thrusterCost,") = ", remainingBP)
        globals()["PCU"] = remainingPCU
        globals()["BP"] = remainingBP

        return thrusterSelection[0]
    except ValueError as error:
        print("error in selectThrusters: ",error)

def selectWeapon(BP,PCU,size): #Selects a weapon based on remaining bp, pcu, and what mounts are available
    try: 
        frameMounts = globals()["frameMounts"]
        if frameMounts[size] != 0:
            weaponsStatement = "SELECT Weapons.id, Weapons.Name, Weapons.PCU, Weapons.Cost \
                                FROM Weapons \
                                WHERE Weapons.Weight IN ('"+ size+"')\
                                    AND Weapons.Cost < "+ str(BP) + \
                                    " AND Weapons.PCU < " + str(PCU) +";" # only checking less than to ensure 
                                                                          # there is some budget left for both 
                                                                          # PCU and BP
            cur.execute(weaponsStatement)
            weaponsResult = cur.fetchall()
            weaponSelection = random.choice(weaponsResult)
            weaponPCU = weaponSelection[2]
            weaponCost = weaponSelection[3]
            remainingPCU = globals()["PCU"] - weaponPCU
            print("Starting PCU(",globals()["PCU"],") - weaponPCU(",weaponPCU,") = ", remainingPCU)
            remainingBP = globals()["BP"] - weaponCost
            print("Starting BP(",globals()["BP"],") - weaponCost(",weaponCost,") = ", remainingBP)
            globals()["PCU"] = remainingPCU
            globals()["BP"] = remainingBP
            frameMounts[size] -= 1
            print("frameMounts: ", frameMounts)
            print("weaponsResult: ",weaponsResult)
            return(weaponSelection[1])
        else:
            print("No available mounts of this size")
            return 0
    except ValueError as error:
        print("error in selectWeapon: ",error)


def fillWeapons(BP,PCU,mounts):
    try:
        if BP > 0 and PCU > 0:  
            for size in mounts:
                while mounts[size] > 0 and BP >0 and PCU >0:
                    newWeapon = selectWeapon(BP,PCU,size)
                    if newWeapon != 0:
                        globals()["weapons"].append(newWeapon)
                        print("newWeapon: ", newWeapon)
    except ValueError as error:
        print("error in fillWeapons: ", error)

def selectShields(BP,PCU):
    try:
        if BP > 0 and PCU > 0:

            shieldStatement = "SELECT Shields.Name, Shields.PCU, Shields.Cost \
                        FROM Shields\
                        WHERE Shields.Cost < "+ str(BP)+ \
                            " AND Shields.PCU < "+str(PCU)+";"
            cur.execute(shieldStatement)
            shieldResult = cur.fetchall()
            shieldSelection = random.choice(shieldResult)
            print("shieldSelection: ",shieldSelection)
            shieldPCU = shieldSelection[1]
            shieldCost = shieldSelection[2]

            remainingPCU = globals()["PCU"] - shieldPCU
            print("Starting PCU(",globals()["PCU"],") - shieldPCU(",shieldPCU,") = ", remainingPCU)
            remainingBP = globals()["BP"] - shieldCost
            print("Starting BP(",globals()["BP"],") - shieldCost(",shieldCost,") = ", remainingBP)
            globals()["PCU"] = remainingPCU
            globals()["BP"] = remainingBP
            return shieldSelection[0]
        else: 
            print("No more alotted budget")


    except ValueError as error:
        print("error in selectShields: ", error)




 



def printValues():
    print("BP: ",globals()["BP"], " PCU: ", globals()["PCU"], " Size: ", 
          globals()["shipSize"]," thrusters: ", globals()['thrusters']," weapons: ", globals()["weapons"])


con = connect()
cur = con.cursor()
verifyTables()
# bootup.insertData() 
# baseSet(1,"Fighter","Micron Heavy",cur)
# thrusters = selectThrusters(BP,shipSize,PCU,cur)
# shields = selectShields(BP,PCU)
# fillWeapons(BP,PCU,frameMounts)
# printValues()








