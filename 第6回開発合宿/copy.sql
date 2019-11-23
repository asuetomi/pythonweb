-- 元のテーブルから Django の models に対応したテーブルにコピーする
INSERT INTO `suetomi`.`chatbot_siritori`
(
`ruby`,
`word`,
`used`)
SELECT `siritori`.`ruby`,
    `siritori`.`word`,
    `siritori`.`used`
FROM `suetomi`.`siritori`;


INSERT INTO `suetomi`.`chatbot_response`
(`keyword`,
`text`)
SELECT `response`.`keyword`,
    `response`.`text`
FROM `suetomi`.`response`;


INSERT INTO `suetomi`.`chatbot_words`
(`word`,
`mean`)
SELECT `words`.`word`,
    `words`.`mean`
FROM `suetomi`.`words`;

