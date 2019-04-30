import json
import csv
import os
import sys
import requests
import shutil
import colorAnalysis

def add_artist(artist_json, csv_file):
    with open(artist_json, "r") as infile, open(csv_file, mode="a+") as outfile:
        data = json.load(infile)
        print(sys.argv[1])
        
        fieldnames = ["title", "artistName", "yearAsString", "genre", "image", "vector"] 
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        if os.stat(sys.argv[2]).st_size == 0:
            writer.writeheader()

        fieldnames_available = [x for x in fieldnames if x != "vector"]
        for painting in data:
            if painting["genre"] and "abstract" in painting["genre"]: 
                p_info = {"vector":None}
                for field in fieldnames_available:
                    p_info[field] = painting[field].encode('utf-8').strip()
                writer.writerow(p_info)


def form_vector(color_breakdown, colors_present, brightness):
    vector = []
    colors = color_breakdown.keys()
    # print colors
    for color in colors:
        vector.append(color_breakdown[color])
    vector.append(len(colors_present))
    vector.append(brightness)
    return vector 


def fill_vectors(infile, outfile):
    with open(infile, mode="r") as in_csv, open(outfile, mode="w") as out_csv:        
        fieldnames = ["title", "artistName", "yearAsString", "genre", "image", "vector"] 
        writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
        writer.writeheader()
        reader = csv.DictReader(in_csv)
        a = colorAnalysis.ColorAnalysis()

        for row in reader:
            path = "paintings/" + row["title"] + ".jpg"
            print path

            if row["vector"]:
                print "vector value preset: ", row["vector"]
                writer.writerow(row)
            else:
                is_downloaded, url = download_image(row["image"], path)
                if is_downloaded:
                    img_bgr = colorAnalysis.read_bgr(path)
                    img_bgr = colorAnalysis.resize_image(img_bgr)
                    histogram, present, imageOut = a.color_breakdown(img_bgr)
                    brightness = a.brightness_bgr(img_bgr)
                    # print histogram, present, brightness
                    vector = form_vector(histogram, present, brightness)
                    print "vector value calculated: ", vector
                    row["vector"] = vector
                    row["image"] = url
                    writer.writerow(row)    
                else:
                    print "vector value not found"
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
fill_vectors(sys.argv[1], sys.argv[2])

            


