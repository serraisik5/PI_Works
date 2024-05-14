import cx_Oracle

connection = cx_Oracle.connect('..')
cursor = connection.cursor()

create_median_table = """
CREATE TABLE median_temp (
    country VARCHAR2(100),
    median_val NUMBER
);
"""

cursor.execute(create_median_table)

insert_medians_query = """
INSERT INTO median_temp (country, median_val)
SELECT 
    country,
    MEDIAN(daily_vaccinations) AS median_val
FROM 
    vaccination
GROUP BY 
    country;
"""

cursor.execute(insert_medians_query)

update_vaccination_query = """
UPDATE vaccination v
SET v.daily_vaccinations = (
    SELECT 
        NVL(m.median_val, 0)
    FROM 
        median_temp m
    WHERE 
        v.country = m.country
)
WHERE 
    v.daily_vaccinations IS NULL;
"""

cursor.execute(update_vaccination_query)
connection.commit()

cursor.close()
connection.close()
