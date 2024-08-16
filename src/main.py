from fastapi import FastAPI
import uvicorn


from event_operathion.router import router as router_event_operathion

app = FastAPI()

app.include_router(router_event_operathion)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)