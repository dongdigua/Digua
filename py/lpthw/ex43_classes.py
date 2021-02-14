class scene(object):
    
    def enter(self):
        pass


class engine(object):
    
    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class death(scene):

    def enter(self):
        pass

class centralcorridor(scene):

    def enter(self):
        pass

class laser(scene):

    def enter(self):
        pass

class thebridge(scene):

    def enter(self):
        pass

class escapepod(scene):

    def enter(self):
        pass


class map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = map('central_corridor')
a_game = engine(a_map)
a_game.play()
