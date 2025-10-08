nameFileWithType = input("File name: ").strip().lower()
extension = nameFileWithType.split('.')[-1] # if negative star with the last phrase
print(extension)


if ".git" in nameFileWithType:
  print("image/gif")
elif ".jpg" in nameFileWithType or ".jpeg" in nameFileWithType:
  print("image/jpeg")
# elif ".jpeg" in nameFileWithType:
#   print("image/jpeg")
elif ".png" in nameFileWithType:
  print("image/png")
elif ".pdf" in nameFileWithType:
  print("application/pdf")
elif ".txt" in nameFileWithType:
  print("text/plain")
elif ".zip" in nameFileWithType:
  print("application/zip")
else:
  print("application/octet-stream")



name = input("File name: ").strip().lower()

extension = name.split('.')[-1] if '.' in name else ''

mime_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

print(mime_types.get(extension, "application/octet-stream"))




import mimetypes

name = input("File name: ").strip().lower()
mime_type, _ = mimetypes.guess_type(name)
print(mime_type or "application/octet-stream")