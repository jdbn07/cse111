from formula import parse_formula, FormulaError

def main():
   
    # Get a chemical formula for a molecule from the user.
    chemical_formula = input("Enter the molecular formula: ")
    # Get a mass in grams from the user.
    mass = float(input("Enter the mass in grams: "))
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    table =make_periodic_table()
    periodic_table=table
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    formula = parse_formula(chemical_formula,periodic_table)
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(formula,periodic_table)
    # store in a variable the get_molecules_name function
    molecules= get_molecules_names()
    # call the get_formula_name function
    name_chemical=get_formula_name(chemical_formula, molecules)
    # Compute the number of moles of the sample.
    total_moles= mass/molar_mass
    # Print the molar mass.
    print(f"The molar mass is: {molar_mass:.3f} grams/mole")
    # Print the number of moles.
    print(f"Total: {total_moles:.3f} moles")
    #print the formula chemical name
    print(name_chemical)



def make_periodic_table(): 

    table= {
    
    # [symbol, name, atomic_mass]
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        "Am":	["Americium",	243],
        "Ar":	["Argon",	39.948],
        "As":	["Arsenic",	74.9216],
        "At":	["Astatine",	210],
        "Au":	["Gold",	196.966569],
        "B":	["Boron",	10.811],
        "Ba":	["Barium",	137.327],
        "Be":	["Beryllium",	9.012182],
        "Bh":	["Bohrium",	272],
        "Bi":	["Bismuth",	208.9804],
        "Bk":	["Berkelium",	247],
        "Br":	["Bromine",	79.904],
        "C":	["Carbon",	12.0107],
        "Ca":	["Calcium",	40.078],
        "Cd":	["Cadmium",	112.411],
        "Ce":	["Cerium",	140.116],
        "Cf":	["Californium",	251],
        "Cl":	["Chlorine",	35.453],
        "Cm":	["Curium",	247],
        "Cn":	["Copernicium",	285],
        "Co":	["Cobalt",	58.933195],
        "Cr":	["Chromium",	51.9961],
        "Cs":	["Cesium",	132.9054519],
        "Cu":	["Copper",	63.546],
        "Db":	["Dubnium",	268],
        "Ds":	["Darmstadtium",	281],
        "Dy":	["Dysprosium",	162.5],
        "Er":	["Erbium",	167.259],
        "Es":	["Einsteinium",	252],
        "Eu":	["Europium",	151.964],
        "F":	["Fluorine",	18.9984032],
        "Fe":	["Iron",	55.845],
        "Fl":	["Flerovium",	289],
        "Fm":	["Fermium",	257],
        "Fr":	["Francium",	223],
        "Ga":	["Gallium",	69.723],
        "Gd":	["Gadolinium",	157.25],
        "Ge":	["Germanium",	72.64],
        "H":	["Hydrogen",	1.00794],
        "He":	["Helium",	4.002602],
        "Hf":	["Hafnium",	178.49],
        "Hg":	["Mercury",	200.59],
        "Ho":	["Holmium",	164.93032],
        "Hs":	["Hassium",	270],
        "I":	["Iodine",	126.90447],
        "In":	["Indium",	114.818],
        "Ir":	["Iridium",	192.217],
        "K":	["Potassium",	39.0983],
        "Kr":	["Krypton",	83.798],
        "La":	["Lanthanum",	138.90547],
        "Li":	["Lithium",	6.941],
        "Lr":	["Lawrencium",	262],
        "Lu":	["Lutetium",	174.9668],
        "Lv":	["Livermorium",	293],
        "Mc":	["Moscovium",	288],
        "Md":	["Mendelevium",	258],
        "Mg":	["Magnesium",	24.305],
        "Mn":	["Manganese",	54.938045],
        "Mo":	["Molybdenum",	95.96],
        "Mt":	["Meitnerium",	276],
        "N":	["Nitrogen",	14.0067],
        "Na":	["Sodium",	22.98976928],
        "Nb":	["Niobium",	92.90638],
        "Nd":	["Neodymium",	144.242],
        "Ne":	["Neon",	20.1797],
        "Nh":	["Nihonium",	284],
        "Ni":	["Nickel",	58.6934],
        "No":	["Nobelium",	259],
        "Np":	["Neptunium",	237],
        "O":	["Oxygen",	15.9994],
        "Og":	["Oganesson",	294],
        "Os":	["Osmium",	190.23],
        "P":	["Phosphorus",	30.973762],
        "Pa":	["Protactinium",	231.03588],
        "Pb":	["Lead",	207.2],
        "Pd":	["Palladium",	106.42],
        "Pm":	["Promethium",	145],
        "Po":	["Polonium",	209],
        "Pr":	["Praseodymium",	140.90765],
        "Pt":	["Platinum",	195.084],
        "Pu":	["Plutonium",	244],
        "Ra":	["Radium",	226],
        "Rb":	["Rubidium",	85.4678],
        "Re":	["Rhenium",	186.207],
        "Rf":	["Rutherfordium",	267],
        "Rg":	["Roentgenium",	280],
        "Rh":	["Rhodium",	102.9055],
        "Rn":	["Radon",	222],
        "Ru":	["Ruthenium",	101.07],
        "S":	["Sulfur",	32.065],
        "Sb":	["Antimony",	121.76],
        "Sc":	["Scandium",	44.955912],
        "Se":	["Selenium",	78.96],
        "Sg":	["Seaborgium",	271],
        "Si":	["Silicon",	28.0855],
        "Sm":	["Samarium",	150.36],
        "Sn":	["Tin",	118.71],
        "Sr":	["Strontium",	87.62],
        "Ta":	["Tantalum",	180.94788],
        "Tb":	["Terbium",	158.92535],
        "Tc":	["Technetium",	98],
        "Te":	["Tellurium",	127.6],
        "Th":	["Thorium",	232.03806],
        "Ti":	["Titanium",	47.867],
        "Tl":	["Thallium",	204.3833],
        "Tm":	["Thulium",	168.93421],
        "Ts":	["Tennessine",	294],
        "U":	["Uranium",	238.02891],
        "V":	["Vanadium",	50.9415],
        "W":	["Tungsten",	183.84],
        "Xe":	["Xenon",	131.293],
        "Y":	["Yttrium",	88.90585],
        "Yb":	["Ytterbium",	173.054],
        "Zn":	["Zinc",	65.38],
        "Zr":	["Zirconium",	91.224]
    }
    return table

def get_molecules_names():
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }
    return known_molecules_dict

NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list. Each element in
    symbol_quantity_list is a list in the form: ["symbol", quantity].

    As an example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    #  For each element in the symbol_quantity_list:
    #    Split the element into symbol and quantity.
    #    Get the atomic mass for the symbol.
    #    Multiply the atomic mass by the quantity.
    #    Add the product into the total mass.

    quantity= 0
    total= 0
    for i in symbol_quantity_list:
        symbol= i[0]
        quantity= i[1]

        letter =periodic_table_dict[symbol]
        name=letter[NAME_INDEX]
        atomic_mass=letter[ATOMIC_MASS_INDEX]

        total= total + quantity*atomic_mass
        
    return total

    
def get_formula_name(formula, known_molecules):
        
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    """
    name_formula=""
    if formula in known_molecules:    
        name_formula= known_molecules[formula]
        return (f"The formula is called: {name_formula}")
    else:
        return print("unknown compound")

   
        

if __name__ == "__main__":
    main()

