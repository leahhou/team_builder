import math
import random
import copy

class Person:
    def __init__(self, id, languages, position, experience, objective, idea):
        self._id = id
        self.languages = languages #list of strings, only need language 1 to match
        self.position = position #strings - frontend, backend, fullstack
        self.experience = experience #int from 0-3
        self.objective = objective #string Prize, Learn, Network, Other
        self.idea = idea/5 #scale from 0-2
        self.preferences = {} # Key: Person, Value: Int
        self.rankings = [] # list of Person objects
        self.groupMember = None
        self.events = []
        self.placeholder = False

    def genRankings(self):
        self.rankings = sorted(self.preferences.items(), key=lambda vals: vals[1], reverse=True)
        for i in range(0,len(self.rankings)):
            self.rankings[i] = self.rankings[i][0]

    def compare(self,toCompare): # Compare 2 individuals
        if(toCompare.placeholder):
            return 1
        pref = 0
        for lang in self.languages:
            if lang in toCompare.languages:
                pref += 2
                break
        if self.position != toCompare.position:
            pref+=1
        if self.objective == toCompare.objective:
            pref += 1
        pref += abs(self.experience-toCompare.experience) + abs(self.idea - toCompare.idea)
        return pref
    
    @property
    def getPreferences(self):
        return self._preferences
    @preferences.setter
    def setPrefernces(self,preferences):
        self._preferences = replace
    @property
    def getRankings(self):
        return self._rankings
    @rankings.setter
    def setRankings(self,rankings):
        self._rankings = rankings
    @property
    def getGroupMember(self):
        return self._groupMember
    @groupMember.setter
    def setGroupMember(self,groupMember):
        self._groupMember = groupMember
    @property
    def getEventId(self):
        return self._eventId
    @eventId.setter
    def setEventId(self,eventId):
        self._eventId = eventId
    @property
    def isPlaceholder(self):
        return self._placeholder
    @placeholder.setter
    def setIsPlaceholder(self,placeholder):
        self._placeholder = placeholder
    
    def inGroup(self):
        if(self.groupMember == None):
            return False
        return True

    def __repr__(self):
        return self.languages[0]

def groupSatisfaction(group):
    output = 0
    for i in range(0,len(group)):
        for j in range(0,len(group)):
            if(i!=j):
                output += group[i].compare(group[j])
    return output

def basicSort(people, groupSize):

    allGroups = []
    for run in range(0,20): # do 5 random runs of algorithm, find best grouping
        peopleCopy = copy.deepcopy(people)
        print("RUN: " + str(run),end = ": ")
        random.shuffle(people)
        while(len(peopleCopy)%groupSize != 0):
            blank = Person(-1, [""],"",0,"",0)
            blank.setIsPlaceHolder(True)
            peopleCopy.append(blank)

        for i in range(0,len(peopleCopy)): #get everyones rankings of everyone else
            for j in range(0,len(peopleCopy)):
                if i!=j:
                    peopleCopy[i].preferences[peopleCopy[j]] = peopleCopy[i].compare(peopleCopy[j])
            peopleCopy[i].genRankings()

        for i in range(0,groupSize-1):

            group1 = peopleCopy[i*(len(peopleCopy)//groupSize):(i+1)*(len(peopleCopy)//groupSize)]
            group2 = peopleCopy[(i+1)*(len(peopleCopy)//groupSize):min((i+2)*(len(peopleCopy)//groupSize),len(peopleCopy))] #getting the 2 groups to compare rankings etc
            while(len(group1) > 0): # while there are still groups to be matched with singles
                asker = group1[0] #get asker, and who is asking
                for possibleAsk in asker.rankings: # highest ranking in other group
                    if possibleAsk in group2:
                        toAsk = possibleAsk
                        asker.rankings.remove(toAsk)
                        break

                if not toAsk.inGroup(): # if not in a group, add the person to the group and remove the asker from their group
                    toAsk.groupMember = asker
                    asker.groupMember = toAsk
                    group1.remove(asker)
                else: #if toAsk prefers the asker to their current group member
                    if(toAsk.rankings.index(asker)<toAsk.rankings.index(toAsk.groupMember)):
                        group1.append(toAsk.groupMember)
                        toAsk.groupMember = asker
                        asker.groupMember = toAsk
                        group1.remove(asker)

            for j in range((i+1)*(len(peopleCopy)//groupSize),min((i+2)*(len(peopleCopy)//groupSize),len(peopleCopy))): # i tells us how many group members they have
                toChange = peopleCopy[j] # want to edit this person's preferenes based on their group member
                basedOff = toChange.groupMember
                for key in toChange.preferences.keys():
                    if(key != basedOff):
                        toChange.preferences[key] = (toChange.preferences[key]+basedOff.preferences[key])/2
                peopleCopy[j].genRankings()

        #import pdb; pdb.set_trace();
        groups = []
        for i in range(0,len(peopleCopy)//groupSize):
            member = peopleCopy[i]
            newGroup = []
            while(member not in newGroup):
                newGroup.append(member)
                member = member.groupMember
            groups.append(newGroup)
        allGroups.append(groups)
        print(groups)

    satisfactions = []
    maxSatisfaction = 0
    maxIndex = 0

    for groupMatch in allGroups:
        forSum = []
        for group in groupMatch:
            forSum.append(groupSatisfaction(group))
        satisfactions.append(sum(forSum))

    for i in range(0,len(satisfactions)):
        if(satisfactions[i]>maxSatisfaction):
            maxSatisfaction = satisfactions[i]
            maxIndex = i
    return allGroups[maxIndex]
