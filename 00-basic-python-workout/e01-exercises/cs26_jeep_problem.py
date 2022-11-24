# Jeep with N barrels of gasoline
# Jeep's tank fits exactly 1 barrel
# Jeep's tank can only be filled when empty
# Jeep's tank allows it to travel D kilometres
# Calculate the distance it can travel
# with one barrel    => D kms
# with two barrels   => 2 * D kms
# with three barrels => (D / 3) + distance(2)
# with four barrels => (D / 5) + distance(3)
# .....
# with N barrels => (D / (2 * N - 3)) + distance(N - 1)


def distance_travelled(num_barrels: int, dist_per_barrel: float) -> float:
    if num_barrels == 1:
        return dist_per_barrel
    else:
        return (dist_per_barrel / (2 * num_barrels - 3)) + distance_travelled(num_barrels - 1, dist_per_barrel)


for num_barrels in range(1, 11):
    print(f"{num_barrels} barrel{'s' if num_barrels > 1 else ''}; 100 kms per barrel: {round(distance_travelled(num_barrels, 100), 1)}")
