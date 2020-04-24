def parse(string_to_parse):
    try:
        string_without_domain = string_to_parse.split('?')[1]
    except IndexError:
        # URL не имеет параметров
        return {}
    # Отбросим якорь (#), если он есть
    if string_without_domain.find("#") != -1:
        string_without_domain = string_without_domain.split('#')[0]
    step1 = string_without_domain.replace("=", " ")
    step2 = step1.replace("&", " ")
    step3 = step2.split()
    try:
        output = {step3[i]: step3[i + 1] for i in range(0, len(step3), 2)}
    except IndexError:
        # Некорректный URL!
        print("Некорректный URL!")
        return -1
    return output

def parse_cookie(string_to_parse):
    output = {}
    # Проверим достаточно ли симолов в строке и есть ли символ "="
    while len(string_to_parse) > 2 and any(char == '=' for char in string_to_parse):
            delimiter1 = string_to_parse.find("=")
            param = string_to_parse[0:delimiter1]
            delimiter2 = string_to_parse.find(";")
            value = string_to_parse[delimiter1+1:delimiter2]
            if (len(param) == 0 or len(value) == 0):
                # Сookie без пары
                print("Неправильный формат Сookie!")
                return -1
            output[param] = value
            string_to_parse = string_to_parse[delimiter2+1:]
    return output

  
if __name__ == '__main__':
    assert parse('http://example.com/?name=Misha') == {'name': 'Misha'}
    assert parse('http://example.com/?name=Misha&') == {'name': 'Misha'}
    assert parse('http://example.com/?name=Misha&gender=male') == {'name': 'Misha', 'gender': 'male'}
    assert parse('http://example.com/?name=Misha&eye_color=green') == {'name': 'Misha', 'eye_color': 'green'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Misha#anchor') == {'name': 'Misha'}
    assert parse('http://example.com/#anchor') == {}
    assert parse('http://example.com/?name=Misha&error') == -1
    assert parse('http://example.com/?error?name=Misha') == -1
    assert parse_cookie('name=Misha;') == {'name': 'Misha'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Misha;age=25;') == {'name': 'Misha', 'age': '25'}
    assert parse_cookie('name=Misha=Admin;age=25;') == {'name': 'Misha=Admin', 'age': '25'}
    assert parse_cookie('name=Misha=Admin;eye_color=green;') == {'name': 'Misha=Admin', 'eye_color': 'green'}
    assert parse_cookie('name=Misha=Admin;;;') == {'name': 'Misha=Admin'}
    assert parse_cookie('name=Misha=Admin;error') == {'name': 'Misha=Admin'}
    assert parse_cookie('name=Misha=Admin;error;') == {'name': 'Misha=Admin'}
    assert parse_cookie('name=Misha=Admin;error=') == -1
    assert parse_cookie('name=Misha=Admin;=error;') == -1
