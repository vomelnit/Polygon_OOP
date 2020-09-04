##@package LayerClass
#Consist of Layer class definition


##This class create Layer object
#
# Create polygon object via array of points (exp. [(1,2),(4,3),(-4.55,6,98)] )
class Layer:
    __layer_quantity = 0
    __layerNamesAndPrioritiesDict = dict.fromkeys(["Red","Blue","Yellow","Purple",
                                             "White","Pink","Grey","Indigo",
                                             "Orange","Green","Brown","Silver",
                                             "Gold","Salmon","Cyan","Plum",
                                                   "Magenta","Mustard","Ochre"])

    ##  The constructor of Layer object
    #   @param self The object pointer
    #   @param DrawSpace Drawspace object
    def __init__(self,DrawSpace = None):
        self.__polygon_array = []
        self.__colorName = self.__getFreeLayerName()
        if self.__colorName is None: raise Exception("You cannot create new layer. All names were taken.")
        Layer.__layer_quantity += 1
        self.__priority = Layer.__layer_quantity
        self.__DrawSpace = DrawSpace
        if (None != DrawSpace): self.__DrawSpace.putLayerIntoDrawspace(self)


    ##  Return name/color of layer that can be used to identify layer
    #   @param self The object pointer
    #   @return string/None
    def __getFreeLayerName(self):
        for x in Layer.__layerNamesAndPrioritiesDict:
            if Layer.__layerNamesAndPrioritiesDict[x] is None:
                Layer.__layerNamesAndPrioritiesDict[x] = "Taken"
                return x
        return None
    ##  Return setted name/color of layer object
    #   @param self The object pointer
    #   @return string
    def getColorName(self):
        return (self.__colorName)

    ##  Bind Layer obj to Drawspace obj
    #   @param self The object pointer
    #   @param self set_DrawSpace object
    def set_DrawSpace(self,DrawSpace):
        self.__DrawSpace = DrawSpace

    ##  Return DrawSpace obj that own this Layer obj
    #   @param self The object pointer
    #   @return set_DrawSpace object
    def get_DrawSpace(self):
        return(self.__DrawSpace)

    ##  Unbind Layer obj from Drawspace obj
    #   @param self The object pointer
    def delete_DrawSpace(self):
        self.__DrawSpace = None

    ##  Return priority of layer (variable not use now)
    #   @param self The object pointer
    #   @return integer
    def get_priority_of_layer(self):
        return (self.__priority)

    ##  Bind StandartPolygon obj to this Layer obj and put it in array of polygons
    #   @param self The object pointer
    #   @param StandartPolygonObj StandartPolygon object
    def put_polygon_into_layer(self,StandartPolygonObj):
        self.__polygon_array.append(StandartPolygonObj)

    ##  Unbind StandartPolygon obj from this Layer obj and delete it from array of layer's polygons
    #   @param self The object pointer
    #   @param StandartPolygonObj StandartPolygon object
    def remove_polygon_into_layer(self,StandartPolygonObj):
        self.__polygon_array.remove(StandartPolygonObj)

    ##  Return array of StandartPolygon objects that belongs to this Layer object
    #   @param self The object pointer
    #   @return array of StandartPolygon objects
    def get_polygon_array_belong_layer(self):
        return self.__polygon_array
