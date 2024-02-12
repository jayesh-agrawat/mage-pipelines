```
CREATE OR REPLACE EXTERNAL TABLE `first-planet-411908.green_taxi.external_green_taxitripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://green-taxi-zoomcamp/green-taxi.parquet']
);
```

```
select * from `first-planet-411908.green_taxi.external_green_taxitripdata`;
```


-- Create a non partitioned table from external table
```
CREATE OR REPLACE TABLE `first-planet-411908.green_taxi.external_green_taxitripdata_non_partitioned`
as select VendorID ,lpep_pickup_datetime ,lpep_dropoff_datetime ,store_and_fwd_flag ,RatecodeID ,PULocationID ,DOLocationID ,passenger_count ,trip_distance ,fare_amount ,extra ,mta_tax ,tip_amount ,tolls_amount ,ehail_fee ,improvement_surcharge ,total_amount ,payment_type ,trip_type ,congestion_surcharge ,lpep_pickup_date ,lpep_dropoff_date ,TIMESTAMP(date_time) as date_time  ,__index_level_0__  from `first-planet-411908.green_taxi.external_green_taxitripdata`;
```

-- Create a partitioned table from external table
```
CREATE OR REPLACE TABLE `first-planet-411908.green_taxi.external_green_taxitripdata_partitioned`
PARTITION BY
  DATE(date_time) AS
SELECT * FROM `first-planet-411908.green_taxi.external_green_taxitripdata_non_partitioned` 
```
