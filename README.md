# Team-Based Inquiry Learning

Welcome to our mono-repo for the Team-Based Inquiry Learning (TBIL) project.
The main products in this repository are our TBIL activity books
and exercise banks (the "TBIL Resource Library"), as well as our project
website at <https://tbil.org>.

## Get Involved

Everyone is welcomed to [contribute](CONTRIBUTING.md) to this project!
You're directed to these resources:

- [Wiki](https://github.com/TeamBasedInquiryLearning/library/wiki):
  a community-maintained wiki on this project.
- [Discussions](https://github.com/TeamBasedInquiryLearning/library/discussions):
  an open forum here on GitHub for discussing TBIL publicly.
- [Issues](https://github.com/TeamBasedInquiryLearning/library/issues):
  the place to point out typos and suggest specific improvements. Not sure exactly
  what needs to be changed? Start a
  [discussion](https://github.com/TeamBasedInquiryLearning/library/discussions)
  instead!
- [Chat](http://chat.tbil.org): our Slack channels are welcome to
  any discussion related to TBIL. "Live" discussion happens here for the most
  part.
- And finally, we welcome direct edits to these material via pull request!
  Not sure what a pull request is? Head over to the
  [wiki](https://github.com/TeamBasedInquiryLearning/library/wiki)
  to learn how to fix our typos with just a free GitHub account and your
  web browser.

## Contributing for Advanced Users

We recommend using Codespaces to propose changes to this repository or a fork,
even for advanced users:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TeamBasedInquiryLearning/library)

If developing locally anyway, you are encouraged to review `.devcontainer.json`
to learn our dependencies, and to install our `pre-commit` hook to prevent
accidentally committing to the main branch:

```
git config core.hooksPath .githooks
```

## Deployment

```
aws configure
aws s3 cp [path/to/year] s3://BUCKET_NAME/[year]/ --recursive
```
