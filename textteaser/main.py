import os

from textteaser.summarizer import Summarizer


def sanitize_lines(text):
    r"""Remove unnecessary \n."""
    return [c.replace('\n', '') for c in text if c != '\n']


def get_input():
    if os.path.exists('input.txt'):
        with open('input.txt') as f:
            content = sanitize_lines(f.readlines())

        title = content[0]
        text = ' '.join(content[-(len(content) - 1):])
    else:
        title = raw_input('Title: ')
        print

        text = ""

        print 'Text ([ctrl + d] to stop):'
        try:
            while True:
                text += raw_input() + " "
        except EOFError:
            pass

    title = title.decode("ascii", "ignore")
    text = text.decode("ascii", "ignore").replace("\n", " ")

    return {
        'title': title,
        'text': text,
    }


def main():
    # todo: use argparse or click or something like that
    input_dict = get_input()

    summarizer = Summarizer()
    result = summarizer.summarize(
        input_dict['text'],
        input_dict['title'],
        'Undefined',
        'Undefined',
    )
    result = summarizer.sortScore(result)
    result = summarizer.sortSentences(result[:30])

    # todo: paginate this output
    print
    print '*' * 80
    print
    print '*' * 80
    print
    print 'Summary of %s:' % input_dict['title']
    for r in result:
        print
        print r['sentence']
        # print r['totalScore']
        # print r['order']


def loop_main():
    print "Press [ctrl + c] to exit.\n"
    try:
        while True:
            main()
            print
            print "*" * 80
            print
    except KeyboardInterrupt:
        print "\n\nGoodbye!"


if __name__ == '__main__':
    main()