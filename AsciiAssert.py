from ascii_homework import *
error = """

import the following functions! (that you wrote)
rotate   convert   serialize  deserialize

"""
try:
    assert rotate("ertyui\ndfghjk\nvbfgrt\ncdferw\njhyuit\nknrfse", 90) == 'kjcvde\nnhdbfr\nryffgt\nfueghy\nsirrju\netwtki'
    assert rotate("ertyui\ndfghjk\nvbfgrt\ncdferw\njhyuit\nknrfse", 180) == 'esfrnk\ntiuyhj\nwrefdc\ntrgfbv\nkjhgfd\niuytre'
    assert rotate("ertyui\ndfghjk\nvbfgrt\ncdferw\njhyuit\nknrfse", 270) == 'iktwte\nujrris\nyhgeuf\ntgffyr\nrfbdhn\nedvcjk'
    assert rotate("ertyui\ndfghjk\nvbfgrt\ncdferw\njhyuit\nknrfse", 360) == 'iuytre\nkjhgfd\ntrgfbv\nwrefdc\ntiuyhj\nesfrnk'

    a = ["ghj", "bsr", "xcv", "!de", "ogt"]

    assert convert("dbxcfv;rxxxxxlhrliwmqggggooietxz", a, 1) == 'XscXXXXXcccccXXXXXXXXhhhhggXXXcX'
    assert convert("dbxcfv;rxxxxxlhrliwmqggggooietxz", a, 2) == 'XrvXXXXXvvvvvXXXXXXXXjjjjttXXXvX'

    assert serialize("ddddddddggggggggggggggeeeeeeeeeeeedbdrrrrrrrrrr", 0, 0, a, True) == '8d14g12e1d1b1d10r'
    assert deserialize("3H1 2e1 3l1 3o1,1 1 1W1o1r1l1d1!1\n5g5y", 0, 0, a, True) == 'HHH ee lll ooo,  World!\ngggggyyyyy'

    assert serialize("hrrr!!i\nhfgh!!h\nhhhh!!h\nhdfe!!w\nhhyu!!t\nhnrf!!e", 270, 2, a, True) == '6X\n6e\n6e\n6X\n1X1j4X\n6X\n6X'
    assert deserialize("3H1 2e1 3l1 3o1,1 1 1W1o1r1l1d1!1\n18g5y", 180, 0, a, True) == 'yyyyygggggggggggggggggg\n!dlroW  ,ooo lll ee HHH'
    assert deserialize("3H1 2e1 3l1 3o1,1 1 1W1o1r1l1d1!1\n18g5y", 0, 1, a, True) == 'XXXXXXXXXXXgggXXXXgXXXd\nhhhhhhhhhhhhhhhhhhXXXXX'
except NameError:
    print(error)
