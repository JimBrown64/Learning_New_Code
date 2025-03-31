DM_Buddy

- This project exists to create an application that will allow A Dungeon Master(DM) 
    in "Dungeons and Dragons" to easily organize notes and information about 
    Non-Playable Characters (NPC's) controlled by the DM, regions in their world, and
    major events that occur in their Campaign (instance of the game the players play,
    with the DM being in control of world events. Typically arcs over a greater storyline.)
- The ui will offer a selection of dropdown menus and fields that can be typed in 
    to find the information they hope to aquire. For example, a generalized dropdown 
    for what kind of information (region, a specific character, a historic event) which
    will then populate other options to fill out. The plan is to allow any level of specificity of information. If someone wants "All information about 'Region A'", then they would select Region from the dropdown, enter 'Region A' into a form that will appear and hit enter. This will provide a list of cities, towns, other locations, 
    relevant characters and historic events. Alternatively, someone could look for "Nobility of 'City A' who were involved in 'The French Revolution'", which would provide just a list of relevant characters.
- Future goals 
    - "Google Maps" type application that allows a user to import a world map for
        their campaign and could instead of using the dropdowns click on the map to gain information relevant to the location clicked. 
    - ability to upload images of characters or cities,
    - android friendly version of the application.
    - ability to import external data, such as a json or csv

- The project will utilize a sqlite database to store the information.
    Tables:
        - NPC's
            - Character_id (primary key)
            - Name
            - Faction(foreign key)
            - Title (Czar, King, Silver Petal)
            - Race (foreign key)
            - Defining characteristics
            - Story_Relevance (more immediate notes available about this char)
            //following columns are for in game stats
            - HP (health points)
            - AC (armor class)
            - Str (strength)
            - Dex (dexterity)
            - Con (constitution)
            - Int (intelligence)
            - Wis (wisdom)
            - Cha (Charisma)
        
        - Races
            - Race_id (primary key)
            - region_id (foreign key)(defines their main homeland)
            - Notable_Relations (how they interact with other races)
            - World_View (how the other races see them)
        
        - History
            - History_id (primary key)
            - Character_id (who is relavent)(foreign key)
            - Event_name ("hundered year war", or brief description)
            - Details (long form description)
            - Importance (tiered based on historical significance. world event? minor
                event? formative to a Player Character?)

        - Continents
            - Continent_id(primary key)
            - Name
            - Generalized Description? (may drop, as it is seldom relevant)

        - Nations
            - Nation_id(primary key)
            - Continent_id(foreign key)
            - Ruler (foreign key)
            - Description (geography, political structure etc)
            - Notes (what significant actions have the players done here?)
            - History(foreign key)

        Cities
            - City_id(primary key)
            - Nation_id(foreign key)
            - Ruler(foreign key)
            - Description
            - Notes
            - History(foreign key)
            - Factions(foreign key)
        
        Factions
            - Faction_id(primary key)
            - Name
            - Description
            - History (foreign key)
        
        location_history (will track where a character has been)
            - LH_id(primary key)
            - character_id(foreign key)
            - location_id(foreign key)
            - current_location ('Y' or 'N')
            - home_location ('Y' or 'N')
               
        -Locations (view combining continents, nations and cities)
            - location_id(primary key)
            - Name
            - Category (continent, nation, city, town)
            - Description
            - Leader
            - Notes
            - History
            - Factions
