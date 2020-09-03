
class Layer:
    __layer_quantity = 0
    __layerNamesAndPrioritiesDict = dict.fromkeys(["Red","Blue","Yellow","Purple",
                                             "White","Pink","Grey","Indigo",
                                             "Orange","Green","Brown","Silver",
                                             "Gold","Salmon","Cyan","Plum",
                                                   "Magenta","Mustard","Ochre"])

    def __init__(self,DrawSpace = None):
        self.__polygon_array = []
        self.__colorName = self.__getFreeLayerName()
        if self.__colorName is None: raise Exception("You cannot create new layer. All names were taken.")
        Layer.__layer_quantity += 1
        self.__priority = Layer.__layer_quantity
        self.__DrawSpace = DrawSpace
        if (None != DrawSpace): self.__DrawSpace.putLayerIntoDrawspace(self)



    def __getFreeLayerName(self):
        for x in Layer.__layerNamesAndPrioritiesDict:
            if Layer.__layerNamesAndPrioritiesDict[x] is None: return x
        return None

    def getColorName(self):
        return (self.__colorName)

    def set_DrawSpace(self,DrawSpace):
        self.__DrawSpace = DrawSpace

    def get_DrawSpace(self):
        return(self.__DrawSpace)

    def delete_DrawSpace(self):
        self.__DrawSpace = None

    def get_priority_of_layer(self):
        return (self.__priority)


    def put_polygon_into_layer(self,StandartPoltObj):
        self.__polygon_array.append(StandartPoltObj)

    def remove_polygon_into_layer(self,StandartPoltObj):
        self.__polygon_array.remove(StandartPoltObj)

    def get_polygon_array_belong_layer(self):
        return self.__polygon_array
