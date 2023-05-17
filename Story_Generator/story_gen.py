


def sentence_maker(text):
    question_words = ['how', 'why', 'what', 'where', 'when',]
    capitalized_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            return '{}?'.format(capitalized_text)
    return '{}.'.format(capitalized_text)



print('Type done when you want to stop')
result = []
while True:
    user_input = input('What is on your mind? ')
    if user_input == 'done':
        break
    else:
        complete_sentence = sentence_maker(user_input)
        result.append(complete_sentence)
story = ' '.join(result)
print(story)