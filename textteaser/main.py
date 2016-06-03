import os

from textteaser.summarizer import Summarizer

import click


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
        try:
            title = raw_input('Title: ')
        except EOFError:
            raise KeyboardInterrupt

        print "\nText ([ctrl + d] to stop):"
        text = ""
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
    click.clear()
    summary = "Summary of '%s':\n\n" % input_dict['title']
    for r in result:
        summary += r['sentence'] + "\n\n"

    summary += "Press [q] to exit."

    click.echo_via_pager(summary)
    click.clear()


def loop_main():
    print "Press [ctrl + c] to exit.\n"
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print "\n\nGoodbye!"


if __name__ == '__main__':
    main()