import aio_pika
import json
import logging
from typing import Callable, Awaitable
from ai_layer.core.events import BaseEvent
import os

logger = logging.getLogger(__name__)

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
EXCHANGE_NAME = "mir_ecosystem_exchange"

class EventBus:
    """
    Wrapper around aio-pika for publishing and consuming events.
    """
    def __init__(self):
        self.connection = None
        self.channel = None
        self.exchange = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(RABBITMQ_URL)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            EXCHANGE_NAME, aio_pika.ExchangeType.TOPIC
        )

    async def publish(self, routing_key: str, event: BaseEvent):
        """Publishes an event to the exchange."""
        if not self.exchange:
            await self.connect()
            
        message = aio_pika.Message(
            body=json.dumps(event.model_dump()).encode(),
            content_type="application/json"
        )
        await self.exchange.publish(message, routing_key=routing_key)
        logger.info(f"Published event {event.event_type} to {routing_key}")

    async def subscribe(self, queue_name: str, routing_key: str, callback: Callable[[BaseEvent], Awaitable[None]]):
        """Subscribes to a queue and registers an async callback."""
        if not self.channel:
            await self.connect()

        queue = await self.channel.declare_queue(queue_name, durable=True)
        await queue.bind(self.exchange, routing_key=routing_key)
        
        async def on_message(message: aio_pika.IncomingMessage):
            async with message.process():
                raw_data = json.loads(message.body.decode())
                # BaseEvent handles validation
                event = BaseEvent(**raw_data)
                await callback(event)
                
        await queue.consume(on_message)
        logger.info(f"Subscribed to {queue_name} with routing key {routing_key}")
