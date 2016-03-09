__author__ = 'postrowski'

# -*-coding: utf-8-*-


class MakeDict(object):

    @staticmethod
    def make_dict(list1, list2, list3):
        """
            Function makes a dictionary.
        :param list1: input list (keys())
        :param list2: input list (nested keys())
        :param list3: input list (nested values())
        :return: output dictionary ({"list1":[{"list2":"list3"}], ...})
        """
        # make dictionary {"list1":[{"list2":"list3"}], ...}
        out_dict = {i: [] for i in set(list1)}
        [out_dict[x].append(y) for (x, y) in zip(list1, zip(list2, list3))]
        # ...make inner dictionary...
        in_dict = [dict(out_dict.values()[i]) for i in range(len(out_dict))]
        # ...join outer and inner dictionary
        new_dict = {i: [j] for (i, j) in zip(out_dict.keys(), in_dict)}
        return new_dict
