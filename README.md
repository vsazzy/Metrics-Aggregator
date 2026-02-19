# Real-Time Metrics Aggregator (Senior Engineering Project)

A distributed system built to demonstrate high-scale data ingestion, stream processing, and container orchestration. 

## The Problem
Software companies handle millions of logs per second. Writing every single log to a primary database is slow and expensive. This project solves that by using a **"Buffer & Flush"** architecture: raw data is buffered in a fast message bus and aggregated in-memory before being stored as summarized metrics.

## Tech Stack
- **Language:** Python 3.9
- **Message Bus:** Redis Streams (for high-throughput persistence)
- **Containerization:** Docker & Docker Compose
- **Infrastructure:** Designed for AWS EC2 deployment

## Current Architecture (Day 1)
- **Producer Service:** Simulates a high-traffic API generating latency and error logs.
- **Redis Bus:** Uses Redis Streams (`XADD`) to ensure zero data loss if downstream services fail.

## How to Run
1. Clone the repository.
2. Ensure Docker Desktop is running.
3. Start the system:
   ```bash
   docker-compose up --build