# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".


def destCity(paths):
    fCity = []
    tCity = []

    for val in paths:
        if val[0] not in fCity:
            fCity.append(val[0])
        if val[1] not in tCity:
            tCity.append(val[1])
    for city in tCity:
        if city not in fCity:
            return city


if __name__ == "__main__":
    paths = [["London", "New York"], [
        "New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(destCity(paths))
