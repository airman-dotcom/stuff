atmos_psi_at_sea_level = 100
temp_boil_water = int(input())
if temp_boil_water >= 80 or temp_boil_water <= 200:
    atmos_psi = (5*temp_boil_water) - 400
    print(atmos_psi)
    if atmos_psi < 100:
        print(1)
    elif atmos_psi > 100:
        print(-1)
    elif atmos_psi == 100:
        print(0)
else:
    print("Error")
