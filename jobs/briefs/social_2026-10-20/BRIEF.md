# social_2026-10-20: Instagram and TikTok handles and follower counts

**Issued** 20 October 2026 · **Kind** read · **Batches of 25, returned as each is done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job. If you cannot run a browser, say so and stop.

## Why

The Cyprus Brand Explorer will show each brand's Instagram and TikTok accounts, with follower counts, on its card. Audience size helps rank brands for partnership. A handle that belongs to someone else is worse than no handle.

## The worklist

`worklist.csv` lists 295 brands with five or more full-price US stores, ordered by store count, largest first, in 12 batches of 25:
- 231 fashion brands;
- 64 jewelry, beauty, home, bag, eyewear and travel brands.

`brand_site` is the brand's own site, the starting point for every brand.

## How to find the right account

1. **Start on the brand's own site.** Most sites link their Instagram and TikTok in the footer or header. A link from the brand's own site makes the account official. Record `found_on` = `brand_site`.
2. **If the site doesn't link one,** search the platform for the brand name. Take the account only if both of these hold:
   - it is verified, or its bio links to the brand's own site;
   - its posts are plainly the brand's own.

   Record `found_on` = `platform_search`. If neither holds, the row is `NONE` for that platform, with a note on what you saw.
3. **One account per platform: the brand's main one.**
   - Where the brand runs regional accounts (a US account beside the global one), take the global or main brand account. Name the US one in `note`.
   - Where it splits by gender or line (a separate men's or kids' account), take the main brand account. Note the others.
   - Set `account_scope` to `main`, `us`, `womens` or `other`, and say which in `note`.
4. **Sister banners are their own brands.** Never give one brand another's account.
   - RRL is not Polo Ralph Lauren.
   - Carhartt WIP is not Carhartt.
   - Athleta is not Gap.
   - Aerie is not American Eagle.
   - LOFT is not Ann Taylor.
   - J.Crew Factory is not J.Crew.

## Follower counts

Open each profile once and read the follower count it shows.
- `followers_shown` is the count exactly as displayed, for example `1.2M` or `48.3K`.
- `followers` is the same count as a whole number, for example `1200000`. Where the display is rounded, the number is rounded too; don't hunt for an exact figure.
- `verified` is `yes` or `no`, from the badge.

## Logins and walls

- **Read only.** Never follow, like, comment, message, save or click anything that acts on an account. If Chrome is signed in to Instagram or TikTok, browse as you are, but take no action on any account.
- **If a profile page asks you to log in before it shows the count,** close the prompt once if it can be closed. If the count still isn't visible, put `NC` in the follower cells and keep the handle.
- **If a check box appears,** ask Sebastian once whether he'll clear it himself. Any other wall (slider, press-and-hold, "try again later") stops that platform: put `NC` on the rest of the batch for it, name the wall in `NOTE.md`, and carry on with the other platform.
- **Pace:** one profile every few seconds. Instagram rate-limits quickly; if pages start coming back empty, stop Instagram for that batch and say so.
- Use only the pages a person sees. Don't call either platform's private services.

## What you return

**`return.csv`**, in the columns of `return_template.csv`, with two rows per brand: one `instagram`, one `tiktok`.
- `handle` without the @. `url` is the profile address.
- `status` is one of:
  - `done`: handle and count read;
  - `handle_only`: the count is behind a wall;
  - `NONE`: no account on that platform;
  - `NC`: not checked.

**`NOTE.md`**, one per batch: the walls you hit, regional or split accounts you passed over, and anything doubtful.

Before each return, run `python3 reconcile.py` on the brand column. No empty cells.

## Order and time box

- Work in batch order and return each batch as it's done.
- Two to three minutes a brand.
- Past the box, return what you have, put `NC` on the rest, and say so.
