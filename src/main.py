import argparse
import os

flow_f = open("flow_result.txt", "r")
rgb_f = open("rgb_result.txt", "r")

# while True:
#     check_flow_line = flow_f.read().split("----\n")[0]
#     check_rgb_line = rgb_f.read().split("----\n")[0]
parser = argparse.ArgumentParser(description='PyTorch Two-Stream Action Recognition')
parser.add_argument('--video', default='', type=str,
                    help='input video')

args = parser.parse_args()
list = args.video

video_list = os.listdir(list)
result = []
check = []
for video in video_list:
    result = []
    flow_line = flow_f.readline().split("\n")[0]
    rgb_line = rgb_f.readline().split("\n")[0]
    if flow_line == video:
        print(flow_line)
        while True:
            flow_line = flow_f.readline().split("\n")[0]
            rgb_line = rgb_f.readline().split("\n")[0]
            if flow_line == "----":
                for res in result:
                    print(res)
                    if res > 0.9:
                        check.append(video + " " + str(res))
                if rgb_line == "----":
                    break
                else:
                    print("sibal")
                    while rgb_line != "----":
                        rgb_line = rgb_f.readline().split("\n")[0]
                    break

            if not flow_line:
                break
            result.append((float(flow_line) + float(rgb_line)) / 2)

print(check)

flow_f.close()
rgb_f.close()
