import viz #insert modules
import vizshape
import vizfx
import vizact
import vizconnect

#Start empty world
#viz.go() #create empty world
#viz.setMuliSample(4)
vizconnect.go("vizconnect_config.py")


room = viz.addChild("room.osgb") #import the 3D model

viz.MainView.move([0,0,-1])
viz.MainWindow.fov(60)
vizshape.addAxes()

ground = viz.addChild("ground_grass.osgb")

env = viz.addEnvironmentMap("sky.jpg")
sky = viz.add("skydome.dlc")
sky.texture(env)

#stop collisions and gravity
viz.MainView.collision(viz.ON)
viz.MainView.gravity(10)
print("Rare: silver was late to class, well he doesnt care about this class")

headlight = viz.MainView.getHeadLight()
headlight.disable() # deactivate scene headlight

#Reduce ambient light

#Add a spot light
mylight=vizfx.addSpotLight(spread=50, pos(0,1.5,0), color=viz.WHITE, texture="porcelain.jpg")
mylight=serIntensity(10)

flame = room.getChild("flame", flags=viz.CHILD_REPLACE_TRANSFORM)
flame_position = flame.getPosition()
print(flame_position)

candle_light = vizfx.addPointLight(color=viz.RED, pos=flame_position)
candle_light_position = candle_light.getPosition()
print(candle_light_position)

candle_light.quadraticAttenuation(1)
candle_light.intensity(8)

flame.specular(viz.YELLOW)
flame.shininess(10)

def candle_off(x, y):
	x.disable()
	y.visible(viz.OFF)

vizact.onkeydown("b", candle_off, candle_light, flame)
vizact.onkeydown("n", candle.enable, candle_light, flame)

#turn the headlight back with keypress
vizact.onkeydown(" ", headlight.enable)


light1=vizfx.addPointLight(color = viz.WHITE, pos = (0,3,0))
light1=vizfx.addPointLight(color = viz.WHITE, pos = (0,-90,0))

#set light parameters
"""light1 = vizfx.addPointLight(color = viz.RED)
light1.position(0, 3,0)
light1.direction(0,0,1)
light1.spread(30)
light1.intensity(2)
light1.spotexponent(3)"""

#Add white point light
light2 = vizfx.addPointLight(color=viz.WHITE,pos=(0,3,0))

#Add white directional light pointing up
light3 = vizfx.addDirectionalLight(color=viz.WHITE,euler=(0,-90,0))

#Open / close the door
door1=room.getTransform("PivotDoor001")

def spinDoor(door , degrees):
	spinAction=vizact.spin(0,0,1,degrees,2)
	door.addAction(spinAction)

vizact.onkeydown("o",spinDoor,door1,40)
vizact.onkeydown("c",spinDoor,door1,-40)

# Add and walk avatar
vicky=viz.add("vcc_female.cfg",euler=(180,0,0))
vicky.setPosition([-1,0,1],viz.ABS_GLOBAL)
vicky.execute(5)
vicky.state(14)

def walkAvatar():
	walk1=vizact.walkTo([1.4,0,0])
	vicky.addAction(walk1)

vizact.onkeydown("w",walkAvatar)

def picker():
	object=viz.pick(info=True)
	if(object.valid):
		print(object.name)


vizact.onmousedown(viz.MOUSEBUTTON_MIDDLE, picker)

#-----------GRAB OBJECTS-----------#
cup1=room.getChild("cup001")
cup2=room.getChild("cup002")

shapes = [cup1, cup2]

#Code to get the grabber tool bu name and suply the
grabber = vizconnect.getRawTool('grabber')
grabber.setItems(shapes)

#Increase the Field of View
viz.MainWindow.fov(60)

#Show text when we point an object
text3D=viz.addText3D("MY HOUSE 3D", pos=[0,5,-8], align=viz.ALIGN_CENTER_BOTTOM)
text2D=viz.addText("MY HOUSE 2D", pos=[0,4,-8], align=viz.ALIGN_CENTER_BOTTOM)
testScreen=viz.addText("MY HOUSE ON SCREEN", parent=viz.ORTHO, pos=[20,20,0], fontSize=50)

text3D.addAction(vizact.spin(0,1,0,15))
text2D.addAction(vizact.spin(0,1,0,-15))

cfg=vizconfig.BasicConfigurable("My House 3D")
cfg.addFloatRangeItem("Thickness", [0.01,0.5], fset=text3D.setThickness, fget=test3D.getThickness)
vizconfig.register(cfg)
vixconfig.getConfigwindow().setWindowsVisible(True)

#add a video
myVideo.viz.addVideo("mona.mpg")
myScreen=room.getChild("painting001")
myScreen.texture(myVideo)

myVideo.play()
myVideo.loop()
myVideo.setRate(0.51)

#add sound
mySound = viz.addAudio("bach_air.mid")
vizact.onkeydown("p", mySound.play)
vizact.onkeydown("s", mySound.stop)