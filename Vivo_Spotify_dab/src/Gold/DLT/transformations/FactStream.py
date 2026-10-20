from pyspark import pipelines as dp

@dp.table
def FactStream_stg():
    df= spark.readStream.table("vivo_project.silver.FactStream")
    return df

dp.create_streaming_table(name="FactStream_gold")  

dp.create_auto_cdc_flow(target="FactStream_gold", source="FactStream_stg", keys=["stream_id"],sequence_by="stream_timestamp",stored_as_scd_type=2)
