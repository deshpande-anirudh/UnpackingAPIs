## API Design

---

### Why is API design important?
A well-designed API ensures that the systems can integrate well, and also ensures security (rate-limiting, TLS termination, and scalability. 

Poor API design:
- Can overhaul order database during peak conditions
- Allow DDOS attacks (i.e. no control over rate)
- Provide access to unauthorized users

![alt](https://plantuml.online/png/ZLB1Rjim3BtxAmYVaaEmUmy5kYuRWhPhaAmVmCXC8aGMFOdswdvzQIafi2nUUfDDliV7zuX6E41vxonvAG4ZcFGiC1UUq5bZkOtm4Yca1XH1Sw1G5BaLPhTGpcU6wvg28RXRBaguWVB7_1TyuL1HY6NnJyC0UXwAy0q5DnWfWRwJc3sWSv2HCFd9iCITzIYM_LIPpb6paVahaZPusBPALcbt9BcaGz77FHHpptNZI2XFJp2OhCb7AxOZMFWjguGhYo-Vrxfv4zXGZBFCDFdgs1oity6AVhSKPVfVJvOPFFIlANJMP7VMlJVxm5xpS3qS9q23VJt8GL-1zPq-EVGVHbsY6hSiDkmZGKKEUwgWQWc4ONCIpms554IyQcMU7awCOclYLXCeJlSpPj_yDUdjqXybI7RbGrYXHlDeQqt3xwQVlwhJ1t17mJ5M8-e_f0qfiehOkC4BRr7lSGlnwD_r7OuXmnyhUw3NXgEQEQppGFs8xBjMzcgTDSdVls8_Astw1ZNsDcKQXHrvE5pcFTlfnQDISR1lAWTDkfvTG2-aZhm3)

Good API design:

![](https://plantuml.online/png/ZPF1RXCn48RlUOhH7b1pM46lI0L54122af3G1vZQqsIq6tjhpoODJy_OthIYxIhSB7l-p-D_VgCH7w3wr38vgG0ZcBoSO3cunfOD-px2JQIG2r04JKDXCYcbK7-0QbuRlzjHC0IpvRSAtaFrTVuRtlfWASIFBUzOhYxVlUbmGrUNrUI5844MgHW-e-0jHigGBoHc2rbE5WeD3YnRK18x5FPEQS-LzKXFAv8-k9DMYLObhtMZ-k5rgbfY4CQsN9ybSF7JGoGNMNXFmExEJwjpXYmNQtMa2zvGZ7M1ASVLjwqt3RiDhEY-foZJ4N-kLQV-mQ-U-cBFtDsdzT3PW4uamTWevPdYoUJbK-cQmfvDuGtR0m_ZqPbjy4xdtnuVRNvDEsRucfo5A2YQeBvJwmWEMtAWXLrBGcUzdvd6-KDBThDBE_xkvLj3SKtzFqLpR0BpXwpPvvsJBiB5AlNreuHiEjBI8pl5ADNdK08faYpP_xXzc6w9BprqFce0KoFVwJWoyLalwfQmoK7_PrGdsbv_g2t7VRPZaKGWlg7qCyO8OmExSQWA7_YFDZSu15OdPIGzygmrCvC3PCbnglyB)

----

### Architectural patterns/styles

- A set of *patterns* that define how components of a system interact, to solve the re-occurring problems.

### Key Characteristics:
1. **Structure:** Defines the components, their roles, and relationships.
2. **Communication:** Specifies how components interact and share information.
3. **Constraints:** Sets rules or best practices for organizing systems (e.g., statelessness in REST).
4. **Behavior:** Describes how components handle operations, data flow, and scalability.

#### Common Architectural patterns:
##### 1. **Monolithic Architecture:**  
   - A single, tightly coupled application.  
   - Example: Legacy e-commerce systems.


##### 2. **Microservices Architecture:**  
   - Application is divided into independent services communicating over APIs.  
   - Example: Modern cloud-based applications like Amazon.


##### 3. **Event-Driven Architecture:**  
   - Components respond to and communicate via events.  
   - Example: Payment processing systems.


##### 4. **Client-Server Architecture:**  
   - Separation between a client (front-end) and a server (back-end).  
   - Example: Web applications.


##### 5. **REST (Representational State Transfer):**  
   - Web service design style that uses HTTP methods for resource operations.  
   - Example: APIs for social media platforms.


##### 6. **Layered Architecture:**  
   - Divides applications into layers (e.g., presentation, business logic, and data).  
   - Example: Enterprise applications.

#### Common Architectural styles

##### 1. **REST (Representational State Transfer)**  
   - **Purpose:** Resource-oriented web services  
   - **Communication:** Stateless, HTTP-based  
   - **Use Cases:** Public APIs (e.g., social networks)  
   - **Example:** `GET /products/{id}`

##### 2. **WebSockets**  
   - **Purpose:** Full-duplex, real-time communication between clients and servers  
   - **Communication:** Persistent TCP connection (bi-directional)  
   - **Use Cases:** Chat applications, live stock updates, multiplayer games  
   - **Example:** A server pushes updates to all connected clients when an event occurs

##### 3. **MQTT (Message Queuing Telemetry Transport)**  
   - **Purpose:** Lightweight messaging protocol for IoT and constrained networks  
   - **Communication:** Publish/Subscribe pattern over TCP  
   - **Use Cases:** IoT applications like smart homes, sensor networks  
   - **Example:** A sensor publishes temperature data to a broker, and clients subscribe to updates

##### 4. **GraphQL**  
   - **Purpose:** Client-driven query language for APIs  
   - **Communication:** Single endpoint with flexible queries  
   - **Use Cases:** Mobile and frontend-heavy applications  
   - **Example:** Fetching multiple fields from different resources in one request

##### 5. **gRPC (gRPC Remote Procedure Call)**  
   - **Purpose:** High-performance communication protocol  
   - **Communication:** HTTP/2, binary serialization (Protocol Buffers)  
   - **Use Cases:** Microservices communication, low-latency applications  
   - **Example:** Direct method calls between services

##### 6. **SOAP (Simple Object Access Protocol)**  
   - **Purpose:** Formal, contract-based protocol for web services  
   - **Communication:** XML over HTTP or other protocols  
   - **Use Cases:** Enterprise systems (e.g., banking)  
   - **Example:** Strictly structured request-response for financial transactions

##### 7. **Server-Sent Events (SSE)**  
   - **Purpose:** One-way communication from server to client  
   - **Communication:** Persistent HTTP connection  
   - **Use Cases:** Live news feeds, real-time notifications  
   - **Example:** Browser keeps listening to server updates  

----

### REST (Representational State Transfer)
Provides guidelines for how systems should communicate over the web, typically **using HTTP**. Simple and scalable. 

Certainly! Here's the merged version:

#### Key Characteristics of REST:
1. **Structure**: Defines the components, their roles, and relationships.
   - **Client**: Makes requests to the server.
   - **Server**: Provides resources or data in response to the client's request.
   - **Resources**: Representations of objects or data that can be interacted with through HTTP methods like GET, POST, PUT, DELETE, etc.
   - **Representations**: The data format in which a resource is presented (commonly JSON, XML, etc.).


2. **Communication**: Specifies how components interact and share information.
   - RESTful systems rely on a stateless, request-response mechanism. Clients and servers communicate over HTTP where each request is independent of previous ones (stateless). The interaction uses standard HTTP methods to perform operations on resources.


3. **Constraints**: Sets rules or best practices for organizing systems.
   - **Statelessness**: No client context is stored on the server between requests.
   - **Uniform Interface**: A consistent, standardized way to access resources.
   - **Cacheability**: Responses should explicitly state whether they can be cached to improve efficiency.
   - **Layered System**: The architecture can be composed of layers to improve scalability and security.


4. **Behavior**: Describes how components handle operations, data flow, and scalability.
   - When a client makes a request, the server processes that request, interacts with the relevant resources, and returns an appropriate representation (data).
   - The behavior of a RESTful system focuses on handling requests and responses while ensuring scalability to accommodate varying loads efficiently. 


#### Key Principles of REST:

##### 1. **Stateless Communication:**  
   - Each request from a client to a server must contain all the information needed to understand and process the request.  
   - The server **does not** store any session information between requests.


##### 2. **Client-Server Separation:**  
   - The client and server operate independently.  
   - The client only knows how to use the API, while the server handles the backend logic.


##### 3. **Uniform Interface:**  
   - RESTful APIs follow consistent patterns for interacting with resources using HTTP methods:
     - `GET`: Retrieve data (e.g., fetching a product list).
     - `POST`: Create a resource (e.g., placing an order).
     - `PUT`/`PATCH`: Update a resource (e.g., modifying user information).
     - `DELETE`: Remove a resource (e.g., deleting an order).


##### 4. **Resource-Based:**  
   - Everything in a REST API is considered a resource, represented by a unique URL (e.g., `/orders`, `/users`).


##### 5. **Stateless Responses:**  
   - Responses often include representations of resources, typically in formats like JSON or XML.

#### REST Example in E-Commerce:

- **GET Request:**  
   Request: `GET /orders?limit=10&page=1`  
   Response: Returns a list of 10 paginated orders.  

- **POST Request:**  
   Request: `POST /process-order`  
   Body: `{ "productId": 123, "quantity": 2 }`  
   Response: Acknowledges that the order processing request has been accepted.



