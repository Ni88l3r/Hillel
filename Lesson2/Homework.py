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
