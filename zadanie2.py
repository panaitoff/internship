from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs_with_nulls(spark, products_df, categories_df, product_category_df):
    # Присоединяем таблицы продуктов и категорий по соответствующим ключам
    joined_df = product_category_df.join(products_df, on='product_id', how='right') \
                                    .join(categories_df, on='category_id', how='right')
    
    # Получаем пары "Имя продукта - Имя категории"
    product_category_pairs = joined_df.select('product_name', 'category_name')
    
    # Получаем имена всех продуктов, у которых нет категорий
    products_with_null_category = products_df.join(product_category_df, on='product_id', how='left_anti') \
                                             .select('product_name')
    
    return product_category_pairs, products_with_null_category

# Создаем SparkSession
spark = SparkSession.builder \
                    .appName("ProductCategoryPairs") \
                    .getOrCreate()

# Создаем фиктивные данные для продуктов
products_data = [("product1", 1), ("product2", 2), ("product3", 3)]
products_df = spark.createDataFrame(products_data, ["product_name", "product_id"])

# Создаем фиктивные данные для категорий
categories_data = [("category1", 1), ("category2", 2), ("category3", 3)]
categories_df = spark.createDataFrame(categories_data, ["category_name", "category_id"])

# Создаем фиктивные данные для связей продуктов и категорий
product_category_data = [(1, 1), (1, 2), (2, 2), (3, 3)]
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

# Получаем результаты
product_category_pairs, products_with_null_category = get_product_category_pairs_with_nulls(spark, products_df, categories_df, product_category_df)

# Выводим результаты
print("Product-Category Pairs:")
product_category_pairs.show()

print("Products with Null Category:")
products_with_null_category.show()

# Останавливаем SparkSession
spark.stop()
