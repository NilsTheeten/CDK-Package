import urllib.parse
import requests
from IPython.display import SVG, display


def smiles_depict_url(smiles: str, format: str = 'svg') -> str:
    """
    Generate the URL for the depiction of a SMILES string.
    Args:
        smiles: smiles string to depict
        format: 'svg', 'pdf', 'png', etc.
    Returns:
        URL string
   """
    CDKDEPICTLINK = 'https://www.simolecule.com/cdkdepict/depict/bow'
    params = {
        'smi': smiles,
        'w' : "-1",
        'h' : "-1",
        'abbr': "off",
        'hdisp' : "bridgehead",
        'zoom' : "1.3",
        'annotate' : "mapidx",
        'r' : "0" ,
        'style' : "bot",
        #sma : smart_pattern
        
        
    }
    params_str = urllib.parse.urlencode(params)
    url = "https://www.simolecule.com/cdkdepict/depict/cow/svg?"+params_str
    return url


    

def display_svg(url: str) -> None:
    # post a request to the link you construct. Remember to handle the cases where the response does not work as intented
    # Look at the response content to find the SVG data.
    response = requests.get(url)

    if response.status_code == 200:
        svg_data = response.text
        # Use the display function to display the SVG data
        display(SVG(svg_data))
        
    else:
        print(f"An Error Occured with the retrieval")


smiles = 'CN(CC(=O)O)C(=N)N' 
url = smiles_depict_url(smiles)
display_svg(url)
