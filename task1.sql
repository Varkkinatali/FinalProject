SELECT c.login, COUNT(o.track)
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;