import argparse
import lxml.etree as ET

def main(query:str, file:str,verbose=False):
    tree = ET.parse(file)
    results=tree.xpath(query)
    if not results:
        if verbose:
            print(f"Scanning {file}...")
            print(f"No results found")
        return
    print(f"Found in {file}:")
    for result in results:
        print(f"Line {result.sourceline}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Searches files for xml elements specified by the query')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-q', '--query', help="Give an explicit xpath query. If present, overrides --element, --child, and --no-child")
    parser.add_argument('-e', '--element', action='append',  help="Restricts search to specified elements")
    parser.add_argument('-c', '--child', action='append',  help="Restricts search to elements who have a specified child element")
    parser.add_argument('-n', '--no-child', action='append',  help="Restricts search to elements who do not have a specified child element")
    parser.add_argument('-d', '--display-query',action='store_true', help="Display xpath query generate from --element, --child, and --no-child")
    parser.add_argument('-v', '--verbose',action='store_true', help="Verbose mode")
    args = parser.parse_args()

    files=args.files
 
    if args.query:
        query=args.query
        if args.element or args.child or args.no_child:
            print("Applying --query and ignoring --element, --child, and --no-child")
    else:
        if not args.element:
            print("Must specify --query or --element")
            exit(1)
        query='//*[(' + ' or '.join([f"self::{e}" for e in args.element])+')'
        if args.child:
          query+= 'and '+' and '.join([f"child::{c}" for c in args.child])
        if args.no_child:
          query+= 'and '+' and '.join([f"not(child::{c})" for c in args.no_child])
        query+=']'
        if args.verbose or args.display_query:
            print(f"Applying query {query}")

    for file in files:
        main(query=query, file=file,verbose=args.verbose)