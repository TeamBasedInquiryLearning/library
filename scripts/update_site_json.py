import json

def main():
    site_dict = {
        "SITENAME": "Team-Based Inquiry Learning",
        "SITESUBTITLE": "Open Resources and Research supporting Active Learning in Mathematics",
        "PTX_SHOW_TARGETS": "no",
        "STATIC_PATHS": ["static", "precalculus", "calculus", "linear-algebra"]
    }
    with open("site/description.html") as f:
        site_dict["PTX_SITE_DESCRIPTION"] = f.read()
    with open("site/site.json", "w") as f:
        json.dump(site_dict, f, indent=4)

if __name__ == "__main__":
    # we're not using this right now...
    raise NotImplementedError
    main()
