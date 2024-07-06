import requests
import base64
import cv2 as cv

def text_get(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.4cf79942e7aaca08f0775f5354253ded.2592000.1722743178.282335-89995416'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    Text=''
    if response:
        data = response.json()   
        for item in data['words_result']:
            Text += item['words']
            if not data['words_result']:
                break
    #print("Text:",Text)
    return img, Text
def num_get(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.02bddb79f75c69034da8aa0d6133c635.2592000.1722756894.282335-89995416'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        for item in data['words_result']:
            if len(item['words'])==12:
                num = item['words']
                location = item['location']
                x1 = location['left']
                y1 = location['top']
                x2 = x1 + location['width']
                y2 = y1 + location['height']
                cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                text = 'Recognized encoding'
                position = (x1, y1-2)
                font = cv.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                color = (0, 0, 0)  # 红色
                thickness = 2
                img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
    return img, str(num)