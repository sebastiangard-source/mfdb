# Authored dials for the held four, 14 October 2026. UGG not seated (shoes still behind the bot wall; no priced staple).
# Kapital banded by hand at ¥150/$ (shirt ¥19,580 ≈ $131, sweater ¥29,480 ≈ $197, mean $164 → accessible); native prices stay.
F = lambda d=1, ca=1, li=1, co=3, wo=1, sy=1: dict(denim=d, cashmere=ca, linen=li, cotton=co, wool=wo, synth=sy)
A = {
 'Kapital': dict(tech=1, comfort=3, style=4, fabric=F(5,1,2,4,2,1), dur=4, forg=2, forgc=[2,3,1], fuss=1, golffice=-3,
   reg=dict(murica=3, workwear=4, western=3, weird=3, avant=2, street=2), whitet=2, logo=2, western=3, rock=2, workwear=4, outdoor=1, surf=1,
   why="Kojima denim house from 1985, boro patchwork, bandana prints and its own dye works; twelve shops in Japan, none in the US, prices in yen.", chan=['I','W'], say='KAP-ih-tl',
   band='accessible', seg=dict(s='Heritage & workwear', s2='Fashion insider', c='medium', r='authored at seat 14 Oct: Japanese denim and workwear heritage with a designer edge; the dials would read Heritage on workwear 4')),
 'Y-3': dict(tech=3, comfort=3, style=4, fabric=F(1,1,1,3,2,4), dur=3, forg=2, forgc=[2,3,1], fuss=0, golffice=-3,
   reg=dict(avant=3, street=3, status=2, scandi=1), whitet=2, logo=3, western=1, rock=1, workwear=1, outdoor=1, surf=1,
   why="Yohji Yamamoto's sportswear line with adidas since 2002, sold on adidas.com in the US; no store of its own.", chan=['D','W'], say='why-THREE',
   seg=dict(s='Fashion insider', s2='Avant-garde designers', c='medium', r='authored at seat 14 Oct: designer sportswear, logo 3 keeps it out of the Insider rule; placed on the why line')),
 'Sanderlak': dict(tech=1, comfort=3, style=5, fabric=F(2,1,1,3,3,2), dur=3, forg=2, forgc=[2,3,1], fuss=1, golffice=-2,
   reg=dict(avant=3, fren=1, status=2), whitet=2, logo=1, western=1, rock=1, workwear=1, outdoor=1, surf=1,
   why="Sander Lak's New York label from 2024, a collection a year rooted in one place, the Maharam jacquard coat its signature; one store, 2 East Broadway.", chan=['O','D','W'], say='SAN-der-lahk',
   seg=dict(s='Fashion insider', c='high', r='authored at seat 14 Oct: designer-led, quiet, style 5 and logo 1 with avant 3 (R15)')),
}
