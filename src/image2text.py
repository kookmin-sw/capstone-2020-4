import os

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description
    #
    # for text in texts:
    #     print("{}".format(text.description))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        #
        # print('bounds: {}'.format(','.join(vertices)))
        # print(vertices[0])

    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))

if __name__ == "__main__":
    f = open("result.txt", "w", encoding="UTF-8")
    list = os.listdir("subtitle/")
    for file in list:
        filename = "subtitle/" + file
        f.write(filename + "\n")
        f.write(str(detect_text(filename)).replace("\n"," ") + "\n-----------\n")
