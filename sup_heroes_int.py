import requests


def max_intel_hero():
    main_url = 'https://akabab.github.io/superhero-api/api'

    responce_Hulk = requests.get(main_url+'/powerstats/332.json')
    responce_Cap =  requests.get(main_url+'/powerstats/149.json')
    responce_Thanos =  requests.get(main_url+'/powerstats/655.json')
    heroes_dict_int = {eval(responce_Hulk.text)['intelligence']:'Hulk',eval(responce_Cap.text)['intelligence']:'Captain America',eval(responce_Thanos.text)['intelligence']:'Thanos'}
    max_intelligence = max(heroes_dict_int.keys())
    return heroes_dict_int[max_intelligence]


if __name__ == '__main__':
    print(max_intel_hero())
