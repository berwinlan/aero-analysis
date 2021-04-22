def vertical_tail_sizing():
    while True:
        L_v = float(input("Enter the vertical distance of tail to CG of aircraft (L_v):"))
        S_v = float(input("Enter the trapezoidal area of the vertical tail (S_v):"))
        S_w = float(input("Enter the wing area (S_w):"))
        mac = float(input("Enter the MAC (mean aerodynamic chord):"))

        V_v = (L_v * S_v) / (S_w * mac)
        
        if input(f"V_v = {V_v}; press Y to continue or any key to exit") != "Y":
            break

def horizontal_tail_sizing():
    while True:
        L_h = float(input("Enter the vertical distance of tail to CG of aircraft (L_v):"))
        S_h = float(input("Enter the trapezoidal area of the horizontal tail (S_h):"))
        S_w = float(input("Enter the wing area (S_w):"))
        mac = float(input("Enter the MAC (mean aerodynamic chord):"))

        V_h = (L_h * S_h) / (S_w * mac)

        if input(f"V_h = {V_h}; press Y to continue or any key to exit") != "Y":
            break
