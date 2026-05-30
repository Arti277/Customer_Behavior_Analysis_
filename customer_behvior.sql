--
SELECT "Gender", SUM("Purchase Amount (USD)") AS revenue
FROM customer
GROUP BY "Gender";

--Q2.which customer used a discount but still spent more than the average purchase amount

select "Customer ID","Purchase Amount (USD)"
from customer
where "Discount Applied"='Yes' and "Purchase Amount (USD)">= (select AVG("Purchase Amount (USD)")from customer);


--Q3.