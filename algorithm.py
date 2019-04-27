import math
import random

class Person:
    def __init__(self, languages, position, experience, objective, idea, eventId):
        self.languages = languages #list of strings, only need language 1 to match
        self.position = position #strings - frontend, backend, fullstack
        self.experience = experience #int from 0-3
        self.objective = objective #string Prize, Learn, Network, Other
        self.idea = idea/5 #scale from 0-2
        self.preferences = {} # Key: Person, Value: Int
        self.rankings = [] # list of Person objects
        self.inGroup = False
        self.groupMember = None
        self.eventId = eventId

    def genRankings():
        self.rankings = sorted(preferences.items(), key=lambda vals: vals[1], reverse=True).keys()

    def compare(toCompare): # Compare 2 individuals
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

    def inGroup():
        if(self.groupMember == None):
            return True
        return False

def groupSatisfaction(group):
    output = 0
    for i in range(0,len(group)):
        for j in range(0,len(group)):
            if(i!=j):
                output += group[i].compare(group[j])
    return output

def basicSort(people, groupSize):
    groupSize = groupSize - 1
    allGroups = []
    for run in range(0,5): # do 5 random runs of algorithm, find best grouping
        random.shuffle(people)
        peopleCopy = list(people)

        for i in range(0,len(people)): #get ever
            for j in range(0,len(people)):
                if(i!=j):
                    people[i].preferences[people[j]] = people[i].compare(people[j])
            people[i].genRankings()

        for i in range(0,groupSize):

            group1 = people[i*(len(people)//groupSize):(i+1)*(len(people)//groupSize)]
            group2 = people[(i+1)*(len(people)//groupSize):min((i+2)*(len(people)//groupSize),len(people))] #getting the 2 groups to compare rankings etc

            while(len(group1) > 0): # while there are still groups to be matched with singles
                asker = group1[0] #get asker, and who is asking
                toAsk = asker.rankings.pop(0) #find highest ranked in group2
                while toAsk not in group2:
                    toAsk = asker.rankings.pop(0)

                if not toAsk.inGroup(): # if not in a group, add the person to the group and remove the asker from their group
                    toAsk.groupMember = asker
                    asker.groupMember = toAsk
                    group1.remove(asker)
                else: #if toAsk prefers the asker to their current group member - rmb that index should be LESS than!
                    if(toAsk.rankings.index(asker)<toAsk.rankings.index(toAsk.groupMember)):
                        group1.append(toAsk.groupMember)
                        toAsk.groupMember.groupMember = None
                        toAsk.groupMember = asker
                        group1.remove(asker)

            for j in range((i+1)*(len(people)//groupSize),min((i+2)*(len(people)//groupSize),len(people))): # i tells us how many group members they have
                toChange = people[j] # want to edit this person's preferenes based on their group member
                basedOff = toChange.groupMember
                for key in toChange.preferences.keys():
                    toChange.preferences[key] = (toChange.preferences[key]+basedOff.preferences[key])/2
                people[j].genRankings()

        groups = []
        for i in range(0,len(people)//groupSize):
            member = people[i]
            groups.append([member])
            while(member.groupMember != None):
                groups[i].append(member.groupMember)
                member = member.groupMember
        allGroups.append(groups)

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

    return allGroups[i]
