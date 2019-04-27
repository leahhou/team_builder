from team_building_system import TeamBuildingSystem
from profile import Login

def bootstrap_system():
    system = TeamBuildingSystem()

    user = Login("hello", "world", "organiser")
    system.add_login(user)
    return system