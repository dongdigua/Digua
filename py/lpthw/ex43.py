from sys import exit
class scene(object):
    
    def enter(self):
        print('oops, there is something wrong')
        exit(1)
     

class engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

        


class death(scene):

    def enter(self):
        print('you died')
        exit(1)

class centralcorridor(scene):

    def enter(self):
        print('aliens are here,\n what do you want to do next?\n1. joke 2. shoot')
        
        choice = int(input('> '))
        if choice == 1:
            print('you passed the alien\'s defence')
            return 'laster' 

        elif choice == 2:
            return 'death'
        else:
            print('I don\'t understand it')
            return 'centralcorridor'



class laser(scene):

    def enter(self):
        print('there is a bomb, and there is a keyboard on the wall, you should enter the correct passwd to pickup the bomb')

        passwd = input('> ')
        if passwd == '123456':
            print('you are right, pick up the bomb')
            return 'thebridge'
        else:
            print('you\'ve been alarmed, and you will be catched soon')
        return 'death'

class thebridge(scene):

    def enter(self):
        print('you are at the bridge, you should setup the bomb here')
        a = input('> ')
        return 'escapepod'

class escapepod(scene):

    def enter(self):
        print('YOU WIN')

class finished(scene):
    print('you won')
    exit(0)


class Map(object):

    scenes = {
            'central_corridor': centralcorridor(),
            'laser': laser(),
            'thebridge': thebridge(),
            'escapepod': escapepod(),
            'death': death(),
            'finished': finished(),
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = engine(a_map)
a_game.play()

a = scene()
a.enter()

