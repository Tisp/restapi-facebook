import facebook

token = 'EAAZAhuHuxO3QBAJoPq7tnPSHmIy9Us7BzQAAjuzadq4KKrHtErh3nmlKGJ6dRfX4Be055utWijVRTmGivIQBoBmnBlJK7feDNT2cVlqIali04zIWrV3jU907tbUP2GUqqN4skTQrpAoZAZArdZAxZBXaFzLIikYUVix2cyNSg5Pnyb6ZAZCQmBNAqM2GuMzxOQZD'


graph = facebook.GraphAPI(access_token=token, version = '2.7')
events = graph.request('/100000108849996')
print (events)