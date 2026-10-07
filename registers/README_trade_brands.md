# trade_brands.csv — brands that turn up on stockist lists

A living register of every brand name seen on a shop's brand list or locator, whether or not it is on
the map. Started 7 October 2026 from seen_register_2026-09-13 (804 names from the Mid-Atlantic shop
register) plus the Boyds profile. The map, with few exceptions, seats brands with at least a few US
stores of their own; this file keeps the ones that do not make that cut — small Italian shirtmakers,
knit houses, trade labels — because they say what the specialty stores buy and will be useful later.

Columns: brand · shops (count of shops seen carrying it) · carried_by (shop names, ;-separated) · states ·
first_seen · last_seen · us_own_stores (NC until read; 0 is a finding) · status (seated | queued |
briefed <job> | unassessed | benched | rejected) · note.

Rule: every stockist or shop-profile return appends to this file before anything else merges — new names
added, shops and last_seen updated on names already here. A name that reaches the map changes status to
seated and stays in the file.
