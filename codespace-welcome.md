## Welcome to the TBIL Resource Library Codespace!

<!--

    To see a prettier version of this file with clickable links, 
    press [Ctrl/Cmd]+[Shift]+[v] on your keyboard.

-->

### Automated Setup

If you see this message, your Codespace should already be configured with
all the necessary software.

You may see a terminal that downloads a cache of 

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

### Learn more

For more information, visit our wiki at
<https://github.com/TeamBasedInquiryLearning/library/wiki/GitHub-Codespaces-for-Authors>.
