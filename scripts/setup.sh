sudo apt-get update 
sudo apt-get install -y --no-install-recommends \
                    python3-louis \
                    libcairo2-dev \
                    librsvg2-bin

pip install -r requirements.txt
git config core.hooksPath .githooks
touch codechat_config.yaml
pretext --version

playwright install-deps

playwright install

# # Install mermaid for diagrams
# npm install -g @mermaid-js/mermaid-cli

# prefig init
