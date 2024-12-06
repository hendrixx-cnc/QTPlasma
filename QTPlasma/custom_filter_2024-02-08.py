INCREMENTAL = False

def custom_pre_parse(data):
    global INCREMENTAL
    if data[0] == '%':
        data = None # add some preamble codes if needed
    elif data[0] == 'P':
        data = 'F#<_hal[plasmac.cut-feed-rate]>'
    elif data[:3] == 'G91' and not data[:4] == 'G91.':
        data = None
        INCREMENTAL = True
    elif data[:3] == 'G00':
        if INCREMENTAL:
            data = f'\nG91\n{data}'
            INCREMENTAL = False
    elif data[:3] == 'M30':
        data = '\nG90\nM30' # add some postamble codes if needed
        INCREMENTAL = False
    elif data[:2] == 'M3' and not '$0' in data:
        data = 'M3 $0'
    elif data[:2] == 'M5' and not '$0' in data:
        data = 'M5 $0'
    return(data)
self.custom_pre_parse = custom_pre_parse
