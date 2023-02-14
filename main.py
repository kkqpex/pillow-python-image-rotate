from PIL import Image

def print_hi(name):
    x = int(input("Rotate Image: "))
    with Image.open(f"images/{name}") as im:
        print(im.format, im.size, im.mode)
        im.rotate(x).show()
        return im

if __name__ == '__main__':
    y = input("Name Image (with '.jpg'): ")
    print_hi(y)