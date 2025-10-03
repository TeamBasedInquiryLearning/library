## Welcome to the TBIL Resource Library Codespace!

<!--

    To see a prettier version of this file with clickable links, 
    press [Ctrl/Cmd]+[Shift]+[v] on your keyboard.

-->

### Automated Setup

If you see this message, your Codespace should already be configured with
all the necessary software.

A terminal will open to download a cache of assets (several lines of
`inflating: .cache/foobar/etc123.svg`). You can safely close this terminal if it
doesn't close itself.

### Live CodeChat Previews

Once this software is installed, you can edit a book with live previews
by doing one of the following:

#### Option 1

First opening the appropriate file:

- Calculus: [`codechat_config_calculus.yaml`](codechat_config_calculus.yaml)
- Precalculus: [`codechat_config_precalculus.yaml`](codechat_config_precalculus.yaml)
- Linear Algebra: [`codechat_config_linear_algebra.yaml`](codechat_config_linear_algebra.yaml)

Copy its entire contents (`Ctrl`+`A` then `Ctrl`+`C`), then open and overwrite *ALL* the contents of
the [`codechat_config.yaml`](codechat_config.yaml) file (`Ctrl`+`A` then `Ctrl`+`V`).

#### Option 2

Alternatively, open a terminal and run this command to copy everything for you.

- Precalculus: `cp codechat_config_precalculus.yaml codechat_config.yaml`
- Calculus: `cp codechat_config_calculus.yaml codechat_config.yaml`
- Linear Algebra: `cp codechat_config_linear_algebra.yaml codechat_config.yaml`

#### Open Preview with CodeChat

Then select "Preview file with CodeChat" from the PreTeXt menu in the bottom toolbar.
You will now be able to see live previews of most `.ptx` files for that book in a side panel.

### Note for local (non-Codespace) usage of devcontainer

We [have a report](https://github.com/TeamBasedInquiryLearning/library/pull/832#issuecomment-3099019003)
that when using this devcontainer on a local installation of VS Code, the
extensions specified in `devcontainer.json` may need to be installed manually.

### Learn more

For more information, visit our wiki at
<https://github.com/TeamBasedInquiryLearning/library/wiki/GitHub-Codespaces-for-Authors>.
