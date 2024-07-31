
f(x) = (x-3)*(x-5)*(x-7)+40
p = line([(2,0),(2,f(2))], color='black')
p += line([(8,0),(8,f(8))], color='black')
p += polygon([(2,0),(2,f(2))] + [(x, f(x)) for x in [2,2.1,..,8]] + [(8,0),(2,0)],  rgbcolor=(0.8,0.8,0.8),aspect_ratio='automatic')
p += text("$\\mathrm{Area}=\\int_{a}^b f(x) dx$", (4, 55), fontsize=16, color='black')
p += plot(f, (1, 8.5), thickness=3)
p += line([(6,0),(6,f(6))], color="#8888ff")
p += text("$\\mathrm{Length}=f(x)$", (5.9, 20), fontsize=16, color='black', horizontal_alignment='right')
p