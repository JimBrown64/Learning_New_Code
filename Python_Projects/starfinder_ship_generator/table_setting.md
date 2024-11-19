
Functions of the app:
- Create starships for Starfinder based on base criteria: Tier, Ship function, region of creation(optional)
- Allow starships to be saved for later use
- Create starships manually
- Edit ships before saving
- Edit ships after saving

Tables and columns:
- Tier:
    - Tier:
        - Tier
        - Build_Points

- Ships:
    - Ships:
        - Name
        - Tier 
        - BP (how many Build Points available to build the ship)
        - Special (additional modifiers, typically an hp increase)
- Ship parts:    
    - Frames:
        - Name
        - Size (tiny, small, medium, large, huge, gargantuan, Colossal)
        - HP (Hull Points)
        - DT (Damage Threshold(If damage is less than this value, negates it))
        - CT (Critical Threshold(each time ship takes damage of this multiple, damages a ship system))
        - Expansion bays (spaces for cargo bays intended for special purposes)
        - Minimum crew (required to pilot ship)
        - Maximum crew (max alotment of potential crew)
        - Cost (in Build Points. Currency used to build ship.)
    - Power Cores:
        - Name
        - Size
        - PCU (power core units. How much power the core generates)
        - Cost
    - Power Core Sizes:
        - Power_Core_id
        - size
    - Thrusters:
        - Name
        - Size
        - Speed (in hexes)
        - Piloting Modifier (applied when making Piloting checks)
        - PCU (power core units. How much power the item consumes)
        - Cost
    - Armor:
        - Name
        - Bonus to AC (how much AC the armor adds to the ship)
        - Special (additional modifier from the armor)
        - Cost (effected by the ships size category)
    - Computer:
        - Name
        - Bonus (bonus applied to X battle stations, where X is the number of nodes)
        - Nodes (number of battle stations that can use the computers bonus in a round)
        - PCU (cost in PCU)
        - Cost
    - Defensive Counter Measures:
        - Name
        - Bonus to TL (how much TL the countermeasure adds to the ship)
        - PCU (cost in PCU)
        - Cost
    - Drift Engines:
        - Name
        - Engine Rating(Divide travel time by this number)
        - Min PCU (cost in PCU)
        - Max Size (largest size of ship the drift engine can be equipped to)
        - Cost
    - Security:
        - Name
        - Cost
    - Sensors:
        - Name
        - Range(short - 5 hexes, medium - 10 hexes, long - 20 hexes)
        - Modifier (applied to checks that would use the sensors (usually some form of perception))
        - Cost
    - Shields:
        - Name
        - Total SP (shield Points. these are removed before hull points)
        - Regen (rate at which the shields recover SP)
        - PCU (cost in PCU)
        - Cost
    - Weapons:
        - Name
        - Range(short - 5 hexes, medium - 10 hexes, long - 20 hexes)
        - Speed(How fast a tracking weapon travels, such as missiles)
        - Damage
        - PCU (cost in PCU)
        - Special Properties(additional effects from the weapon)
        - Cost
    - Expansion Bays:
        - Name
        - PCU (cost in PCU)
        - Cost
    - Mounts:
        - Frame_id
        - Arc
        - Weight
        - Count
    - Size:
        - id
        - size

    - Maneuverability:
        - Maneuverability(word)
        - Bonus
    - Special:
            TL(target lock),
            Turn_Distance,
            Effect(catch all for additional abilities)
- Crew:
    - Crew:
        - Role (captain, pilot, science officer, engineer, gunner)
        - Skill proficiency (Master(9 + skill level), Good(4 + skill level), Poor(0 + skill level))(usually 1 master,rest
            good)
        - Skill level (numerical value for their needed skill, usually ship tier)


