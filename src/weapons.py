import random
from enemy_data import ENEMY_TYPES

def pick_enemy_type():
    pool = []

    for name, data in ENEMY_TYPES.items():
        pool += [name] * data["weight"]

    return random.choice(pool)



WEAPONS = {
    #enemy weapons, add elites later
    "judgement": {
        "type": "rifle",
        "damage": 200,
        "ammo": 1,
        "reload": 3.0,
        "rpm": 21,
        "accuracy": 0.9
    },

    "prince": {
        "type": "rifle",
        "damage": 150,
        "ammo": 7,
        "reload": 4.0,
        "rpm": 60,
        "accuracy": 0.85
    },

    "jesse": {
        "type": "rifle",
        "damage": 130,
        "ammo": 10,
        "reload": 5.5,
        "rpm": 75,
        "accuracy": 0.75
    },

    "hellion": {
        "type": "shotgun",
        "damage": 22,
        "pellets": 9,
        "ammo": 6,
        "reload": 7.75,
        "rpm": 150,
        "accuracy": 0.55
    },

    "grace": {
        "type": "revolver",
        "damage": 120,
        "ammo": 6,
        "reload": 4.75,
        "rpm": 80,
        "accuracy": 0.85
    },

    "insurgent": {
        "type": "handgun",
        "damage": 60,
        "ammo": 20,
        "reload": None,
        "rpm": 230,
        "accuracy": 0.5
    }
}

#players weapon