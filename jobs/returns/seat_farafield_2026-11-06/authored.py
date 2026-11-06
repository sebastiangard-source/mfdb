# Authored dials for Farafield, 6 November 2026. Sebastian ruled craft 2, the Porto studio counted as a door, founded 2016, floor 0 where the scale has a 0 and nothing was found.
# Tech 1 (thread proposed 1). Dials from the thread's dials.csv (scanned across 155 live pages, about ten read by eye). golffice and western were NC and are left unscored.
F = lambda d=1, ca=1, li=1, co=1, wo=1, sy=1: dict(denim=d, cashmere=ca, linen=li, cotton=co, wool=wo, synth=sy)
A = {
 'Farafield': dict(tech=1, craft=2, comfort=3, style=4, fabric=F(1,1,2,3,2,1), dur=3, forg=2, forgc=[3,2,1],
   fuss=1, golffice=0,
   reg=dict(murica=2, ivy=2, prep=2, golf=1, status=2, finbro=1, ital=2, fren=2, briish=2, bruv=-1, scandi=0, street=2, avant=1, weird=3,
            boat=0, racquet=0, ski=0),
   whitet=1, logo=2, western=0, rock=1, workwear=3, outdoor=1, surf=3, shoes=0,
   why="Menswear from Brighton and Porto, founded in 2016 by two brothers: knitwear, chore jackets and printed shirts, made in Sri Lanka, India, Turkey, Portugal and the UK, with a design studio and sample store in Porto.",
   chan=['I','W']),
}
