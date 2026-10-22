# croissant_member_review_2026-10-22: Croissant from the inside, as a member

**Issued** 22 October 2026 · **Kind** competitive read · **One thread, one return** · **Returns to** the Spectrum thread (for the competitive file)

This is a Chrome job in **Sebastian's own browser, signed in to his Croissant account**. If you can't run a browser, or Croissant isn't signed in, say so and stop. Don't sign in for him and don't ask for his password.

## Why

Cyprus is a premium membership that rewards shopping at the brands' own stores. Croissant comes at the same shopper another way: it shows a guaranteed resale price when you buy, gives credit back, and buys the item back later. The Cyprus whitepaper describes Croissant from the outside. This pass looks at it **as a member sees it**, so the comparison rests on what Croissant actually offers and how it works, not on press. A companion pass does the same for CAKE.

## You are in someone's account: read only

This is the rule that matters most:

- **Look, never act.** Don't:
  - buy anything;
  - start a trade-in or buy-back, or list or sell an item;
  - claim, redeem or apply credit;
  - link or change a card or bank account;
  - change a setting, refer anyone, message support or post anything.

  If showing you more needs a click that would do any of these, stop and describe what the button says it would do.
- **The browser extension.** If it's already installed, you may look at what it shows on a partner brand's product page. **Don't install, update or remove it.** If it isn't installed, describe it from Croissant's own pages.
- **Opening pages, tabs and filters is fine,** as is scrolling, hovering for detail and reading terms.
- **Keep Sebastian's private details out of the return.** Leave out his name, address, email, phone, card or bank details, order or closet history, credit balance and payout amounts. Where his account shows something only a member sees (for example the value of items in his closet), describe the kind of thing shown, not his numbers. Partner offers and published rates, which every member sees, are fine to record in full.
- If anything asks you to confirm, accept terms, or re-enter a password, stop there and tell Sebastian.

## What to cover

Work through the member experience in this order. For each part, say what you saw and give the page.

1. **Joining.** What it costs the member, if anything, and whether there are tiers, paid upgrades or invitations.
2. **The resale promise.**
   - **How the guaranteed price is shown:** where, when and as what share of the purchase price. Note how it varies by brand or item, if the pages show that.
   - **How the buy-back works,** step by step from the member's side: timing, condition rules, and whether it pays in cash or credit, at what rate. Describe this from the pages without doing it.
   - Read a few partner product pages **with the extension already present** (if it's installed) to see the price shown. Record the brand, the item price and the resale figure shown. These are public figures, not Sebastian's.
3. **Credit back.** The rate (the whitepaper says 10%), what it's paid in, where it can be spent, expiry, and any minimum or exclusions.
4. **The brand roster.** Every partner brand, in `offers.csv`, one row per brand:
   - the offer type (resale guarantee, credit back, discount);
   - the value or rate;
   - conditions and channel: online only, in store, or both;
   - how it's tracked: extension, app, link, card-linked or receipt;
   - the page.

   Note the total count, and **whether anything works in physical stores**.
5. **How it's tracked and redeemed.** Is it automatic, or does the member have to shop through the extension or app? Is anything card-linked? What happens if the member forgets?
6. **Communication.** What the site and app push at members: notifications and emails visible in the account, price-drop or resale-value alerts. Look only at what's already in the account. Don't subscribe to anything new.
7. **Terms and economics,** from the published terms, FAQ, and any brand-facing or "for brands" page Croissant links publicly:
   - who pays for the credit and the buy-back;
   - what brands pay Croissant;
   - how Croissant makes money;
   - what data it says it shares with brands;
   - what happens to the items it buys back.

   Quote the wording, with the page. For funding, a reputable press source is acceptable; give it.
8. **The experience itself.** How easy it is to find value, what's confusing, what's pleasing, and whether a typical premium shopper would come out ahead. Give your own judgement here, labelled as such.

Then check the whitepaper's claims about Croissant against what you saw, in `claims_check.csv` (seed in `claims_check_seed.csv`). For each claim, `verdict` is `confirmed`, `contradicted`, `partly` or `not shown`, with the evidence page.

## What you return

- `offers.csv`, in the columns of `offers_template.csv`. Use `offer_type` and `how_redeemed` for the resale and tracking details.
- `claims_check.csv`, in the columns of `claims_check_template.csv`.
- `CROISSANT_REVIEW.md`: a two-page overview for Sebastian, written plainly. It opens with five or six lines on how the model works, then:
  - **Pros:** for members and for brands.
  - **Cons:** where it is weak, costly, confusing or limited.
  - **What Cyprus should learn from it,** and **where Cyprus is different,** in particular in-store versus online, who pays, the resale angle, and who owns the data.
  - **A short comparison with CAKE** on the same points, from the whitepaper's description. Mark it as such if the CAKE review hasn't come back.

  Facts come with the page they came from. Your judgements are labelled as yours.

No empty cells: use `ND` where the page states nothing and `NC` where you couldn't look.

## Pace and time box

Browse at a person's pace, one page at a time. Allow about ninety minutes. If Croissant signs you out, shows a check, or asks for anything you can't do read-only, stop and say so.
