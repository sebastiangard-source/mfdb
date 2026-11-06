# Authored dials for the three Withered Fig D brands, 6 November 2026, from the thread's dials.csv. Sail unscored (NA); golffice seated then popped when NC.
F = lambda d=1, ca=1, li=1, co=1, wo=1, sy=1: dict(denim=d, cashmere=ca, linen=li, cotton=co, wool=wo, synth=sy)
A = {}
A['Fitted Underground'] = dict(tech=1, craft=4, comfort=3, style=2, fabric=F(5,1,1,3,1,1), dur=4, forg=4, forgc=[3, 3, 2], fuss=1, golffice=0,
  prices_override={'T-shirt': None},  # the $35 tee is a graphic tee (Brooklyn Army), not the core tee; core PFT tee price not captured
  reg={'murica': 3, 'ivy': 1, 'prep': 1, 'golf': 1, 'status': 2, 'finbro': 1, 'ital': 1, 'fren': 1, 'briish': 1, 'scandi': 1, 'street': 2, 'avant': 1, 'weird': 1, 'boat': 0, 'racquet': 0, 'ski': 0},
  whitet=3, logo=2, western=2, rock=1, workwear=3, outdoor=1, surf=1, shoes=0,
  why="Raw Japanese selvedge jeans, tees and work shirts sewn in Brooklyn, by a founder who taught himself and made jeans alone in a basement for a decade.", chan=['O', 'W'])
A['National Athletic Goods'] = dict(tech=1, craft=3, comfort=3, style=2, fabric=F(1,1,1,3,1,1), dur=3, forg=2, forgc=[3, 2, 1], fuss=-1, golffice=1,
  band='premium',
  reg={'murica': 4, 'ivy': 2, 'prep': 2, 'golf': 1, 'status': 3, 'finbro': 1, 'ital': 1, 'fren': 1, 'briish': 1, 'scandi': 1, 'street': 2, 'avant': 1, 'weird': 1, 'boat': 0, 'racquet': 0, 'ski': 0},
  whitet=1, logo=2, western=1, rock=1, workwear=1, outdoor=1, surf=1, shoes=0,
  why="Vintage-spec athletic tees and sweats in Japanese combed cotton, made in Canada.", chan=['I'])
A['Barnstormer'] = dict(tech=1, craft=4, comfort=2, style=3, fabric=F(1,1,1,3,4,1), dur=4, forg=4, forgc=[3, 3, 2], fuss=1, golffice=-1,
  band='premium',
  prices_override={'T-shirt': None, 'Dress shirt': [117, 198], 'Jeans': [205, 315], 'Dress pants': [161, 323], 'Sweater': None, 'Outerwear': [330, 880]},
  reg={'murica': 4, 'ivy': 4, 'prep': 3, 'golf': 1, 'status': 3, 'finbro': 2, 'ital': 1, 'fren': 1, 'briish': 2, 'scandi': 1, 'street': 1, 'avant': 1, 'weird': 2, 'boat': 1, 'racquet': 0, 'ski': 0},
  whitet=1, logo=1, western=1, rock=1, workwear=3, outdoor=1, surf=1, shoes=0,
  why="Japanese-made American Trad chinos and wool trousers from a Tokyo house whose predecessor began in 1977.", chan=['O', 'I', 'W'])
