from utils.logger import get_logger

logger = get_logger(__name__)

def create_api_request_data(content):
    data = {
        "model": "deepseek-coder",
        "messages": [
            {"role": "system", "content": "You are a code analysis assistant."},
            {"role": "user", "content": content}
        ],
        "stream": False,
        "response_format": {"type": "json_object"}
    }
    logger.debug(f"Odesílaná data API: {data}")
    return data
