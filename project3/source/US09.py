from util_date import Date

def birth_before_parents_death(individuals_dict, families_dict):
    for family_id, family_info in families_dict.items():
        husb_info = individuals_dict[family_info['HUSB']]
        wife_info = individuals_dict[family_info['WIFE']]
        if husb_info.get('DEAT') != None and husb_info.get('DEAT') != 'NA':
            if family_info.get('CHIL') != None and family_info.get('CHIL') != 'NA':
                for child in family_info.get('CHIL'):
                    child_info = individuals_dict[child]
                    if husb_info.get('DEAT') == "NA" or type(husb_info.get('DEAT').date_time_obj) is str or child_info.get('BIRT') == "NA" or type(child_info.get('BIRT')) is str:
                        pass
                    else:
                        try:
                            if Date.get_dates_difference(husb_info.get('DEAT').date_time_obj, child_info.get('BIRT').date_time_obj) < 0:
                                raise ValueError(f"ERROR: Husband died before the birth of his child - {family_id}")
                        except ValueError as e:
                            print(e)

        if wife_info.get('DEAT') != None and wife_info.get('DEAT') != 'NA':
            if family_info.get('CHIL') != None and family_info.get('CHIL') != 'NA':
                for child in family_info.get('CHIL'):
                    child_info = individuals_dict[child]
                    if wife_info.get('DEAT') == "NA" or type(wife_info.get('DEAT').date_time_obj) is str or child_info.get('BIRT') == "NA" or type(child_info.get('BIRT')) is str:
                        pass
                    else:
                        try:
                            if Date.get_dates_difference(wife_info.get('DEAT').date_time_obj, child_info.get('BIRT').date_time_obj) < 0:
                                raise ValueError(f"ERROR: Wife died before the birth of her child - {family_id}")
                        except ValueError as e:
                            print(e)