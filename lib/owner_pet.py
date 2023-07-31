class PET_TYPES:
    all=["dog", "cat","rodent", "bird", "reptile", "exotic"]

    def __init__(self, pet_type):
        if not isinstance(pet_type, str) or pet_type not in PET_TYPES.all:
            raise Exception("pet_type must be one of the following: dog, cat, rodent, bird, reptile, exotic")
        self._pet_type=pet_type
    @classmethod
    def validate(cls, pet_type):
        if pet_type not in cls.all:
            raise Exception("woah!")

class Pet:
    all=[]
    PET_TYPES=PET_TYPES.all

    def __init__(self, name, pet_type, owner=None):
        PET_TYPES.validate(pet_type)
        self._name=name
        self._pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Bitch!")
            owner.add_pet(self)
    def set_owner(self, owner):
        self.owner=owner
  
    

    @property
    def pet_type(self):
        return self._pet_type
    
    @property
    def name(self):
        return self._name

class Owner:
    def __init__(self, name):
        self._name=name
        self._pets=[]
    def pets(self):
        return self._pets
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("no!")
        pet.set_owner(self)
        self._pets.append(pet)
            
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet._name)
    pass

    @property
    def name(self):
        return self._name

