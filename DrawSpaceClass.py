class DrawSpace:

    def __init__(self, width, height):
        self.__layersArray = []
        self.__width = width
        self.__height = height

    def get_DrawSpace_dimensions(self):
        return (self.__width, self.__height)

    def putLayerIntoDrawspace(self, LayerObj):
        self.__layersArray.append(LayerObj)

    def getLayerArrayBelongsToDrawspace(self):
        return self.__layersArray

    def getLayersNamesInDrawSpace(self):
        layerNamesArray = []
        for i in self.__layersArray:
            layerNamesArray.append(i.getColorName())
        return layerNamesArray

    def getLayerObjByColorName(self,colorName):
        for x in self.__layersArray:
            if x.getColorName() == colorName: return x
        return None