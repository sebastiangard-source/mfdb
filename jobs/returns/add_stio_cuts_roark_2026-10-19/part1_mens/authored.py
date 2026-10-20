# Authored dials for Stio and Roark, 20 October 2026. Tech and craft at the thread's proposals, pending ruling.
# Roark: basic by the rule on the $35 Made To Fade tee and the $65 Well Worn button-up (short-sleeved); whether that
# is the core shirt is put to Sebastian. Katin and RVCA sit in basic on the same reading. Stio: no sweater, so the shirt entry alone ($99) reads premium.
F = lambda d=1, ca=1, li=1, co=3, wo=1, sy=1: dict(denim=d, cashmere=ca, linen=li, cotton=co, wool=wo, synth=sy)
A = {
 'Stio': dict(tech=4, comfort=3, style=2, fabric=F(2,1,1,2,2,5), dur=4, forg=3, forgc=[3,4,2], fuss=-1, golffice=1,
   reg=dict(ski=5, murica=3, finbro=3, status=2), whitet=2, logo=2, western=2, rock=1, workwear=2, outdoor=5, surf=1,
   why="Mountain clothing from Jackson, Wyoming, since 2011: shells, down, flannels and base layers, much of it in its own PeakProof fabrics, sold in 13 stores of its own.",
   chan=['O','I','W'],
   seg=dict(s='Outdoor & coast', c='high', r='authored at seat 20 Oct: outdoor 5 and ski 5, a technical mountain house')),
 'Roark': dict(tech=2, comfort=4, style=3, fabric=F(2,1,1,4,1,3), dur=3, forg=4, forgc=[4,4,1], fuss=-1, golffice=1,
   reg=dict(murica=3, boat=1, status=1), whitet=2, logo=2, western=1, rock=2, workwear=1, outdoor=4, surf=5,
   why="Travel and surf clothing from Southern California, founded in 2009: cotton tees, button-ups, boardshorts and the Run Amok running line, in eight Expedition Union stores.",
   chan=['O','I','W'],
   seg=dict(s='Outdoor & coast', c='high', r='authored at seat 20 Oct: surf 5 and outdoor 4, travel and surf')),
}
