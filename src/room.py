
class Room:


    XY = (0, 0)  # XY coordinates of room
    present_entities = {}  # entities present in room


    def __init__(self):
        pass

    def __init__(self, coordinates):
        self.XY = coordinates

    #may pass a list of entities to begin in room
    def __init__(self, coordinates, entity_list):
        self.XY = coordinates
        for entity in entity_list:
            self.present_entities[entity.id] = entity


    # adds entity to a dictionary, using its id value to determine the key
    def add(self, entity):
        self.present_entities[entity.id] = entity

    # remove entity by id
    def rm(self, entityID):
        del self.present_entities[entityID]

