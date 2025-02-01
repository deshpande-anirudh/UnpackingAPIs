## API Design

## Why is API design important?
A well-designed API ensures that the systems can integrate well, and also ensures security (rate-limiting, TLS termination, and scalability. 

Poor API design:
- Can overhaul order database during peak conditions
- Allow DDOS attacks (i.e. no control over rate)
- Provide access to unauthorized users

![alt](https://plantuml.online/png/ZLB1Rjim3BtxAmYVaaEmUmy5kYuRWhPhaAmVmCXC8aGMFOdswdvzQIafi2nUUfDDliV7zuX6E41vxonvAG4ZcFGiC1UUq5bZkOtm4Yca1XH1Sw1G5BaLPhTGpcU6wvg28RXRBaguWVB7_1TyuL1HY6NnJyC0UXwAy0q5DnWfWRwJc3sWSv2HCFd9iCITzIYM_LIPpb6paVahaZPusBPALcbt9BcaGz77FHHpptNZI2XFJp2OhCb7AxOZMFWjguGhYo-Vrxfv4zXGZBFCDFdgs1oity6AVhSKPVfVJvOPFFIlANJMP7VMlJVxm5xpS3qS9q23VJt8GL-1zPq-EVGVHbsY6hSiDkmZGKKEUwgWQWc4ONCIpms554IyQcMU7awCOclYLXCeJlSpPj_yDUdjqXybI7RbGrYXHlDeQqt3xwQVlwhJ1t17mJ5M8-e_f0qfiehOkC4BRr7lSGlnwD_r7OuXmnyhUw3NXgEQEQppGFs8xBjMzcgTDSdVls8_Astw1ZNsDcKQXHrvE5pcFTlfnQDISR1lAWTDkfvTG2-aZhm3)

Good API design:

![](https://plantuml.online/png/ZPF1RXCn48RlUOhH7b1pM46lI0L54122af3G1vZQqsIq6tjhpoODJy_OthIYxIhSB7l-p-D_VgCH7w3wr38vgG0ZcBoSO3cunfOD-px2JQIG2r04JKDXCYcbK7-0QbuRlzjHC0IpvRSAtaFrTVuRtlfWASIFBUzOhYxVlUbmGrUNrUI5844MgHW-e-0jHigGBoHc2rbE5WeD3YnRK18x5FPEQS-LzKXFAv8-k9DMYLObhtMZ-k5rgbfY4CQsN9ybSF7JGoGNMNXFmExEJwjpXYmNQtMa2zvGZ7M1ASVLjwqt3RiDhEY-foZJ4N-kLQV-mQ-U-cBFtDsdzT3PW4uamTWevPdYoUJbK-cQmfvDuGtR0m_ZqPbjy4xdtnuVRNvDEsRucfo5A2YQeBvJwmWEMtAWXLrBGcUzdvd6-KDBThDBE_xkvLj3SKtzFqLpR0BpXwpPvvsJBiB5AlNreuHiEjBI8pl5ADNdK08faYpP_xXzc6w9BprqFce0KoFVwJWoyLalwfQmoK7_PrGdsbv_g2t7VRPZaKGWlg7qCyO8OmExSQWA7_YFDZSu15OdPIGzygmrCvC3PCbnglyB)

----

## Architectural patterns/styles

- A set of *patterns* that define how components of a system interact, to solve the re-occurring problems.

### Key Characteristics:
1. **Components:** Defines the components, their roles, and relationships.
2. **Communication:** Specifies how components interact and share information.
3. **Constraints:** Sets rules or best practices for organizing systems (e.g., statelessness in REST).
4. **Behavior:** Describes how components handle operations, data flow, and scalability.

### Common Architectural patterns:
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

### Common Architectural styles

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

## REST (Representational State Transfer)
Architectural style that provides guidelines for how systems should communicate over the web, typically **using HTTP**. Simple and scalable. 

### REST Example:
- **GET Request:**  
   Request: `GET /orders?limit=10&page=1`  
   Response: Returns a list of 10 paginated orders.  

- **POST Request:**  
   Request: `POST /process-order`  
   Body: `{ "productId": 123, "quantity": 2 }`  
   Response: Acknowledges that the order processing request has been accepted.

### Characteristics:
#### Components
- **Client**: Makes requests to the server.
- **Server**: Provides resources or data in response to the client's request.
- **Resources**: Representations of objects or data that can be interacted with through HTTP methods like GET, POST, PUT/PATCH, DELETE.
  - **Resource Representations**: The data format in which a resource is presented (commonly JSON, XML, etc.).

#### **Constraints**
#####  **Statelessness**: No client context is stored on the server between requests.
- RESTful systems rely on a *stateless*, request-response mechanism. 
- Clients and servers communicate over HTTP where each request is independent of previous ones (stateless). 
- The interaction uses standard HTTP methods to perform operations on resources.

#####  **Uniform Interface**: A consistent, standardized way to access resources.
- RESTful APIs follow consistent patterns for interacting with resources using HTTP methods:
  - `GET`: Retrieve data (e.g., fetching a product list).
  - `POST`: Create a resource (e.g., placing an order).
  - `PUT`/`PATCH`: Update a resource (e.g., modifying user information).
  - `DELETE`: Remove a resource (e.g., deleting an order).

#####  **Cacheability**: Responses should explicitly state whether they can be cached to improve efficiency.
**Request**: `GET /products`

The server responds with a list of products and includes a **Cache-Control** header in the response:

**Response**:
```json
Cache-Control: public, max-age=3600
[
  { "id": 1, "name": "Laptop" },
  { "id": 2, "name": "Smartphone" }
]
```
The **Cache-Control** header tells the client that the response can be cached for 1 hour (`max-age=3600` seconds).
This means the client doesn't need to request the same data again for the next hour, improving efficiency by reducing the number of requests to the server.

##### **Layered System**: The architecture can be composed of layers to improve scalability and security.

Imagine an e-commerce platform with multiple layers:

1. **Client Layer**: The front-end user interface, like a web or mobile app, interacts with the server.
2. **API Gateway Layer**: An intermediary that routes incoming requests from clients to the appropriate backend services. It can also handle authentication, logging, and load balancing.
3. **Application Layer**: This is where the core business logic resides, such as processing orders, managing inventory, and handling payments.
4. **Data Layer**: A database or storage system that stores product information, user accounts, and order history.

In this layered system:
- **Scalability**: Different layers can scale independently. For example, if there’s a spike in traffic, you can scale the API Gateway or application layer without affecting the database layer.
- **Security**: The API Gateway layer can handle security concerns like authentication (using OAuth or API keys) and protect sensitive data, while the application layer focuses on business logic.

Each layer in the system only communicates with the layer directly below or above it, helping manage complexity and improve both security and scalability.

![](https://plantuml.online/png/NO_D2i8m48JlUOgb9mMjTm-2-8SYMgiliBQB12I9oPRIjpVQDBOUT-URdLaiM5jOFIKf5WOjoq8QL0p9Cjl33fbgRE283Ta4q7MRFzIOfooGfLOzr6-7s1ePU_fdlACZ8Tfuc2vYu1okf4h8wLMHOnXH-aWdiDlSO6QiBgk2tLXqiFVvBE_PQbkZZJRnsNgn2_B4fIBRGDQU-0eYgl5CJbnPDQJ2gL-_0ENaZ5RU7IeUhkSJbDung1SUZ5-r7l46)

#### **Behavior**: Describes how components handle operations, data flow, and scalability.
- When a client makes a request, the server processes that request, interacts with the relevant resources, and returns an appropriate representation (data).
- The behavior of a RESTful system focuses on handling requests and responses while ensuring scalability to accommodate varying loads efficiently. 



