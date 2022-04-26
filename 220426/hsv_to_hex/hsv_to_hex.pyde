###sketch for distance and rotation to hex color translation of hsv where h is rotation and is distance.  v is constant

def hsv_to_rgb(h, s, v):
    h_val = float(h)/360.0
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h_val*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

def rgb_to_hex(r, g, b):
    return '%02x%02x%02x' % (r, g, b)

def hsv_to_hex(h, s, v):

    r, g, b = hsv_to_rgb(h,s,v)

    return rgb_to_hex(r, g, b)
    

r, g, b = hsv_to_rgb(240,.2,1)
print(r, g, b)

hex_color = rgb_to_hex(r,g,b)


un_hex = unhex(hex_color)

print (hex_color)
colorMode(RGB)

background(un_hex)
