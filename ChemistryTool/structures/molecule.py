from .abc import MoleculeABC
from ..algorithms import Isomorphism


class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: str, number: int):
        if not isinstance(element, str) or not isinstance(number, int):
            raise TypeError
        else:
            if element in self._atoms:
                raise ValueError
            else:
                self._atoms[number] = element
                self._bonds[number] = {}

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if not isinstance(start_atom, int):
            raise TypeError
        elif not isinstance(end_atom, int):
            raise TypeError
        elif not isinstance(bond_type, int):
            raise TypeError
        elif end_atom in self._bonds[start_atom].keys():
            raise ValueError
        elif start_atom == end_atom:
            raise ValueError
        else:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[start_atom][end_atom] = bond_type

    def __repr__(self):
        return self._atoms, self._bonds


__all__ = ['Molecule']
