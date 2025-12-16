import femm

class Model:
    def __init__(self, radius, symetric):
        self.symetric = symetric
        self.blocks = []
        self.materials = []
        
        femm.openfemm() 
        femm.newdocument(0)
        
        if symetric == True:
            femm.mi_probdef(0,'millimeters','axi',1e-8,0,30);
            femm.mi_drawline(0, -radius, 0, radius)
            
        else:
            femm.mi_probdef(0,'millimeters','planar',1e-8,0,30);
            femm.mi_drawarc(0, radius, 0, -radius, 180, 30)
            
        femm.mi_drawarc(0, -radius, 0, radius, 180, 30)
        femm.mi_getmaterial('Air')
        femm.mi_addblocklabel(radius-0.1, 0)
        femm.mi_selectlabel(radius-0.1, 0)
        femm.mi_setblockprop('Air', 0, 0, 0, 0, 0, 0)
        femm.mi_clearselected()
        
    def addBlock(self, material, direction = 0):
        block = Block(self, str(material), direction)
        self.blocks.append(block)
        return block    
    
    def drawAll(self):
        for x in self.blocks:
            x.draw()
        
    def createMaterial(self, matName, ux, uy, hC, j, cDuct, lamD, phiHMax, lam, phiHx, phiHy, nstr, dwire):
        material = Material(matName, ux, uy, hC, j, cDuct, lamD, phiHMax, lam, phiHx, phiHy, nstr, dwire, True)
        return material
    
    def loadMaterial(self, matName):
        material = Material(matName)
        
        return material
    
class Block:
    def __init__(self, model, material, coords = None, direction = 0):
        self.model = model
        self.material = material
        self.direction = direction
        self.coords = coords
        
    def getForce(self):
        femm.mi_saveas('blah' + str(self.x) + str(self.y) + '.fem')
        femm.mi_analyze()
        femm.mi_loadsolution()
        femm.mo_selectblock(self.x, self.y)
        return(femm.mo_blockintegral(19))
    
    def setCoords(self, coords):
        self.coords = coords
    
    def draw(self):
        coords = self.coords
        femm.mi_getmaterial(self.material)
        if len(self.coords)%2 == 0:
            for i in range(0, len(coords), 2): femm.mi_drawline(coords[i], coords[i+1], coords[(i+2)%len(coords)], coords[(i+3)%len(coords)])

        xMax, yMax = max(coords[::2]), max(coords[1::2])
        self.x,self.y = xMax-0.1*xMax, yMax-0.1*yMax
        
        femm.mi_addblocklabel(self.x, self.y)
        femm.mi_selectlabel(self.x, self.y)
        femm.mi_setblockprop(self.material, 0, 2, 0, self.direction, 0, 0)
        femm.mi_clearselected()
        
class Material:
    def __init__(self, matName=None, ux=None, uy=None, hC=None, j=None, cDuct=None, lamD=None, phiHMax=None, lam=None, phiHx=None, phiHy=None, nstr=None, dwire=None, create = False):
        self.matName = matName
        if create:
            femm.mi_addmaterial(matName, ux, uy, hC, j, cDuct, lamD, phiHMax, lam, phiHx, phiHy, nstr, dwire)
        else:
            femm.mi_getmaterial(matName)
            
    def __str__(self):
        return self.matName
