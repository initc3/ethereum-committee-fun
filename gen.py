from HoneyBadgerBFT.commoncoin import *
import cPickle as pickle
import sys, math, time

log_filename = 'gen.log'
log_file = open(log_filename, 'w')

plan = {
'n': [3, 10, 100, 1000, 10000, 1000000],
'fk': [2./3.]
}

#start_point = [60000, 51000]
#begin = False
 
for n in plan['n'] :
	for fk in plan['fk'] :
		k = (int)(math.ceil(n * fk))
#		if start_point[0] == n and start_point[1] == k :
#			begin = True
#		if not begin :
#			continue
		output_filename = 'sig-' + str(n) + '-' + str(k) + '.txt'
		output_file = open(output_filename, 'w')
		start_time = time.time()
		print "Generating: (%s, %s)" % (n, k)
		output = boldyreva.gen(n, k, 'hi')
		#pickle.dump(output, output_file)
		#print >>output_file, output
		output_file.write(output['VK'].encode('hex') + '\n')
		output_file.write(output['h'].encode('hex') + '\n')
		output_file.write(output['sig'].encode('hex') + '\n')
		duration = time.time() - start_time
		print 'Completed in %s seconds' % (duration)
		log_file.write(str(n) + ' ' + str(k) + ' ' + str(duration) + '\n')
		output_file.close()

#output_filename = 'test.txt'
#output_file = open(output_filename, 'w')

#output = {
#'n':10,
#'k':6,
#'m':"hi",
#'sigs':boldyreva.gen(10, 6, "hi")
#}
#print >>output_file, output

print "OK"
