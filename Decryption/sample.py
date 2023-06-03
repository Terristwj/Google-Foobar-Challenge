import base64

# Your encripted message
MESSAGE = '''
D0IBBwoQERIdUEVTVEIVAAwSAEZCV0IKGwkeFwgUAQRJV19JUwABBgwWGQQKUElJUwAUFAYBABJJ\nV19JUwwcERsWEAgMGwBOWEVVEwobHQQYEggMGhFVUlNTUxQAGwoKHwAWVUVTUxMPFQcAABZVUlNT\nUxIPEQBOWEVVFAYcU0FUV0IeHQtTVRQ=
'''

# Your username
KEY = 'terristanwei'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
# Output:
# {'success' : 'great',
#  'colleague' : 'esteemed',
#  'efforts' : 'incredible',
#  'achievement' : 'unlocked',
#  'rabbits' : 'safe',
#  'foo' : 'win!'}