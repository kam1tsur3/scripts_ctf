#!/usr/bin/python3
ar = [143,224,86,71,69,249,251,10,253,96,0,114,121,72,68,119,179,127,191,114,13,159,207,114,249,0,0,79,9,192,95,0,174,239,118,2,0,187,54,65,21,0,156,36,0,65,138,0,222,49,59,95,114,34,0,202,155,120,200,95,73,55,11,82,0,179,231,31,69,252,68,176,174,7,54,87,0,73,110,108,137,121,0,226,165,127,26,90,66,3,247,88,155,20,191,220,0,0,78,241,113,78,1,122,0,110,206,219,212,188,243,57,164,80,1,91,158,10,68,193,1,14,163,228,11,171,193,55,48,0,0,24,188,0,94,243,84,3,52,0,20,73,175,84,82,0,69,149,143,73,16,35,48,146,241,13,239,48,63,206,201,16,96,126,32,134,80,52,151,209,216,0,0,227,252,92,191,110,25,46,34,15,126,135,152,89,211,237,183,239,252,102,59,36,54,34,210,90,213,47,23,205,187,81,127,140,199,23,127,164,252,225,221,53,7,32,216,173,65,63,198,105,180,7,214,239,158,226,141,149,210,249,73,123,71,91,199,235,203,239,133,187,217,95,103,243,204,107,255,226,207,59,127,249,131,249,241,7,181,66,38,73,218,102,0,159,106,117,171,231,197,32,249,218,75,217,199,221,178,128,159,248,128,213,51,0,241,75,127,73,46,210,252,250,102,59,122,13,85,56,199,31,11,248,152,209,107,15,240,46,223,54,125,135,132,231,216,105,2,227,187,226,175,222,96,2,43,109,191,83,213,211,184,91,86,238,172,97,100,16,85,139,32,191,110,223,37,238,155,133,251,210,252,18,157,210,139,176,9,11,128,241,38,204,1,183,168,13,153,223,60,107,16,62,241,154,32,223,90,51,73,22,121,55,20,177,73,161,177,164,252,206,255,103,110,141,196,163,141,94,4,138,31,91,182,108,250,173,200,127,113,69,154,126,59,82,253,84,253,200,7,242,61,96,149,226,52,134,223,96,237,180,91,21,73,56,0,235,73,243,173,176,100,242,47,147,44,156,149,38,11,8,127,196,228,226,174,95,88,57,40,71,65,24,91,127,84,9,109,37,91,223,157,254,228,103,157,213,146,72,203,211,0,77,239,180,218,205,189,91,126,191,40,31,242,131,90,19,164,82,53,211,246,171,243,121,69,249,243,31,169,20,195,178,32,181,244,236,95,191,16,183,191,174,249,204,169,167,176,59,241,41,43,52,211,183,59,157,251,156,228,119,254,11,107,25,101,108,153,44,43,12,113,171,39,254,193,77,92,92,146,0,206,183,126,196,196,254,127,17,80,173,159,38,246,101,212,196,16,201,81,90,245,215,61,166,176,105,227,248,189,173,179,197,198,60,54,181,62,143,231,163,247,126,79,118,145,96,54,169,16,109,206,11,72,27,106,154,55,183,26,184,111,251,85,210,55,127,242,205,23,221,46,212,29,27,128,73,71,19,252,203,231,51,212,59,127,198,12,65,191,254,233,231,157,89,47,250,254,79,244,230,238,183,155,255,142,223,229,214,110,157,115,236,243,73,231,126,193,174,175,251,130,89,213,0,0,185]
png_header = "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52"
l = len(png_header)
answer = ""
"""
print(int(len(ar)/16))
for i in range(0, 16):
	#j = int(len(ar)/16) - 1
	print("phase"+str(i))
	for j in range(int(len(ar)/16)):
		if png_header[i] == chr(ar[j*16+i]):
			#answer += ("%02d"%j)
			#break
			
			print(j)
		#j -= 1
		#if j < 0:
		#	print("error")
		#	exit()
"""
for i in range(0, 16):
	#j = int(len(ar)/16) - 1
	#print("phase"+str(i))
	for j in range(int(len(ar)/16)):
		if png_header[i] == chr(ar[j*16+i]):
			answer += str(j)
			answer += "0"
			break
			#print("%02d" % j)
		#j -= 1
		#if j < 0:
		#	print("error")
		#	exit()
#"""

print(answer)

