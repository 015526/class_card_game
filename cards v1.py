import randomsuit=['diamonds','hearts','spades','clubs']value=[1,2,3,4,5,6,7,8,9,10]colour=['red','black']faceup=[True,False]names=['the','of'] #['the',colour,value,'of',suit]class Card(object):    def __init__(self,suit,value,colour,points,faceup):        self.suit = suit        self.value = value               self.colour = colour        self.points = points        self.faceup = faceup    def __str__(self):        y=''        y+="suit: "+str(self.suit)+'\n'        y+="value: "+str(self.value)+'\n'        y+="colour: "+str(self.colour)+'\n'        y+="points: "+str(self.points)+'\n'        y+="card position: "+str(self.faceup)+'\n'        return y        def getsuit(self):                return self.suit    def getvalue(self):        return self.value    def getcolour(self):        return self.colour    def getpoints(self):        return self.points    def getpoints(self):        return self.points    def getfaceup(self):        return self.faceup    def setfaceup(self):        self.faceup = z        #print(self.faceup)    def setshortname(self):            names.insert(2,self.suit)            names.insert(1,self.colour)            names.insert(2,self.value)            print(names)            card = Card(random.choice(suit),random.choice(value),random.choice(colour),0,random.choice(faceup))card.setshortname()def choice_faceup(faceup):    x = input("face up or face down, True/False: ")    global z    z = x.title()    if bool(z) in faceup:        card.setfaceup()    else:        choice_faceup(faceup)choice_faceup(faceup)def Hand(object):    def __init__(self,h
