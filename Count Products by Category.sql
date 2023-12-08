-- This is auto-generated code
SELECT
    Category, COUNT(*) AS ProducuctCount
FROM
    OPENROWSET(
        BULK 'https://datalakedtu9yfm.dfs.core.windows.net/files/product_data/products.csv',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
        HEADER_ROW = TRUE
    ) AS [result]
    GROUP BY Category;
