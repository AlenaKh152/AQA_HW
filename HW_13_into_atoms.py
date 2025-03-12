import os
os.system('cls')


class IntoAtoms:
    def __init__(self, molecula):
        self.molecula = molecula
        self.result_dict = {}

    def count_atoms(self):
        atom_dict = {}
        dict_union_list = []
        open_braces = '([{'
        close_braces = ')]}'
        i = 0

        while i < len(self.molecula):
            if self.molecula[i].isalpha():
                self.process_element(i, atom_dict)
            elif self.molecula[i] in open_braces:
                dict_union_list.append(atom_dict)
                atom_dict = {}
            elif self.molecula[i] in close_braces:
                atom_dict = self.process_close_brace(i, atom_dict, dict_union_list)

            i += 1

        self.result_dict = atom_dict
        return self.result_dict

    def process_element(self, i, atom_dict):
        j = i + 1
        if j < len(self.molecula) and self.molecula[j].islower():
            element = self.molecula[i:j + 1]
            i += 1
        else:
            element = self.molecula[i]

        count = self.get_element_count(j)
        atom_dict[element] = atom_dict.get(element, 0) + count

    def get_element_count(self, j):
        count = 0
        while j < len(self.molecula) and self.molecula[j].isdigit():
            count = count * 10 + int(self.molecula[j])
            j += 1

        return 1 if not count else count

    def process_close_brace(self, i, atom_dict, dict_union_list):
        count = self.get_element_count(i + 1)

        for elem in atom_dict:
            atom_dict[elem] *= count

        if dict_union_list:
            new_dict = dict_union_list.pop()
            for element, quantity in atom_dict.items():
                new_dict[element] = new_dict.get(element, 0) + quantity
            atom_dict = new_dict

        return atom_dict


molecula_1 = IntoAtoms('H2O')
print(molecula_1.count_atoms())

molecula_2 = IntoAtoms('Mg(OH)2')
print(molecula_2.count_atoms())

molecula_3 = IntoAtoms('K171[ON(SO3)11]2')
print(molecula_3.count_atoms())
