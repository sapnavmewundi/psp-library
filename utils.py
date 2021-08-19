from models.tab import *


class Util:
    @staticmethod
    def insert_all_combinations(session, finalresult, seq_type):
        for comb in finalresult:
            first = comb[0]
            second = comb[1]
            rms = comb[2]
            result = AllCombinations()
            #first
            result.fragment_one = first.fragment
            result.start_one = first.start
            result.end_one = first.end
            result.resolution_one = first.resolution
            result.chain_id_one = first.chain_id
            result.protein_id_one = first.protein_id
            #second
            result.fragment_two = second.fragment
            result.start_two = second.start
            result.end_two = second.end
            result.resolution_two = second.resolution
            result.chain_id_two = second.chain_id
            result.protein_id_two = second.protein_id

            result.rms = rms
            result.seq_type = seq_type
            result.fragment_type = Util.find_type(first.fragment)
            session.add(result)
        session.commit()

    @staticmethod
    def find_type(seq):
        vals = []
        indexes = []
        for x in range(0, len(seq) + 1, 3):
            indexes.append(x)
        count = 0
        while count < len(indexes):
            if count == len(indexes) - 2:
                vals.append(seq[indexes[count]:indexes[count + 1]])
                break
            vals.append(seq[indexes[count]:indexes[count + 1]])
            count += 1
        countval = {}
        for k in vals:
            if k not in countval:
                countval[k] = str(vals.count(k))
        return ''.join(countval.values())

    @staticmethod
    def get_sup_atoms(structure, ch, seqval):
        atoms = []
        for chain in structure.get_chains():
            if chain.get_id() == ch:
                res = [residue.get_atoms() for residue in chain.get_residues() \
                        if residue.get_id()[1] == seqval]

                #res = [residue.get_atoms() for residue in
                # structure.get_residues()
               #if residue.get_id()[1] == seqval]
                for atm in res:
                    atoms += [a for a in atm]
                return atoms

    @staticmethod
    def get_table_name(index):
        if index == 3:
            return Tab3
        elif index == 4:
            return Tab4
        elif index == 5:
            return Tab5
        elif index == 6:
            return Tab6
        elif index == 7:
            return Tab7
        elif index == 8:
            return Tab8
        elif index == 9:
            return Tab9
        elif index == 10:
            return Tab10
        elif index == 11:
            return Tab11
        elif index == 12:
            return Tab12
        elif index == 13:
            return Tab13
        elif index == 14:
            return Tab14
        elif index == 15:
            return Tab15
        elif index == 16:
            return Tab16
        elif index == 17:
            return Tab17
        elif index == 18:
            return Tab18
        elif index == 19:
            return Tab19
        elif index == 20:
            return Tab20
        elif index == 21:
            return Tab21
        elif index == 22:
            return Tab22
        elif index == 23:
            return Tab23
        elif index == 24:
            return Tab24
        elif index == 25:
            return Tab25
        elif index == 26:
            return Tab26
        elif index == 27:
            return Tab27
        elif index == 28:
            return Tab28
        elif index == 29:
            return Tab29
        elif index == 30:
            return Tab30
        elif index == 31:
            return Tab31
        elif index == 32:
            return Tab32
        elif index == 33:
            return Tab33
        elif index == 34:
            return Tab34
        elif index == 35:
            return Tab35
        elif index == 36:
            return Tab36
        elif index == 37:
            return Tab37
        elif index == 38:
            return Tab38
        elif index == 39:
            return Tab39
        elif index == 40:
            return Tab40
        elif index == 41:
            return Tab41
        else:
            return None




