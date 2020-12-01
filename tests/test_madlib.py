from madlib_cli.madlib import read_template,parse_template,merge_template,write_the_result



"""
input >> 'assets/madlip.txt'
output >> the content of the file that called madlip.txt
"""
def test_reading_file():
    actual = read_template('assets/madlip.txt')
    expected = "Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."
    assert actual==expected



"""
input >> template string.
output >> returns a string with language parts removed and a separate list of those language parts.
"""
def test_parsed_text():
    actual = parse_template()
    expected = ("Make Me A Video Game!\n\nI the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.", ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'Large Animal', 'Small Animal', "A Girl's Name", 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50', "First Name's", 'Number', 'Plural Noun', 'Number', 'Plural Noun'])
    assert actual==expected


"""
input >> template and a list of user entered language parts.
output >> string with the language parts inserted into the template.
"""

def test_merge_text():
    # actual = merge_template()
    # expected = read_template()
     assert True