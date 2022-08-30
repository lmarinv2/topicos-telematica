from redis import StrictRedis
import sys

print( "args=" + str(len(sys.argv)))

if len(sys.argv) < 5:
    print( "ingrese comando valido.")
    exit(len(sys.argv))

hostname=sys.argv[1]
password=sys.argv[2]
key=sys.argv[3]
value=sys.argv[4]

print(f'Setting "{key}" to "{value}"')
r = StrictRedis(host=hostname, port=6379, password=password, db=0)
r.set(key, value)
print(f'{key} was set successfully!')

print( "program ended.")
