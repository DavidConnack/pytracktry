"""
Python wrapper for the TrackTry API
"""

import asyncio
import logging
import socket
import aiohttp
import async_timeout

BASE_URL = 'https://api.tracktry.com/v1'

_LOGGER = logging.getLogger(__name__)

class Tracking(object):
    """A class for the TrackTry API"""

    def __init__(self, loop, session, api_key):
        """Initialize the class."""
        self._loop = loop
        self._session = session
        self.api_key = api_key
        self._trackings = {}
        self._meta = {}
    
    async def get_trackings(self):
        """Get tracking information."""
        self._trackings = {}
        headers = {
            'Tracktry-Api-Key': self.api_key
        }
        url = f'{BASE_URL}/trackings/get'
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                response = await self._session.get(url, headers = headers)
                result = await response.json()
                try:
                    meta = result['meta']
                    if meta['code'] == 200:
                        results = result['data']['items']
                        self._trackings = results
                    else:
                        _LOGGER.error('Error code '+ meta['message'])
                except (TypeError, KeyError) as error:
                    _LOGGER.error(f'Error parsing data from TrackTry, {error}')
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error(f'Error connecting to TrackTry, {error}')
        return self._trackings

    async def add_package_tracking(self, tracking_number, carrier_code, title=None, comment=None):
        """Add tracking information."""
        headers = {
            'Tracktry-Api-Key': self.api_key
        }
        url = f'{BASE_URL}/trackings/post'
        data = {}
        data['tracking_number'] = tracking_number
        data['carrier_code'] = carrier_code
        if title is not None:
            data['title'] = title
        if comment is not None:
            data['comment'] = comment
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                await self._session.post(url, headers=headers, json=data)
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to TrackTry, %s', error)

    async def remove_package_tracking(self, carrier_code, tracking_number):
        """Delete tracking information."""
        headers = {
            'Tracktry-Api-Key': self.api_key
        }
        url = f'{BASE_URL}/trackings/{carrier_code}/{tracking_number}'
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                await self._session.delete(url, headers=headers)
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to TrackTry, %s', error)

    @property
    def trackings(self):
        """Return all trackings."""
        return self._trackings

