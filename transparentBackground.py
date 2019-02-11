from PIL import Image

def convertToPNG():
  img = Image.open('./1.jpg')
  img = img.convert("RGBA")
  datas = img.getdata()
  newData = []
  for item in datas:
      if item[0] == 0 and item[1] == 0 and item[2] == 0: # 255 is white, while 0 is black.
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  img.putdata(newData)
  img.save("./TransparentImage.png", "PNG")
  print('Done')

convertToPNG()
