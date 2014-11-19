__author__ = 'henry'

# Variables and defaults
image_number = 0
daytime = 1

# Initial load / creation of configuration
def load(location):
    try:
        configfile = open(location, 'r')
        print 'Configuration file found'
        for line in configfile: checkline(line)
        configfile.closed
    except IOError:
        print 'Configuration file not found'

def checkline(line):
    if 'image_number' in line:
        print "Found image_number"
        integers = [int(s) for s in line.split() if s.isdigit()]
        if len(integers):
            print 'Setting image number to: ' + str(integers[0])
            global image_number
            image_number = integers[0]
    elif 'daytime' in line:
        print "Found daytime"
        integers = [int(s) for s in line.split() if s.isdigit()]
        if len(integers):
            print 'Setting daytime to: ' + str(integers[0])
            global daytime
            daytime = integers[0]
    else:
        print 'line ignored'

def write(location):
    configfile = open(location, 'w')
    configfile.write('image_number = ' + str(image_number) + '\n')
    configfile.write('daytime = ' + str(daytime) + '\n')
    configfile.closed