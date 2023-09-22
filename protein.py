#import libraries
import random
import string
import py3Dmol
import requests
import biotite.structure.io as bsio
#from stmol import showmol

#"TLVRPKPLLLKLLKSVGAQKDTYTMKEVLFYLGQYIMTKRLYDEKQQHIVYCSNDLLGDLFGVPSFSVKEHRKIYTMIYRNLVV"

def create_protein(input):
  target_sequence = input

  headers = {'Content-Type': 'application/x-www-form-urlencoded',}
  response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=target_sequence)
  pdb_string = response.content.decode('utf-8')

  with open('predicted.pdb', 'w') as f:
    f.write(pdb_string)

  struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
  b_value = round(struct.b_factor.mean(), 4)

  return b_value

def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    pdbview.spin(True)
    return pdbview

