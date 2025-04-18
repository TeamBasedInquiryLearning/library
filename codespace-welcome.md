## Welcome to the TBIL Resource Library Codespace!

<!--
To see a prettier version of this file with clickable links, 
press [Ctrl/Cmd]+[Shift]+[v] on your keyboard.
-->

### Automated Setup

Upon first creating your Codespace, it will automatically install several
pieces of software for you. You can start editing files while this happens,
but live previews will not be available until this process is complete.
This is a one-time process; future boot-ups of your Codespace
will be ready to edit instantly.

### Live CodeChat Previews

Once this software is installed, you can edit a book with live previews
by first opening the appropriate file:

- Calculus: [`codechat_config_calculus.yaml`](codechat_config_calculus.yaml)
- Precalculus: [`codechat_config_precalculus.yaml`](codechat_config_precalculus.yaml)
- Linear Algebra: [`codechat_config_linear_algebra.yaml`](codechat_config_linear_algebra.yaml)

Copy its entire contents (`Ctrl`+`A` then `Ctrl`+`C`), then open and overwrite *ALL* the contents of
the [`codechat_config.yaml`](codechat_config.yaml) file (`Ctrl`+`A` then `Ctrl`+`V`).

> Alternatively, open a terminal and run this command to copy eveything for you.
> 
> - Calculus: `cp codechat_config_calculus.yaml codechat_config.yaml`
> - Precalculus: `cp codechat_config_precalculus.yaml codechat_config.yaml`
> - Linear Algebra: `cp codechat_config_linear_algebra.yaml codechat_config.yaml`

Then select "Preview with Codechat" from the PreTeXt menu in the bottom toolbar.
You will see live previews of most `.ptx` files for that book in a side
panel.

### Learn more

For more information, visit our wiki at
<https://github.com/TeamBasedInquiryLearning/library/wiki/GitHub-Codespaces-for-Authors>.
