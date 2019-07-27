bee_hiv, t, desired_waypoint, plant_loc = [0, 0, 0], 0, [], [[-6, 2, 40], [-4, 6, 50], [0, 6, 65], [4, 4, 35]]
pyth = lambda x, y: ((x*x)+(y*y))**0.5


def comp_path(source_node, plant_location):
    mini, i, nex_node = 800000000, 0, []

    while i < len(plant_location):

        dist = pyth((plant_location[i][0] - source_node[0]), (plant_location[i][1] - source_node[1]))

        if dist < mini:
            global t
            mini, nex_node, t = dist, plant_location[i], i

        i += 1
    global desired_waypoint
    desired_waypoint.append(nex_node)

    if len(plant_location) == 0:
        return desired_waypoint
    else:
        plant_location.pop(t)
        comp_path(nex_node, plant_location)


r = comp_path(bee_hiv, plant_loc)
desired_waypoint.append(bee_hiv)
desired_waypoint.pop(-2)
print(desired_waypoint)
