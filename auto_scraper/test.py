from items import Vehicle
from pipelines import AutoScraperPipeline
i = Vehicle(price="$ 19,000")
p = AutoScraperPipeline()
print dict(p._get_serialized_fields(i))
