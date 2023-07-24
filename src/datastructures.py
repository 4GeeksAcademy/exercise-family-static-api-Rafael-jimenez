
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
import array
from random import randint

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name
        
        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "age": str(randint(0,90)) + " Years old",
                "last_name": last_name,
                "lucky_numbers": list(array.array('i',(randint(0,90) for i in range(0,randint(1,3)))))
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "age": str(randint(0,90)) + " Years old",
                "last_name": last_name,
                "lucky_numbers": list(array.array('i',(randint(0,90) for i in range(0,randint(1,3)))))
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "age": str(randint(0,90)) + " Years old",
                "last_name": last_name,
                "lucky_numbers": list(array.array('i',(randint(0,90) for i in range(0,randint(1,3)))))
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # new_member = {
        #     "age": member["age"],
        #     "first_name": member["first_name"],
        #     "id": member["id"],
        #     "last_name": member["last_name"],
        #     "lucky_numbers": member["lucky_numbers"]
        # }
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        for obj in self._members:
            if obj["id"] == id:
                self._members.remove(obj)
                break
        return self._members

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return None  # Si no se encuentra el miembro con el ID dado, se devuelve None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
