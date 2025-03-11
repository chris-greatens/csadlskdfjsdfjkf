INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no BETWEEN 1 
   AND 80 
   AND c.set_id = 4 
   AND v.variation = 'Red Back';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no BETWEEN 1 
   AND 80 
   AND c.set_id = 4 
   AND v.variation = 'Black Back';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no BETWEEN 131 
   AND 190 
   AND c.set_id = 4 
   AND v.variation = 'White Back';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no BETWEEN 131 
   AND 190 
   AND c.set_id = 4 
   AND v.variation = 'Gray Back';

INSERT INTO variations (variation) VALUES ('Yellow/Orange Tigers logo');
INSERT INTO variations (variation) VALUES ('Yellow Tigers logo');

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 146 
   AND c.set_id = 4 
   AND v.variation = 'Yellow/Orange Tigers logo';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 146 
   AND c.set_id = 4 
   AND v.variation = 'Yellow/ Tigers logo';

INSERT INTO variations (variation) VALUES ('Red Star on Copyright Line');
INSERT INTO variations (variation) VALUES ('Black Star on Copyright Line');

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 307 
   AND c.set_id = 4 
   AND v.variation = 'Red Star on Copyright Line';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 307 
   AND c.set_id = 4 
   AND v.variation = 'Black Star on Copyright Line';

INSERT INTO variations (variation) VALUES ('Full Black Border Yankees Logo');
INSERT INTO variations (variation) VALUES ('No Black Border Yankees Logo');

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 311 
   AND c.set_id = 4 
   AND v.variation = 'Full Black Border Yankees Logo';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 311 
   AND c.set_id = 4 
   AND v.variation = 'No Black Border Yankees Logo';

INSERT INTO variations (variation) VALUES ('BB Stitching Points Left');
INSERT INTO variations (variation) VALUES ('BB Stitching Points Right');

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 312 
   AND c.set_id = 4 
   AND v.variation = 'BB Stitching Points Left';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 312 
   AND c.set_id = 4 
   AND v.variation = 'BB Stitching Points Right';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 313 
   AND c.set_id = 4 
   AND v.variation = 'BB Stitching Points Left';

INSERT INTO card_variations (card_id, variation_id)
SELECT c.id, v.id
  FROM variations v, cards c
 WHERE c.card_no = 313 
   AND c.set_id = 4 
   AND v.variation = 'BB Stitching Points Right';