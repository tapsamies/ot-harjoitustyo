```mermaid
sequenceDiagram
  Machine->>FuelTank:FuelTank()
  Machine->>FuelTank:fill(40)
  Machine->>Engine:Engine(FuelTank())
  Machine.drive->>Engine.start:FuelTank.consume(5)
  opt if engine is running
  Engine.is_running->>FuelTank:contents
  
  Machine.drive->>Engine.use_energy:fuel_tank.consume(10)
  end
  
  
  
  John-->>Alice: Great!
  Alice-)John: See you later!
 
 
 ```
