# Task Overview
Your FastAPI microservice for handling user notifications has developed critical slowdowns, specifically on the notification-sending endpoint. A synchronous blocking function is causing the entire server to become sluggish, degrading performance for other API routes and leading to a poor user experience. You are required to refactor this endpoint so that notification tasks are handled asynchronously, ensuring the API remains responsive and scalable.

# Guidance
- Focus on identifying operations in the notification endpoint that may be blocking the event loop.
- Utilize only the built-in features provided by FastAPI for handling background or async tasks.
- Avoid introducing external dependencies or async-IO libraries; adhere to native FastAPI tools.
- Aim for production-quality code that maintains responsiveness and reliability.
- Do not modify endpoints or files unrelated to the notification handling issue.

# Objectives
- Refactor the notification endpoint to eliminate all blocking calls from within async handlers.
- Ensure notification-sending operations are offloaded from the main event loop.
- Guarantee that all API endpoints continue to respond quickly, regardless of notification load.
- Maintain clear and consistent logging for all notification operations.

# How to Verify
- Submit multiple notification requests in quick succession and observe that responses are immediate.
- Access other API endpoints (such as a health check) and confirm they remain fast and unaffected by notification traffic.
- Monitor server logs to ensure there are no warnings regarding event loop blocking.
- Confirm the notification logic continues to execute reliably in the background after API responses are sent.
