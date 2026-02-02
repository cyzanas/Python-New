e=input("File name: ")
if "gif" in e:
    print("image/gif")
elif "jpg" in e:
    print("image/jpeg")
elif "pdf" in e:
    print("application/pdf")
else:
    print("application/octet-stream")    