import json

with open('sample_data.json') as file:
    json_data = json.load(file) 
    print('''
    Interface Status
    ================================================================================
    DN                                                 Description           Speed    MTU  
    -------------------------------------------------- --------------------  ------  ------
    ''')
    imdata = json_data['imdata']
    for item in imdata:
        o_item = item['l1PhysIf']
        attr = o_item['attributes']
        dn = attr['dn']
        speed = attr['speed']
        mtu = attr['mtu']
        out = ''
        if len(dn) == 42:
            out += dn + '                              ' + speed + '   ' + mtu
        else:
            out += dn + '                              ' + speed + '   ' + mtu
        print(out)