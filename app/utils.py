# def get_population():
#   keys = ['col', 'bol']
#   values = [300, 400]
#   return keys, values

# A = 'Hola'

def get_population(conuntry_dict):
  population_dict = {
    '2022': int(conuntry_dict['2022 Population']),
    '2020': int(conuntry_dict['2020 Population']),
    '2015': int(conuntry_dict['2015 Population']),
    '2010': int(conuntry_dict['2010 Population']),
    '2000': int(conuntry_dict['2000 Population']),
    '1990': int(conuntry_dict['1990 Population']),
    '1980': int(conuntry_dict['1980 Population']),
    '1970': int(conuntry_dict['1970 Population'])
  }
  keys = population_dict.keys()
  values = population_dict.values()
  return keys, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

