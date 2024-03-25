import pyNetLogo

netlogo = pyNetLogo.NetLogoLink(gui=True, threed=True)

model_path = '/GreenThreads/NetLogo_3D/Porosity.nlogo3d'
netlogo.load_model(model_path)


netlogo.command('setup')
netlogo.command('repeat 100 [ go ]')

number_of_turtles = netlogo.report('count clay')
print('Clay Count:', clay-count)


netlogo.kill_workspace()
