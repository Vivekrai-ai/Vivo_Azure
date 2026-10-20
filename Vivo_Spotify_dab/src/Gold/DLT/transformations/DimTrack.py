from pyspark import pipelines as dp

@dp.table
def DimTrack_stg():
    df= spark.readStream.table("vivo_project.silver.DimTrack")
    return df

dp.create_streaming_table(name="DimTrack_gold")  

dp.create_auto_cdc_flow(target="DimTrack_gold", source="DimTrack_stg", keys=["track_id"],sequence_by="updated_at",stored_as_scd_type=2)
