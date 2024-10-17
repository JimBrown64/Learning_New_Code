update as of 07/10/2024

- Ai should: 
    - take in an input ("battleship")
    - take in list of "answers" (the ships generated in the list)
    - assess based on Q-values which of the ANSWERS would be a proper fit in relation to the INPUT
        - Q-values would contain:
            - input
            - answer 
            - reward
    - NOTE: can use    "ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS row_index," in the SELECT
        statement to label each row with an index (makes recalling the correct row easier) 



update as of 05/24/2024

- Adjusted plan to generate list of possibly compatible ship combinations based on conditions in SQL
    - Query pulls together:
        - Tier
        - Frame
        - power core
        - thrusters
    - Components are matched based on compatibilities:
        - Size
        - Power requirement/allotment
        - Tier (Build point allotment)
    - Conditions may include (but not limited to):
        - Tier (would dictate amount of BP available)
        - Crew allotment (for example, If there are 4 players, would need to filter for 4+ crew allotment)
        - Minimum remaining PCU or BP (as this query does not cover ALL parts, just the core ones, there needs to
            be adequate resources remaining to finish out the ship)

- App will utilize AI to select a ship off of this list based on requirements
    - example, input of 'battleship' should generate a ship with a focus on combat, whereas an input of 
        freighter would prioritize number of cargo holds.
    - current plan is to take values of ships generated in SQL and convert them into a value on a scale of 
        -1 through +1 based on if a given statistic for the ship is above or below the average for the 
        given component based on the returned ships presented.


----ORIGINAL---
- Build App To take a Tier, Frame, and Power Core and have it select all the other parts
    - Base level:
        - Build a function That takes in the Tier, Frame, and Power Core
            - Strip Build Points From Tier and store it in a variable
            - Strip Size and Cost from Frame
                - Use Frame id to gather Frame Mounts
                - Function should deduct Cost Build Points from the total allotment of BP
            - Strip Size, Cost and PCU from Power core
                - Function Should confirm the Size of the Power Core is appropriate for the size of the Frame, 
                    if not, throw an error.
                - Function should deduct Cost Build Points from the total allotment of BP

        - Build a function that takes in remaining Build Points, Size, and remaining PCU
            - should select thrusters of an appropriate size and power requirement in relation to Frame.Size and   
                Power_Core.PCU
            - should deduct Cost from remaining BP, and PCU from remaining PCU
        
        - Build a function that takes in remaining Build Points, remaining PCU, and Frame_Mounts
            - Function should select weapons based on remaining BP, PCU and number of available Mounts
                - The weapons must also be of an appropriate weight Category for the mounts





- Make Changes to the app to not need to provide it Power Core


- Make Further changes to not require a Frame