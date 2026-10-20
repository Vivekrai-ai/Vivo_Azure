from pyspark import pipelines as dp

@dp.table
def DimUser_stg():
    df= spark.readStream.table("vivo_project.silver.DimUser")
    return df

dp.create_streaming_table(name="DimUser_gold")  

dp.create_auto_cdc_flow(target="DimUser_gold", source="DimUser_stg", keys=["user_id"],sequence_by="updated_at",stored_as_scd_type=2)
