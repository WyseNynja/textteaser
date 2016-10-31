# TextTeaser

TextTeaser is an automatic summarization algorithm.

I've added a simple command line entrypoint for easy summarizing.


## Quick Setup with Docker

1. Install Docker from https://www.docker.com/

2. Add the following to your dotfiles:

  ```bash
  alias textteaser="docker run --rm -it bwstitt/textteaser"
  ```

3. Run this in your terminal:

  ```bash
  textteaser
  ```

4. Follow the prompts to summarize text

Entering a title helps inform the summarizer what is imporant.

Press [ctrl + c] to exit at any time.

Press [ctrl + d] on a blank line when done entering your text to see the summary.

Press [space] to read the full summary if it is too long.

Press [q] to stop reading the summary and enter the next article.


## Developing

Automatically upgrading requirements.txt:

```bash
pip install pip-tools
pip-compile requirements.in
```


## Todo

 * [ ] Automatically save full text as it is entered
 * [ ] Automatically save summaries as they are created
 * [ ] Support entering a URL
