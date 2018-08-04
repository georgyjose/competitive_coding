b,n,m = map(int,input().split())
keyboard = list(map(int, input().split()))
usb = list(map(int, input().split()))
keyboard.sort(reverse=True)
usb.sort(reverse=True)

for i in usb:
    if i>b:
        usb.remove(i)
for i in keyboard:
    if i>b:
        usb.remove(i)

i = 0
count = -1
while(i<len(keyboard)):
    j = 0
    while(j<len(usb)):
        if ((keyboard[i] + usb[j])<b) and ((keyboard[i] + usb[j])>count):
            count = keyboard[i] + usb[j]
        j += 1
    i += 1
print (count)