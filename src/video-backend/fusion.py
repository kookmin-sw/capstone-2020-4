import argparse
import os

# while True:
#     check_flow_line = flow_f.read().split("----\n")[0]
#     check_rgb_line = rgb_f.read().split("----\n")[0]
parser = argparse.ArgumentParser(description='PyTorch Two-Stream Action Recognition')
parser.add_argument('--video', default='', type=str,
                    help='input video')
parser.add_argument('--label', default='', type=str,
                    help='input label')

args = parser.parse_args()
list = args.video
label = args.label
client_folder = list.split("/")[0]
flow_f = open(list + "flow_result.txt", "r")
rgb_f = open(list + "rgb_result.txt", "r")
result_f = open(list + label + "_result.txt", "w")
video_list = os.listdir(list)
result = []
for video in video_list:
    check = 0
    if video.endswith("mp4"):
        result = []
        flow_line = flow_f.readline().split("\n")[0]
        rgb_line = rgb_f.readline().split("\n")[0]
        if flow_line == video:
            while True:
                flow_line = flow_f.readline().split("\n")[0]
                rgb_line = rgb_f.readline().split("\n")[0]
                if flow_line == "----":
                    for res in result:
                        print(res)
                        if res > 0.8:
                            check += 1
                    if check >= 2:
                        result_f.write(video.split(".")[0] + '\n') 

                    if rgb_line == "----":
                        break
                    else:
                        while rgb_line != "----":
                            rgb_line = rgb_f.readline().split("\n")[0]
                        break

                if not flow_line:
                    break
                result.append((float(flow_line) + float(rgb_line)) / 2)

print(list, label)
os.system("mv " + list + label + "_result.txt ../static/" + client_folder + "/")  
flow_f.close()
rgb_f.close()
