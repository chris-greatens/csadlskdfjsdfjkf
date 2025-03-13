-- Get the Master cared set for a player 
SELECT
  c.id,
  r.release_year,
  r.release_brand,
  r.release_name,
  c.card_no,
  c.card_title
FROM
  sets s,
  releases r,
  cards c,
  card_players cp,
  players p
WHERE
  r.id = s.release_id
  AND p.player_name = 'Hoyt Wilhelm'
  AND cp.player_id = p.id
  AND cp.card_id = c.id
  AND c.set_id = s.id
ORDER BY r.release_year, r.release_brand, r.release_name, c.card_no;

-- List all cards in a collection
select
  r.release_year,
  r.release_brand,
  r.release_name,
  c.card_no,
  c.card_title,
  p.player_name
from
  sets s,
  releases r,
  cards c,
  card_players cp,
  collection_cards cc,
  players p
where
  cc.collection_id = 1
  and r.id = s.release_id
  and cp.player_id = p.id
  and cp.card_id = c.id
  and c.set_id = s.id
  and cc.card_id = c.id
ORDER BY r.release_year, r.release_brand, r.release_name, c.card_no;