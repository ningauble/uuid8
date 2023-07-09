import time
import random

'''
Simple implementation of UUIDv8 with Timestamp Usage
Based on https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html
'''
def uuid8():
    
    ts, ms = str(time.time()).split(".")
    
    ts = int(ts)
    
    # make 28 bits of milliseconds with a possible little loss of precision on decode
    ms = round(float("0." + ms) * 0xfffffff)
    
    part1 = ts << 32
    
    # use first 16 bits of milliseconds
    part1 = part1 | ( (ms >> 12) << 16 )
    
    # ver 8, yes
    part1 = part1 | (8 << 12)
    
    # use last 12 bits of milliseconds
    part1 = part1 | ( ms & 0xfff )
    
    # ietf draft says var should be 0b10
    part2 = (random.randint( 0, 0x0fff ) | 0x2000) << 48
    
    # mighty random
    part2  = part2 | (random.randint(0, 0xffffffff) << 16)
    part2  = part2 | random.randint(0, 0xffff)
    
    part1 = str('{0:x}'.format(part1))
    part2 = str('{0:x}'.format(part2))
    
    uuidv8 = part1 + part2
    
    return '%s-%s-%s-%s-%s' % (uuidv8[:8], uuidv8[8:12], uuidv8[12:16], uuidv8[16:20], uuidv8[20:])

if __name__ == '__main__':
    print(uuid8())
