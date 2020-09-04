##@package DrawSpaceClass
#Consist of DrawSpace class definition


##This class create DrawSpace objects which connected with Layer objects
#
# It was created to bind layers and use graphics but it is not done yet
class DrawSpace:

    ##  The constructor of DrawSpace
    #   @param self The object pointer
    #   @param width float
    #   @param height float
    def __init__(self, width, height):
        self.__layersArray = []
        self.__width = width
        self.__height = height

    ##  Return width and height of DrawSpace object
    #   @param self The object pointer
    #   @return float,float
    def get_DrawSpace_dimensions(self):
        return (self.__width, self.__height)

    ##  Bind Layer obj to DrawSpace object and put it into array of layers
    #   @param self The object pointer
    #   @param LayerObj Layer object
    def putLayerIntoDrawspace(self, LayerObj):
        self.__layersArray.append(LayerObj)

    ##  Return array of Layer objs that belong to this DrawSpace object
    #   @param self The object pointer
    #   @return array of Layer object
    def getLayerArrayBelongsToDrawspace(self):
        return self.__layersArray

    ##  Return array of Layer objects' name/color that belong to this DrawSpace object
    #   @param self The object pointer
    #   @return array of strings
    def getLayersNamesInDrawSpace(self):
        layerNamesArray = []
        for i in self.__layersArray:
            layerNamesArray.append(i.getColorName())
        return layerNamesArray

    ##  Return Layer object that has entered name/color. Layer obj belongs to this DrawSpace object
    #   @param self The object pointer
    #   @param colorName string
    #   @return string
    def getLayerObjByColorName(self,colorName):
        for x in self.__layersArray:
            if x.getColorName() == colorName: return x
        return None