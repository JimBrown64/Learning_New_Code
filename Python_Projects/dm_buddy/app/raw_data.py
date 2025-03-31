"""list of tables and values to be stored in them. Planning to replace with JSON at a later time."""
table_list = {
                'NPCs':[
                    'Character_id',#primary key
                    'Name',
                    'Faction',#foreign key
                    'Title',#Czar, King, Silver Petal
                    'Race',#foreign key
                    'Defining_characteristics',
                    'Story_Relevance',
                    #more immediate notes available about this char
                    #following columns are for in game stats
                    'HP',
                    'AC',
                    'Str',
                    'Dex',
                    'Con',
                    'Int',
                    'Wis',
                    'Cha'
                ],
                'Continents':[
                    'Continent_id', #primary key
                    'Name',
                    'Generalized_Description',
                ],
                'Nations':[
                    'Nation_id',#primary key
                    'Continent_id',#foreign key
                    'Ruler',#foreign key
                    'Description',#geography, political structure etc
                    'Notes',#what significant actions have the players done here?
                    'History'#foreign key
                ],
                'Cities':[
                    'City_id',#primary key
                    'Nation_id',#foreign key
                    'Ruler',#foreign key
                    'Description',
                    'Notes',
                    'History',#foreign key
                    'Factions'#foreign key
                ],
                'Factions':[
                    'Faction_id',
                    'Name',
                    'Description',
                    'History'
                ],
                'location_history':[#will track where a character has been)
                    'LH_id'#primary key)
                    ,'character_id'#foreign key)
                    ,'location_id'#foreign key)
                    ,'current_location '#'Y' or 'N')
                    ,'home_location '#'Y' or 'N')
                ],
                'Locations':[#view combining continents, nations and cities)
                    'location_id'#primary key)
                    ,'Name'
                    ,'Category '#continent, nation, city, town)
                    ,'Description'
                    ,'Leader'
                    ,'Notes'
                    ,'History'
                    ,'Factions'
                ]
            }
