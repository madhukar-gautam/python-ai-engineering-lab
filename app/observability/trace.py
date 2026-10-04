import time
import uuid
import logging

logger = logging.getLogger(__name__)


class TraceContext:

    def __init__(self):
        self.trace_id = str(uuid.uuid4())

    def start(self, operation: str):
        self.start_time = time.perf_counter()

        logger.info(
            "TRACE trace_id=%s",
            self.trace_id
        )

        logger.info(
            "├── %s",
            operation
        )

    def log_step(
        self,
        step: str,
        model: str | None = None,
        latency_ms: float | None = None
    ):
        logger.info(
            "├── %s",
            step
        )

        if model:
            logger.info(
                "│   ├── model=%s",
                model
            )

        if latency_ms is not None:
            logger.info(
                "│   └── latency=%.2fms",
                latency_ms
            )

    def end(self):
        latency_ms = (
            time.perf_counter() - self.start_time
        ) * 1000

        logger.info(
            "└── TOTAL latency=%.2fms",
            latency_ms
        )