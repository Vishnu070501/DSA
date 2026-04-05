def ninja_training( matrix, day=0, last_activity=None):
    if day == len(matrix):
        return 0
    max_points_from_picking_one = None
    max_points_from_picking_two = None
    max_points_from_picking_three = None
    if last_activity !=0:
        max_points_from_picking_one = matrix[day][0] + ninja_training(matrix, day+1, 0)
    if last_activity !=1:
        max_points_from_picking_two = matrix[day][1] + ninja_training(matrix, day+1, 1)
    if last_activity !=2:
        max_points_from_picking_three = matrix[day][2] + ninja_training(matrix, day+1, 2)
    max_points_from_picking_one = max_points_from_picking_one if max_points_from_picking_one is not None else float('-inf')
    max_points_from_picking_two = max_points_from_picking_two if max_points_from_picking_two is not None else float('-inf')
    max_points_from_picking_three = max_points_from_picking_three if max_points_from_picking_three is not None else float('-inf')
    return max(max_points_from_picking_one, max_points_from_picking_two, max_points_from_picking_three)


print(ninja_training(
    [
        [10,50,1],
        [5,100,10]
    ]
))