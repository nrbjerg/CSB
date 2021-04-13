import re
from typing import Dict, Tuple, List

def findMathModeAndText (string: str) -> List[Tuple[str]]:
    """ Returns a list of tuples containing the starting and closing indexes of the math blocks """
    # 1. Find the math sub strings
    matches = re.findall(r"\$\$.*?\$\$|\$.*?\$|\\begin\{equation\*?\}.*?\\end\{equation|\\begin\{align\*?\}.*?\\end\{align\*?\}", string)

    subStrings = []
    if (matches[0].start != 0):
        subStrings.append(("text", string[:matches[0].start()]))
    
    index = 0    
    for match in matches:
        subStrings.append(("math", string[match.start():match.end()]))
        
        
    return subStrings
def modify (string: str, matches: Dict[str, str]) -> str:
    """ Takes a string and replaces the keys in the matches dictionary with the values """
    # 1. Find every math mode
    mathModeStrings = findMathModeAndText(string)
    
    print(mathModeStrings)
    
if (__name__ == "__main__"):
    with open("../test.tex", "r") as file:
        modify(file.read(), {})