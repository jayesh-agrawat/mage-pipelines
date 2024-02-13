## SQL Scripts
```
CREATE OR REPLACE EXTERNAL TABLE `first-planet-411908.green_taxi.external_green_taxitripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://green-taxi-zoomcamp/green-taxi.parquet']
);
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


-- Impact of partition
```
SELECT * FROM `first-planet-411908.green_taxi.external_green_taxitripdata_non_partitioned`
WHERE DATE(date_time) BETWEEN '2022-06-01' AND '2022-06-30'
ORDER BY PUlocationID ASC;
```

```
SELECT * FROM `first-planet-411908.green_taxi.external_green_taxitripdata_partitioned`
WHERE DATE(date_time) BETWEEN '2022-06-01' AND '2022-06-30'
ORDER BY PUlocationID ASC;
```

```
SELECT table_name, partition_id, total_rows
FROM `first-planet-411908.green_taxi.INFORMATION_SCHEMA.PARTITIONS`
WHERE table_name = 'external_green_taxitripdata_partitioned'
ORDER BY total_rows DESC;
```


-- Creating a partition and cluster table
```
CREATE OR REPLACE TABLE `first-planet-411908.green_taxi.external_green_taxitripdata_partitioned_cluster`
PARTITION BY DATE(date_time)
CLUSTER BY VendorID AS
SELECT * FROM `first-planet-411908.green_taxi.external_green_taxitripdata_non_partitioned`;
```

```
SELECT count(*) as trips
FROM `first-planet-411908.green_taxi.external_green_taxitripdata_partitioned`
WHERE DATE(date_time) BETWEEN '2022-06-01' AND '2022-06-30'
  AND VendorID=1;
```

```
  SELECT count(*) as trips
FROM `first-planet-411908.green_taxi.external_green_taxitripdata_partitioned_cluster`
WHERE DATE(date_time) BETWEEN '2022-06-01' AND '2022-06-30'
  AND VendorID=1;
```
