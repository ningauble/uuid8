import time
import random

'''
Simple implementation of UUIDv8 with Timestamp Usage
Based on https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html
'''
def uuid8():
    
    ts, ns = divmod(time.time_ns(), 1_000_000_000)
    
    # make 28 bits of nanoseconds with a possible little loss of precision on decode
    ms = (ns >> 2) & 0xfffffff
    
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
    
    return '%s-%s-%s-%s-%s' % (part1[:8], part1[8:12], part1[12:], part2[:4], part2[4:])

if __name__ == '__main__':
    for x in range(0, 270000):
        uuid8()
