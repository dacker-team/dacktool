def split_paragraphs(text):
    list = text.split('. ')
    result = []
    paragraph = ''
    for sentence in list:
        paragraph += sentence + '. '
        if len(paragraph) > 200:
            result.append(paragraph)
            paragraph = ''
    return '</p><p>'.join(result)
