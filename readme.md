# ITI Graduation Project - GIS

## Initial Proposal
### Problem Definition:
    
    Knowing how long it takes to get to a point/place from several different points.

    For example: Tourist buses will move from different places heading to the pyramids and they must arrive on time.

    Another example: School buses arrive at schools on time.

### Current Situation
    Input:
    - Different moving points
    - Fixed arrival point
    - Arrival time
    outputs:
    - Time and duration for each of the moving points

### Project Analysis
-
### Solution: Initial Phases Details
- QGIS Plugin to get the Journey routes
- Web App for Users/Bus drivers

### Project limitation
- 
### Next Steps
-
## Development Part

### Kafka for Real Time Tracking
- `kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic geodata_final`
- `kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic geodata_final --from-beginning`