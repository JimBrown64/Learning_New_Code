


def query_construction(conditions):
    """creates SQL statement being provided to generate a ship selection"""
    try:

        sql_statement = """SELECT  tier.build_points AS BP,
                    mount_totals.mount_count AS mount_quantity,
                    frame.maneuverability,
                    frame.expansion_bays,
                    power_core.pcu,
                    thrusters.speed,
                    (tier.build_points - Frame.cost - power_core.cost - thrusters.cost) AS remaining_bp
                FROM Frame
                JOIN (SELECT SUM(frame_mounts.count) AS mount_count,frame_mounts.frame_id
                    FROM frame_mounts
                    GROUP BY frame_mounts.frame_id)AS mount_totals ON Frame.id = mount_totals.frame_id
                JOIN maneuverability ON Frame.maneuverability = maneuverability.id
                JOIN Tier ON Frame.Cost < Tier.Build_Points
                JOIN size ON Frame.size = size.id
                JOIN power_core ON power_core.id = power_core_size.power_core_id
                JOIN power_core_size ON Frame.size = power_core_size.size
                JOIN thrusters ON Frame.size = thrusters.size
                WHERE """ + conditions + """;"""
        # sql_statement = """SELECT  tier.build_points AS BP,
        #                     Frame.name,size.size,
        #                     mount_totals.mount_count AS mount_quantity,
        #                     maneuverability.maneuverability,
        #                     frame.expansion_bays,
        #                     power_core.name AS power_core_name, power_core.pcu,
        #                     thrusters.name AS thruster_name,
        #                     (tier.build_points - Frame.cost - power_core.cost - thrusters.cost) AS remaining_bp
        #                 FROM Frame
        #                 JOIN (SELECT SUM(frame_mounts.count) AS mount_count,frame_mounts.frame_id
        #                     FROM frame_mounts
        #                     GROUP BY frame_mounts.frame_id)AS mount_totals ON Frame.id = mount_totals.frame_id
        #                 JOIN maneuverability ON Frame.maneuverability = maneuverability.id
        #                 JOIN Tier ON Frame.Cost < Tier.Build_Points
        #                 JOIN size ON Frame.size = size.id
        #                 JOIN power_core ON power_core.id = power_core_size.power_core_id
        #                 JOIN power_core_size ON Frame.size = power_core_size.size
        #                 JOIN thrusters ON Frame.size = thrusters.size
        #                 WHERE """ + conditions + """;"""
        return sql_statement
    except ValueError as error:
        print("error in query_construction: ", error)
        return None
