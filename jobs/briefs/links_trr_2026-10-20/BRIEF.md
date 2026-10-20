# links_trr_2026-10-20: The RealReal, the brands the last pass couldn't check

**Issued** 20 October 2026 · **Kind** links · **One site, one return** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job. If you cannot run a browser, say so and stop.

## Why

Each Brand Set card links to the brand's page on The RealReal. The last pass read TRR's **Women** designer directory and matched 287 brands. Then a press-and-hold check appeared on the **Men** directory, and the pass stopped. That left 177 brands not checked: they weren't in the Women directory, and the other directories went unread. `worklist.csv` lists them, along with Bulgari, whose link was never opened.

Wrong is worse than missing: a card shows only a link that is right.

## Before you start: the check

The press-and-hold check is a bot test.

1. Open https://www.therealreal.com/designers/men once, at a normal pace.
2. **If the press-and-hold check appears**, stop and ask Sebastian in one line: *"The RealReal is showing its press-and-hold check on the Men designers page; will you clear it in this tab?"*
   - **If he clears it and the page loads**, carry on.
   - **If he says no, or doesn't answer**, return every row `NC` with the wall named, and stop.
3. Don't press and hold yourself, retry in a loop, or use any other route around the check.

## What to read

Work by directory, as before. Open each A–Z page once, read the whole list, and match it against the worklist:

1. **Men** (`/designers/men`)
2. **Fine Jewelry**, for the jewelry and watch brands in the worklist (`kind` = jewelry_high or jewelry_fine)
3. **Watches**
4. **Kids or Home**, only if a worklist brand plainly belongs there. Otherwise skip them.

Then:

- **Bulgari:** open `/designers/bvlgari/women` once and confirm it is Bulgari's page with items on it.
- **Brands still missing after all the directories:** search each name once in TRR's own search box, and look for a designer result. If none comes up, the row is `NONE`. TRR seems to leave mass-market labels out of the directories (Nike, Levi's, J.Crew and Zara appeared only in collaborations). Say so in `note` where that's the case.

## Matching rules

- **Sister lines are their own names.** Never fold one into another.
  - RRL is not Polo Ralph Lauren.
  - Carhartt WIP is not Carhartt.
  - Calvin Klein Collection is not Calvin Klein.
  - Levi's Vintage Clothing is not Levi's.
  - Black Comme des Garçons and Comme des Garçons Play are not Comme des Garçons.
  - Emporio Armani is not Giorgio Armani.
  - MM6 is not Maison Margiela.
- **Same name, different brand.** Open the page and check the category before matching On, Theory, Reiss, Still Here, CO, Sea, Purple, Represent, Elan, Rowan, Camilla and Bode.
- **Men's pages are fine here.** A brand TRR lists only under Men gets its men's page, with `note` saying so. Where TRR lists the brand under both Men and Women, give the women's page.
- **Listings:** give a count only where the brand page shows one in its header. Otherwise `ND`. Don't scroll to count.

## Return

- `return.csv` in the columns of `return_template.csv`, one row per worklist brand (178 rows). `site` = `The RealReal`.
  - `url_kind` is `designer_page` wherever possible.
  - `match` is `exact`, `alias` (with `name_on_site`), `NONE` or `NC`.
- `NOTE.md`: the pages you read, any wall, and anything doubtful.
- Run `python3 reconcile.py` on the brand column before returning. No empty cells. Where there's no link, put `NONE` or `NC` in `url`.

## Pace and time box

- One page every few seconds.
- If any other wall appears (slider, access denied), stop there, return what you have, and put `NC` on the rest.
- About an hour.
