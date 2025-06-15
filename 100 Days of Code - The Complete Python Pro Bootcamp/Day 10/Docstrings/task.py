


def format_name(f_name, l_name):
    '''Takes the firts and last name  from the funxiton converts it into title case'''
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "Yu" )

length = len(formatted_name)


