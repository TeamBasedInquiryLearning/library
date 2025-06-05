#!/bin/bash

sudo apt-get update 
sudo apt-get install -y --no-install-recommends \
                    python3-louis \
                    libcairo2-dev \
                    librsvg2-bin

bash ./.devcontainer/installSage.sh
bash ./.devcontainer/installLatex.sh
tlmgr install tikz-cd
git config --global --add safe.directory $(pwd)

python -m pip install CodeChat-Server
eval "$('conda' 'shell.bash' 'hook' 2> /dev/null)"
conda activate sage
python -m pip install -r requirements.txt

