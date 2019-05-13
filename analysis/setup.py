import json
import csv
import os
import sys
import requests
import shutil
import colorAnalysis

def get_features(a):
    features = ["brightness", "blockCount", "colorCount"] 
    features.extend(a.bucketer.color_bases.keys())
    gradient_types = ["mean_b_gradients_horiz", "mean_g_gradients_horiz", "mean_r_gradients_horiz", "mean_b_gradients_vert", "mean_g_gradients_vert", "mean_r_gradients_vert"]
    features.extend(gradient_types)
    return features


def add_artist(artist_json, csv_file):
    a = colorAnalysis.ColorAnalysis()

    with open(artist_json, "r") as infile, open(csv_file, mode="a+") as outfile:
        data = json.load(infile)
        print(sys.argv[1])
        
        fieldnames = ["title", "artistName", "yearAsString", "genre", "image"] 
        fieldnames.extend(get_features(a))
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        if os.stat(sys.argv[2]).st_size == 0:
            writer.writeheader()

        fieldnames_available = [x for x in fieldnames if x not in get_features(a)]
        for painting in data:
            if painting["genre"] and "abstract" in painting["genre"]: 
                p_info = {}
                for field in fieldnames_available:
                    p_info[field] = painting[field].encode('utf-8').strip()
                for feature in get_features(a):
                    p_info[feature] = None
                writer.writerow(p_info)


def form_vector(a, img_bgr):
    vector = {}

    histogram, colors_present, imageOut = a.color_breakdown(img_bgr)
    
    vector["brightness"] = a.brightness_bgr(img_bgr)
    vector["blockCount"] = a.count_blocks(img_bgr)
    vector["colorCount"] = (len(colors_present))

    colors = histogram.keys()
    # print colors
    for color in colors:
        vector[color] = histogram[color]

    color_gradients = a.color_gradients(img_bgr)
    gradients = color_gradients.keys()
    # print colors
    for gradient in gradients:
        vector[gradient] = color_gradients[gradient]
    return vector 


def fill_vectors(infile, outfile):
    a = colorAnalysis.ColorAnalysis()

    with open(infile, mode="r") as in_csv, open(outfile, mode="w") as out_csv:        
        fieldnames = ["title", "artistName", "yearAsString", "genre", "image"]
        fieldnames.extend(get_features(a))
        writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
        writer.writeheader()
        reader = csv.DictReader(in_csv)

        for row in reader:
            path = "paintings/" + row["title"] + ".jpg"
            print(path)

            if "" not in [val for key, val in row.items() if key in get_features(a)]:
                # print "vector already set"
                # print row["brightness"] == ""
                writer.writerow(row)
            else:
                is_downloaded, url = download_image(row["image"], path)
                if is_downloaded:
                    img_bgr = colorAnalysis.read_bgr(path)
                    img_bgr = colorAnalysis.resize_image(img_bgr)

                    # print histogram, present, brightness
                    vector = form_vector(a, img_bgr)
                    # print "vector value calculated: ", vector
                    for feature in vector.keys():
                        row[feature] = vector[feature]
                    row["image"] = url
                    writer.writerow(row)    
                else:
                    # print "vector value not found"
                    row["image"] = url
                    writer.writerow(row)


def download_image(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 404 and url.endswith("!Large.jpg"):
        url = url[:-10]
        r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(path, 'wb') as outname:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, outname)
        return (True, url)
    return (False, None)                   


# add_artist(sys.argv[1], sys.argv[2])
#fill_vectors(sys.argv[1], sys.argv[2])

