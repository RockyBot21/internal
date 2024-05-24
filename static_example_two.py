#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 02:36:00 2024

@author: user
"""
import time

# Mock function for authentication check
def is_authenticated():
    return True

class UnauthorizedException(Exception):
    pass

class RateLimitExceededException(Exception):
    pass

def authenticate(func):
    def wrapper(*args, **kwargs):
        # Perform authentication logic
        if not is_authenticated():
            raise UnauthorizedException("Authentication failed")
        return func(*args, **kwargs)
    return wrapper

def rate_limit(max_requests, interval):
    def decorator(func):
        request_count = 0
        last_request_time = None

        def wrapper(*args, **kwargs):
            nonlocal request_count, last_request_time

            # Check rate limit
            if last_request_time and time.time() - last_request_time < interval:
                if request_count >= max_requests:
                    raise RateLimitExceededException("Rate limit exceeded")
            else:
                request_count = 0

            # Update request count and time
            request_count += 1
            last_request_time = time.time()

            return func(*args, **kwargs)
        return wrapper
    return decorator

@authenticate
@rate_limit(max_requests=100, interval=60)
def protected_api_endpoint():
    # API endpoint implementation
    return "Success"

# Test the chained decorators
response = protected_api_endpoint()
print(response)
