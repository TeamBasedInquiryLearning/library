#!/bin/bash

sudo apt-get update 
sudo apt-get install -y --no-install-recommends \
                    python3-louis \
                    libcairo2-dev \
                    librsvg2-bin

pip install -r requirements.txt # install on default python

bash ./.devcontainer/installSage.sh
bash ./.devcontainer/installLatex.sh
tlmgr install tikz-cd
git config --global --add safe.directory $(pwd)

eval "$('conda' 'shell.bash' 'hook' 2> /dev/null)"
conda activate sage
python -m pip install -r requirements.txt # install on conda python
git config core.hooksPath .githooks
touch codechat_config.yaml

playwright install-deps

playwright install

# # Install mermaid for diagrams
# npm install -g @mermaid-js/mermaid-cli

# prefig init
