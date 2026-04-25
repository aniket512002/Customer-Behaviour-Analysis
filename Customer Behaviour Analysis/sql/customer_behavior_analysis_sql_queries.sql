--Q1. Total number of products
SELECT COUNT(*) AS total_products
FROM amazon_sales_data;
--Q2. Top 10 highest rated products
SELECT product_name, rating
FROM amazon_sales_data
ORDER BY rating DESC
LIMIT 10;
--Q3. Top 10 most reviewed products
SELECT product_name, rating_count
FROM amazon_sales_data
ORDER BY rating_count DESC
LIMIT 10;
--Q4. Category-wise product count
SELECT category, COUNT(*) AS total_products
FROM amazon_sales_data
GROUP BY category
ORDER BY total_products DESC;
--Q5. Average rating per category
SELECT category,
       ROUND(AVG(rating),2) AS avg_rating
FROM amazon_sales_data
GROUP BY category
ORDER BY avg_rating DESC;
--Q6. Highest priced products
SELECT product_name, actual_price
FROM amazon_sales_data
ORDER BY actual_price DESC
LIMIT 10;
--Q7. Lowest priced products
SELECT product_name, actual_price
FROM amazon_sales_data
ORDER BY actual_price ASC
LIMIT 10;
--Q8. Products with highest discount
SELECT product_name, discount_percentage
FROM amazon_sales_data
ORDER BY discount_percentage DESC
LIMIT 10;
--Q9. Average price by category
SELECT category,
       ROUND(AVG(actual_price),2) AS avg_price
FROM amazon_sales_data
GROUP BY category
ORDER BY avg_price DESC;
--Q10. Total reviews per category
SELECT category,
       SUM(rating_count) AS total_reviews
FROM amazon_sales_data
GROUP BY category
ORDER BY total_reviews DESC;
--Q11. Products with rating above 4.5
SELECT product_name, rating
FROM amazon_sales_data
WHERE rating > 4.5
ORDER BY rating DESC;
--Q12. Discount vs price comparison
SELECT product_name,
       actual_price,
       discounted_price,
       discount_percentage
FROM amazon_sales_data
ORDER BY discount_percentage DESC;
--Q13. Top 5 categories with highest average discount
SELECT category,
       ROUND(AVG(discount_percentage),2) AS avg_discount
FROM amazon_sales_data
GROUP BY category
ORDER BY avg_discount DESC
LIMIT 5;
--Q14. Most popular categories (by reviews)
SELECT category,
       SUM(rating_count) AS total_reviews
FROM amazon_sales_data
GROUP BY category
ORDER BY total_reviews DESC
LIMIT 5;
--Q15. Products with high rating but low price (value for money)
SELECT product_name, rating, actual_price
FROM amazon_sales_data
WHERE rating >= 4.5 AND actual_price < (
    SELECT AVG(actual_price) FROM amazon_sales_data
)
ORDER BY rating DESC;