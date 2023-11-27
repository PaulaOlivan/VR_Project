import viz
import vizshape
import vizfx
import vizact

viz.go()

room = viz.addChild("room.osgb")

viz.MainView.move([0, 0, -15])

viz.MainWindow.fov(60)
vizshape.addAxes()

ground = viz.addChild("ground_grass.osgb")

env = viz.addEnvironmentMap("sky.jpg")
sky = viz.add("skydome.dlc")
sky.texture(env)
viz.MainView.collision(viz.ON)
viz.gravity(0)

headlight = viz.MainView.getHeadLight()
headlight.disable()

flame = room.getChild("flame", flags=viz.CHILD_REPLACE_TRANSFORM)
flame_position = flame.getPosition()
print(flame_position)

candle_light = vizfx.addPointLight(color=viz.YELLOW, pos=flame_position)
candle_light_position = candle_light.getPosition()
print(candle_light_position)

viz.link(flame, candle_light)
candle_light.quadraticAttenuation(1)
candle_light.intensity(8)

flame.specular(viz.YELLOW)
flame.shininess(10)

def candle_off(x, y):
	x.disable()
	y.visible(viz.OFF)
	
vizact.onkeydown("b", candle_off, candle_light, flame)

vizact.onkeydown(" ", headlight.enable)
vizact.onkeydown(" ", headlight.disable)

#light1 = vixf.addPointlight(color = viz.WHITE, pos(0, 0, 3))
#light2 = vixf.addDirectionalLight(color = viz.WHITE, euler(0, -90, 0))

light1.position(0, 0, 0)
light1.direction(0, 0, 0)
light1.spread(30)
light1.intensity(2)
