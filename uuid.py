import time
import random

'''
Simple implementation of UUIDv8 with 60 bit Timestamp Usage
Based on https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html first with some changes in clock secuence part.
Later based on https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-04.html
Main doc is https://datatracker.ietf.org/doc/draft-ietf-uuidrev-rfc4122bis/07/
'''
def uuid8():
    
    ts, ns = divmod(time.time_ns(), 1_000_000_000)
    
    # make 28 bits of nanoseconds with a possible little loss of precision on decode
    ms = (ns >> 2) & 0xfffffff
    
    # some randoms for later bit operations
    rnd1 = random.randint(0, 0x0fff)
    rnd2 = random.randint(0, 0xffffffff)
    rnd3 = random.randint(0, 0xffff)
    
    bits = ts << 96
    
    # use first 16 bits of milliseconds
    bits = bits | ( (ms >> 12) << 80 )
    
    # ver 8, yes
    bits = bits | (8 << 76)
    
    # use last 12 bits of milliseconds
    bits = bits | ( ( ms & 0xfff ) << 64 )
    
    # ietf draft says var should be 0b10
    # other bits is random according to later drafts
    bits = bits | (rnd1 | 0x2000) << 48
    
    # mighty random fill
    bits  = bits | (rnd2 << 16)
    bits  = bits | rnd3
    
    bits = str('{0:x}'.format(bits))
    
    return '%s-%s-%s-%s-%s' % (bits[:8], bits[8:12], bits[12:16], bits[16:20], bits[20:])

if __name__ == '__main__':
    print(uuid8())
