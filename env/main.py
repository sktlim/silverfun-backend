import json
import copy

from shapely.geometry import Point, mapping, shape
from shapely.ops import nearest_points

def find_nearest_points(file):
    # with open(file, "r") as f:
    geojson = json.load(file)
    # print(geojson)
    ref_point = Point(103.6831, 1.3483)
    geojson_original = copy.deepcopy(geojson)

    features = []
    min_distance = None
    min_index = None

    for i, feature in enumerate(geojson["features"]):

        # Could be improved with Haversine distance, or distance in UTM coordinates for example
        p1, p2 = nearest_points(shape(feature["geometry"]), ref_point)
        distance = p1.distance(p2)

        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_index = i

        feature["properties"] = {"index": i, "distance": distance}
        features.append(feature)
        features.append(
            {
                "type": "Feature",
                "properties": {"index": f"closest_point_{i}", "distance": distance},
                "geometry": mapping(p1),
            }
        )

    features = sorted(features, key=lambda x: x["properties"]["distance"])

    # features.append(
    #     {
    #         "type": "Feature",
    #         "properties": {"index": "ref_point", "distance": 0},
    #         "geometry": mapping(ref_point),
    #     }
    # )

    inter_list = []

    for i in range(10):
        if i % 2 == 0:
            inter_list.append(features[i])
        

    index_list = []
    final_features = []
    dist_list = []

    for i in range(len(inter_list)):
        index_list.append(inter_list[i]['properties']['index'])
        dist_list.append(inter_list[i]['properties']['distance'])


    for i in index_list:
        final_features.append(geojson_original['features'][i])

    # with open("gg.geojson", "w") as f:
    return json.dumps(final_features,indent=4)
