import math
import random

class Person:
    def __init__(self, languages, position, experience, objective, idea):
        self.languages = languages #list of strings, only need language 1 to match
        self.position = position #strings - frontend, backend, fullstack
        self.experience = experience #int from 0-3
        self.objective = objective #string Prize, Learn, Network, Other
        self.idea = idea/5 #scale from 0-2
        self.preferences = {} # Key: Person, Value: Int
        self.rankings = [] # list of Person objects
        self.inGroup = False
        self.groupMembers = []

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
        self.preferences[toCompare] = pref

    def inGroup():
        if(len(groupMembers)==0):
            return False
        return True

def basicSort(people, groupSize):
    for run in range(0,5): # do 5 runs of algorithm, find best grouping
        random.shuffle(people)
        for i in range(0,math.ceil(len(people)/groupSize)-1):
            group1 = people[i*k:i*(k+1)]
            group2 = people[i*(k+1):min(i*(k+2),len(people))] #getting the 2 groups to compare rankings etc

            for person in group1: # getting rankings in each group
                for toCompare in group2:
                    person.compare(toCompare)
                person.genRankings()

            for person in group2: # getting rankings in each group
                for toCompare in group1:
                    person.compare(toCompare)
                person.genRankings()

            while(len(group1) > 0): # while there are still groups to be matched with singles
                asker = group1[0] #get asker, and who is asking
                toAsk = asker.rankings.pop(0)
                if not toAsk.inGroup(): # if not in a group, add the person to the group and remove the asker from their group
                    toAsk.groupMembers.append(asker)
                    asker.groupMembers.append(toAsk)
                    group1.remove(asker)
                else:
                    if
