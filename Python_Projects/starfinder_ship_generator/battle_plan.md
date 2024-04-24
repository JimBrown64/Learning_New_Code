

- Build App To take a Tier, Frame, and Power Core and have it select all the other parts
    - Base level:
        - Build a function That takes in the Tier, Frame, and Power Core
            - Strip Build Points From Tier and store it in a variable
            - Strip Size and Cost from Frame
                - Use Frame id to gather Frame Mounts
                - Function should deduct Cost Build Points from the total Alotment of BP
            - Strip Size, Cost and PCU from Power core
                - Function Should confirm the Size of the Power Core is appropriate for the size of the Frame, 
                    if not, throw an error.
                - Function should deduct Cost Build Points from the total alotment of BP

        - Build a function that takes in remaining Build Points, Size, and remaining PCU
            - should select thrusters of an appropriate size and power requirement in relation to Frame.Size and   
                Power_Core.PCU
            - should deduct Cost from remaining BP, and PCU from remaining PCU
        
        - Build a function that takes in remaining Build Points, remaining PCU, and Frame_Mounts
            - Function should select weapons based on remaining BP, PCU and number of available Mounts
                - The weapons must also be of an appropriate weight Category for the mounts





- Make Changes to the app to not need to provide it Power Core


- Make Further changes to not require a Frame