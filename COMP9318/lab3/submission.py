
################# Question 1 #################

def multinomial_nb(training_data, sms):  # do not change the heading of the function
    '''
    training data: dictionary
    sms: all words
    '''

    num_of_occurs = {'ham': 0, 'spam': 0}
    all_words_dict = {'spam': [], 'ham': []}
    all_words = set()

    for data in training_data:
        if data[1] == 'ham':
            for word_and_occur_times in data[0].items():  # tuple (word, occur_times)
                all_words_dict['ham'].append(word_and_occur_times)
                num_of_occurs['ham'] += word_and_occur_times[1]
        else:
            for word_and_occur_times in data[0].items():
                all_words_dict['spam'].append(word_and_occur_times)
                num_of_occurs['spam'] += word_and_occur_times[1]

    # get all words(distinct)
    for tmp in all_words_dict.items():
        for words in tmp[1]:
            all_words.add(words[0])

    # default value of result
    result = {'spam': (len([_ for _ in training_data if _[1] == 'spam'])) / len(training_data),
              "ham": (len([_ for _ in training_data if _[1] == 'ham'])) / len(training_data)}
    for token in sms:
        if token in all_words:
            for class_type in ['spam', 'ham']:
                total_num_of_docs = num_of_occurs[class_type] + len(all_words)
                occur_times = [_[1] for _ in all_words_dict[class_type] if _[0] == token]
                result[class_type] *= (sum(occur_times) + 1) / total_num_of_docs

    return result['spam'] / result['ham']



