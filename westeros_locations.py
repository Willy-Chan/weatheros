import os
from PIL import Image

def format_descriptions(descr_dict, DESCRIPTIONS_FILE):
    """
    This function formats the descriptions in the weather_descriptions.txt file
    """
    with open(DESCRIPTIONS_FILE, 'r') as f:
        for line in f:
            line = line.strip()  # remove newline characters
            line_parts = line.split("|")  # split the line into two parts based on the comma separator
            descr_dict[line_parts[0]] = line_parts[1]  # add the parts to the dictionary with line1 as key and line2 as value

    return descr_dict

def format_images(img_dict, img_folder_path):
    """
    This function formats the images in the images folder into a dict
    """
    for filename in os.listdir(img_folder_path):
        if filename.endswith(".jpg"):
            img_dict[filename[:-4]] = filename  # add the parts to the dictionary with line1 as key and line2 as value
        else:
            continue
    print(img_dict)
    return img_dict

def get_westeros_location(weather, descr_dict, img_dict):
    """
    This function defines the conditions for each of the locations. A list of locations can be found in the weather descriptions.txt file
    """
    temp = weather['main']['temp']
    weather_condition = weather['weather'][0]['main']

    if weather_condition == "Rain" or weather_condition == "Drizzle":
        return {"name": "The Iron Islands", "image": img_dict["The Iron Islands"],
                "description": descr_dict["The Iron Islands"]}
    elif temp >= 30:
        return {"name": "Dorne", "image": img_dict["Dorne"], "description": descr_dict["Dorne"]}
    elif temp < 0:
        return {"name": "Beyond the Wall", "image": img_dict["Beyond the Wall"],
                "description": descr_dict["Beyond the Wall"]}
    elif weather_condition == "Snow":
        return {"name": "Winterfell", "image": img_dict["Winterfell"], "description": descr_dict["Winterfell"]}
    elif weather_condition == "Clear":
        if temp > 20:
            return {"name": "King's Landing", "image": img_dict["King's Landing"],
                    "description": descr_dict["King's Landing"]}
        else:
            return {"name": "The Wall", "image": img_dict["The Wall"], "description": descr_dict["The Wall"]}
    elif weather_condition == "Clouds":
        if temp > 20:
            return {"name": "Braavos", "image": img_dict["Braavos"], "description": descr_dict["Braavos"]}
        else:
            return {"name": "The North", "image": img_dict["The North"], "description": descr_dict["The North"]}
    elif weather_condition == "Thunderstorm":
        return {"name": "Meereen", "image": img_dict["Meereen"], "description": descr_dict["Meereen"]}
    else:
        return {"name": "Unknown Location", "image": img_dict["Unknown Location"],
                "description": descr_dict["Harrenhall"]}


if __name__ == '__main__':
    pass
