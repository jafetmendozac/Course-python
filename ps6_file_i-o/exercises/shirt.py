import sys
from PIL import Image, ImageOps


path_shirtToMuped = Image.open("shirtToMuped.png")
images = [path_shirtToMuped]

def main():
  try:
    validArguments()

    image = Image.open(sys.argv[1])
    images.append(image)

    fitted_img = ImageOps.fit(images[1], images[0].size)
    images[1] = fitted_img

    images[1].paste(images[0], mask=images[0] if images[0].mode == 'RGBA' else None)

    images[1].save(sys.argv[2])
    images[1].show()
  except FileNotFoundError:
    sys.exit("Input does not exist")



def validArguments():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
  if not sys.argv[2].endswith((".jpg",".jpeg",".png")):
    sys.exit("Invalid output")
  if sys.argv[1][-4:] != sys.argv[2][-4:]:
    sys.exit("Input and output have different extensions")


if __name__ == "__main__":
  main()