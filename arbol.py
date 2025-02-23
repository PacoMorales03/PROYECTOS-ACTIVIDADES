h = 0
while h <= 3: 
    h = int(input("Dame la altura del arbol: "))
    if h <= 3:
        print("Este árbol es muy bajito")
for i in range (1,h+1):
    espacios = " "*(h-i)
    asterisco= "*"*(2*i-1)
    print(espacios + asterisco)
#print(" "*(h-3),"| |")
d = max(2,h//3)
espacios_tronco = h-d//2-2
for i in range (h//5+1):
    print(" "*espacios_tronco,"|"*(d+1))
