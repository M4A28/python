from Question import Question

question_promets = [
    'what is color of see ? \n(a)blue\n(b)red\n(c)green\n\n',
        'what is shap of door? \n(a)circol\n(b)squar\n(c)tryangle\n\n',
            'what is color of blood ?\n(a)red\n(b)blue\n(c)tel\n\n',
            'what is wors devies ?\n(a)TV\n(b)computer\n(c)phones\n\n',
            'what is best brathor in the famly ?\n(a)mohammed\n(b)noor\n(c)hagar\n\n',
            'what you aet in noon ?\n(a)braekfast\n(b)lunch\n(c)dinner\n\n',
            'are you donkey ? \n(a)yes\n(b)no\n(c)myby\n\n',
            '3 * 3 = ? \n(a)9\n(b)6\n(c)3\n\n'

            ]



questions = [
    Question(question_promets[0], 'a'),
    Question(question_promets[1], 'b'),
    Question(question_promets[2], 'a'),
    Question(question_promets[3], 'a'),
    Question(question_promets[4], 'a'),
    Question(question_promets[5], 'b'),
    Question(question_promets[6], 'b'),
    Question(question_promets[7], 'a')


]



def run_test(questions):
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer == (question.answer):
            score += 1
    print('you got  ' + str(score) + '/' + str(len(questions)) + ' correct!')

run_test(questions)
