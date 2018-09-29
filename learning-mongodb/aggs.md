# Aggregation

#### Distinct
```
db.singer_metadata.distinct('source')
```


#### Groupby Count

```
db.singer_metadata.aggregate([
    {"$group" : {_id:"$source", count:{$sum:1}}}
])
```