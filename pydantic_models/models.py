from pydantic import BaseModel
from datetime import datetime


class EventStreamX(BaseModel):
    """
    Defines types and required fields for this event
    """

    id: str
    received_at: datetime
    anonymous_id: str
    context_app_version: str
    context_device_ad_tracking_enabled: bool
    context_device_manufacturer: str
    context_device_model: str
    context_device_type: str
    context_locale: str
    context_network_wifi: bool
    context_os_name: str
    context_timezone: str
    event: str
    event_text: str
    original_timestamp: datetime
    sent_at: datetime
    timestamp: datetime
    user_id: int
    context_network_carrier: str
    context_device_token: str = None
    context_traits_taxfix_language: str
