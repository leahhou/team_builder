from team_building_system import TeamBuildingSystem
from profile import Login
from algorithm import Person
from event import Event

def bootstrap_system():
    system = TeamBuildingSystem()

    user1 = Login("hello", "world", "participant")
    user2 = Login("a", "a", "participant")
    user3 = Login("b", "b", "participant")
    user4 = Login("c", "c", "participant")
    user5 = Login("d", "d", "participant")
    user6 = Login("e", "e", "participant")
    user7 = Login("f", "f", "participant")
    user8 = Login("g", "g", "participant")
    user9 = Login("h", "h", "participant")
    user10 = Login("i", "i", "participant")
    user11 = Login("j", "j", "participant")
    user12 = Login("k", "k", "participant")
    user13 = Login("l", "l", "participant")
    user14 = Login("m", "m", "participant")
    user15 = Login("n", "n", "participant")
    user16 = Login("o", "o", "participant")
    user17 = Login("p", "p", "participant")
    user18 = Login("q", "q", "participant")
    user19 = Login("r", "r", "participant")
    user20 = Login("s", "s", "participant")
    user21 = Login("t", "t", "participant")
    user22 = Login("u", "u", "participant")
    user23 = Login("v", "v", "participant")
    user24 = Login("w", "w", "participant")
    user25 = Login("x", "x", "participant")
    user26 = Login("y", "y", "participant")
    user27 = Login("z", "z", "participant")
    user28 = Login("aa", "aa", "participant")
    user29 = Login("ab", "ab", "participant")
    user30 = Login("ac", "ac", "participant")
    user31 = Login("ad", "ad", "participant")
    user32 = Login("ae", "ae", "participant")
    user33 = Login("af", "af", "participant")
    user34 = Login("ag", "ag", "participant")
    user35 = Login("ah", "ah", "participant")
    user36 = Login("ai", "ai", "participant")
    user37 = Login("aj", "aj", "participant")
    user38 = Login("ak", "ak", "participant")
    user39 = Login("al", "al", "participant")
    user40 = Login("am", "am", "participant")
    user41 = Login("an", "an", "participant")
    user42 = Login("ao", "ao", "participant")
    user43 = Login("ap", "ap", "participant")
    user44 = Login("aq", "aq", "participant")
    user45 = Login("ar", "ar", "participant")
    user46 = Login("as", "as", "participant")
    user47 = Login("at", "at", "participant")
    user48 = Login("au", "au", "participant")

    system.add_login(user1)
    system.add_login(user2)
    system.add_login(user3)
    system.add_login(user4)
    system.add_login(user5)
    system.add_login(user6)
    system.add_login(user7)
    system.add_login(user8)
    system.add_login(user9)
    system.add_login(user10)
    system.add_login(user11)
    system.add_login(user12)
    system.add_login(user13)
    system.add_login(user14)
    system.add_login(user15)
    system.add_login(user16)
    system.add_login(user17)
    system.add_login(user18)
    system.add_login(user19)
    system.add_login(user20)
    system.add_login(user21)
    system.add_login(user22)
    system.add_login(user23)
    system.add_login(user24)
    system.add_login(user25)
    system.add_login(user26)
    system.add_login(user27)
    system.add_login(user28)
    system.add_login(user29)
    system.add_login(user30)
    system.add_login(user31)
    system.add_login(user32)
    system.add_login(user33)
    system.add_login(user34)
    system.add_login(user35)
    system.add_login(user36)
    system.add_login(user37)
    system.add_login(user38)
    system.add_login(user39)
    system.add_login(user40)
    system.add_login(user41)
    system.add_login(user42)
    system.add_login(user43)
    system.add_login(user44)
    system.add_login(user45)
    system.add_login(user46)
    system.add_login(user47)
    system.add_login(user48)

    profile1 = Person(0, ["py"], "fe", 0, "win", 0)
    profile2 = Person(1, ["py"], "be", 1, "learn", 10)
    profile3 = Person(2, ["py"], "fs", 1, "network", 2)
    profile4 = Person(3, ["py"], "fe", 2, "learn", 4)
    profile5 = Person(4, ["ry"], "be", 2, "win", 5)
    profile6 = Person(5, ["ry"], "fs", 0, "learn", 7)
    profile7 = Person(6, ["ry"], "fe", 1, "network", 3)
    profile8 = Person(7, ["ry"], "fe", 1, "learn", 8)
    profile9 = Person(8, ["java"], "fe", 0, "win", 8)
    profile10 = Person(9, ["java"], "be", 1, "learn", 2)
    profile11 = Person(10, ["java"], "fs", 1, "network", 5)
    profile12 = Person(11, ["java"], "fe", 2, "learn", 7)
    profile13 = Person(12, ["js"], "be", 2, "win", 2)
    profile14 = Person(13, ["js"], "fs", 0, "learn", 7)
    profile15 = Person(14, ["js"], "fe", 1, "network", 9)
    profile16 = Person(15, ["js"], "fe", 1, "learn", 10)
    profile17 = Person(16, ["c"], "fe", 0, "win", 3)
    profile18 = Person(17, ["c"], "be", 1, "learn", 3)
    profile19 = Person(18, ["c"], "fs", 1, "network", 2)
    profile20 = Person(19, ["c"], "fe", 2, "learn", 9)
    profile21 = Person(20, ["ch"], "be", 2, "win", 1)
    profile22 = Person(21, ["ch"], "fs", 0, "learn", 10)
    profile23 = Person(22, ["ch"], "fe", 1, "network", 0)
    profile24 = Person(23, ["ch"], "fe", 1, "learn", 3)
    profile25 = Person(24, ["cpp"], "fe", 0, "win", 5)
    profile26 = Person(25, ["cpp"], "be", 1, "learn", 6)
    profile27 = Person(26, ["cpp"], "fs", 1, "network", 8)
    profile28 = Person(27, ["cpp"], "fe", 2, "learn", 6)
    profile29 = Person(28, ["php"], "be", 2, "win", 3)
    profile30 = Person(29, ["php"], "fs", 0, "learn", 4)
    profile31 = Person(30, ["php"], "fe", 1, "network", 7)
    profile32 = Person(31, ["php"], "fe", 1, "learn", 4)
    profile33 = Person(32, ["html"], "fe", 0, "win", 2)
    profile34 = Person(33, ["html"], "be", 1, "learn", 10)
    profile35 = Person(34, ["html"], "fs", 1, "network", 0)
    profile36 = Person(35, ["html"], "fe", 2, "learn", 2)
    profile37 = Person(36, ["css"], "be", 2, "win", 4)
    profile38 = Person(37, ["css"], "fs", 0, "learn", 8)
    profile39 = Person(38, ["css"], "fe", 1, "network", 9)
    profile40 = Person(39, ["css"], "fe", 1, "learn", 3)
    profile41 = Person(40, ["perl"], "fe", 0, "win", 5)
    profile42 = Person(41, ["perl"], "be", 1, "learn", 5)
    profile43 = Person(42, ["perl"], "fs", 1, "network", 5)
    profile44 = Person(43, ["perl"], "fe", 2, "learn", 3)
    profile45 = Person(44, ["swift"], "be", 2, "win", 7)
    profile46 = Person(45, ["swift"], "fs", 0, "learn", 9)
    profile47 = Person(46, ["swift"], "fe", 1, "network", 2)
    profile48 = Person(47, ["swift"], "fe", 1, "learn", 1)
    
    system.add_profile(profile1)
    system.add_profile(profile2)
    system.add_profile(profile3)
    system.add_profile(profile4)
    system.add_profile(profile5)
    system.add_profile(profile6)
    system.add_profile(profile7)
    system.add_profile(profile8)
    system.add_profile(profile9)
    system.add_profile(profile10)
    system.add_profile(profile11)
    system.add_profile(profile12)
    system.add_profile(profile13)
    system.add_profile(profile14)
    system.add_profile(profile15)
    system.add_profile(profile16)
    system.add_profile(profile17)
    system.add_profile(profile18)
    system.add_profile(profile19)
    system.add_profile(profile20)
    system.add_profile(profile21)
    system.add_profile(profile22)
    system.add_profile(profile23)
    system.add_profile(profile24)
    system.add_profile(profile25)
    system.add_profile(profile26)
    system.add_profile(profile27)
    system.add_profile(profile28)
    system.add_profile(profile29)
    system.add_profile(profile30)
    system.add_profile(profile31)
    system.add_profile(profile32)
    system.add_profile(profile33)
    system.add_profile(profile34)
    system.add_profile(profile35)
    system.add_profile(profile36)
    system.add_profile(profile37)
    system.add_profile(profile38)
    system.add_profile(profile39)
    system.add_profile(profile40)
    system.add_profile(profile41)
    system.add_profile(profile42)
    system.add_profile(profile43)
    system.add_profile(profile44)
    system.add_profile(profile45)
    system.add_profile(profile46)
    system.add_profile(profile47)
    system.add_profile(profile48)

    event = Event("here", "host", "hackathon")
    event.add_participant(profile1)
    event.add_participant(profile2)
    event.add_participant(profile3)
    event.add_participant(profile4)
    event.add_participant(profile5)
    event.add_participant(profile6)
    event.add_participant(profile7)
    event.add_participant(profile8)
    event.add_participant(profile9)
    event.add_participant(profile10)
    event.add_participant(profile11)
    event.add_participant(profile12)
    event.add_participant(profile13)
    event.add_participant(profile14)
    event.add_participant(profile15)
    event.add_participant(profile16)
    event.add_participant(profile17)
    event.add_participant(profile18)
    event.add_participant(profile19)
    event.add_participant(profile20)
    event.add_participant(profile21)
    event.add_participant(profile22)
    event.add_participant(profile23)
    event.add_participant(profile24)
    event.add_participant(profile25)
    event.add_participant(profile26)
    event.add_participant(profile27)
    event.add_participant(profile28)
    event.add_participant(profile29)
    event.add_participant(profile30)
    event.add_participant(profile31)
    event.add_participant(profile32)
    event.add_participant(profile33)
    event.add_participant(profile34)
    event.add_participant(profile35)
    event.add_participant(profile36)
    event.add_participant(profile37)
    event.add_participant(profile38)
    event.add_participant(profile39)
    event.add_participant(profile40)
    event.add_participant(profile41)
    event.add_participant(profile42)
    event.add_participant(profile43)
    event.add_participant(profile44)
    event.add_participant(profile45)
    event.add_participant(profile46)
    event.add_participant(profile47)
    event.add_participant(profile48)

    system.add_event(event)
    

    return system