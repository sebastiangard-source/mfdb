# Authored dials for Saint Croix, 6 November 2026. Sebastian ruled murica 4, durability 5 (lifetime repair), finbro 1, craft 4, Chicago counted as an own store.
# Tech 1 (thread returned NC; no technical fabric named). Dials from the thread's dials.csv (171 men's descriptions, 13 product pages).
# golffice was NC (no occasion copy); seated 0 as the neutral value. sail NC, left unseated.
F = lambda d=1, ca=1, li=1, co=1, wo=1, sy=1: dict(denim=d, cashmere=ca, linen=li, cotton=co, wool=wo, synth=sy)
A = {
 'Saint Croix': dict(tech=1, craft=4, comfort=4, style=3, fabric=F(1,2,1,4,4,2), dur=5, forg=2, forgc=[3,2,1],
   fuss=1, golffice=0,
   reg=dict(murica=4, ivy=1, prep=2, golf=2, status=3, finbro=1, ital=3, fren=1, briish=1, scandi=1, street=1, avant=1, weird=1,
            boat=0, racquet=0, ski=0),
   whitet=3, logo=1, western=1, rock=1, workwear=1, outdoor=1, surf=1, shoes=0,
   why="Knitwear, polos and shirts from Winona, Minnesota, in Giza cotton and merino, made since 1960 at the brand's own mill and in Italy, with a store of its own in Chicago.",
   chan=['O','I','W']),
}
