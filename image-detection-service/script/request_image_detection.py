import os
import uuid

import cv2
import requests

# Input Path of your Image Directory
# please make a folder named result under the input path.
path = "/home/ryan/desktop/examples/images/faces"
result_path = os.path.join(path, "result")
classes = 'all'
veichels = 'bicycle,car,motorbike,aeroplane,bus,train,truck,boat'
animals = 'bird,cat,dog,horse,sheep,cow,elephant,bear,zebra,giraffe'
sports_equipments = (
    'frisbee,skis,snowboard,sports ball,kite,baseball bat,baseball glove,skateboard,surfboard,tennis racket'
)
kitchen_utensils = 'bottle,wine glass,cup,fork,knife,spoon,bowl,microwave,oven,toaster,sink,refrigerator'
fruits_and_veggies = 'banana,apple,sandwich,orange,broccoli,carrot'
fast_food = 'hot dog,pizza,donut,cake'
misclenious = 'traffic light,fire hydrant,stop sign,parking meter,bench,backpack,umbrella,handbag,tie,suitcase,chair,sofa,potted plant,bed,dining table,toilet,tvmonitor,laptop,mouse,remote,keyboard,cell phone,book,clock,vase,scissors,teddy bear,hair drier,toothbrush'


for pic in os.listdir(path):
    print(pic)
    if pic != "result":
        frame = os.path.join(path, pic)
        data = open(frame, 'rb').read()
        rq = {'frame': data, 'claases_to_detect': animals, 'id_': str(uuid.uuid4())}

        res = requests.post(f'http://localhost:5000/api/1/example/detect?classes_to_detect={classes}', files=rq)
        response_dict = res.json()
        img = cv2.imread(frame)
        print(response_dict)
        for i in response_dict:
            print(i, response_dict[i]['bbox'])
            coor = response_dict[i]['bbox']
            c1, c2 = (coor[0], coor[1]), (coor[2], coor[3])
            cv2.rectangle(img, c1, c2, (255, 255, 0), 2)

        cv2.imwrite(os.path.join(result_path, pic), img)
