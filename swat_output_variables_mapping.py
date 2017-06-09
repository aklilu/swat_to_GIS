# imports
import sys, os
import numpy as np

#####################                               Functions                    ##########################

def write_to(filename,text_to_write):
    g = open(filename, 'w')
    g.write(text_to_write)
    g.close

def read_from(filename):
    g = open(filename, 'r')
    file_text = g.readlines()
    return file_text
    g.close
	
def update_progress(count,end_val, bar_length):   #bar_length=22
    percent = float(count) / end_val
    hashes = "#" * int(round(percent * bar_length))
    spaces = '_' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent Complete: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
print "_______________________________________________"
print("\nRunning Main Code!!")

###########################################################################################################


#################     Settings  #####################
rootdir = os.getcwd() + "\\"
ascii_out = rootdir + "ascii_out\\"
out_sub_file = rootdir + "TxtInOut\\output.hru"

#################       Main    #####################

# Read asci for reference
all_asc = read_from("bn_basins.asc")
asc_np_reference = np.array(all_asc[7:])
#asc_np_reference = np.dtype(int)

print "Reading ascii file!\n\nDone!"
print "_______________________________________________"

ncols = int(all_asc[0].split("         ")[1])
nrows = int(all_asc[1].split("         ")[1])
cell_size = float(all_asc[4].split("      ")[1])


print "Ascii properties:\n\tRows\t\t: "+ str(nrows) + "\n\tColumn\t\t: " + str(ncols) + "\n\tCell Size\t: " + str(cell_size)

print "_______________________________________________\n"

#################### Reading Basin Output #####################
print "Reading basin output"
sub_results = read_from(out_sub_file)

print sub_results[1].split("                                              ")[0] + "\n_______________________________________________"
print ''

print 'Processing ascii to hold Values'


ascii_text_for_replace = ""		#initialising

count = 0
for line in all_asc:
	ascii_text_for_replace = ascii_text_for_replace + line
	update_progress(count, nrows+4, 22)
	count = 1 + count
default_ascii = ascii_text_for_replace
ascii_text_for_replace = default_ascii= ascii_text_for_replace
ascii_text_for_SW_INITmm = default_ascii= ascii_text_for_replace
ascii_text_for_GW_RCHGmm = default_ascii= ascii_text_for_replace
ascii_text_for_PRECIPmm = default_ascii= ascii_text_for_replace
ascii_text_for_WYLDmm = default_ascii= ascii_text_for_replace
ascii_text_for_GW_Qmm = default_ascii= ascii_text_for_replace
ascii_text_for_PET = default_ascii= ascii_text_for_replace
ascii_text_for_SURQ_CNTmm = default_ascii= ascii_text_for_replace

print "\n\nDone"
print "_______________________________________________\n"

print "Searching for year..."
for i in range(9,len(sub_results)):
    if int(sub_results[i][30:34])>1000:
        year_ = int(sub_results[i][30:34])
        break










print "Year found\t: " + str(year_)
print "_______________________________________________\n"

print "filling raster images\n"

month_ = 1
count = 0

for line in sub_results:
	if line.split("       ")[0][28:29] == "0":
		print(line[32:33])
		if line[32:33] ==".":
			break        
		if int(line[30:34].strip(" ")) != int(month_):
			write_to(ascii_out + str(year_) + "_" + str(month_) + "ET.asc",ascii_text_for_replace)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "SOILWA.asc",ascii_text_for_SW_INITmm)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "RCH.asc",ascii_text_for_GW_RCHGmm)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "PRECIP.asc",ascii_text_for_PRECIPmm)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "WYLD.asc",ascii_text_for_WYLDmm)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "GW.asc",ascii_text_for_GW_Qmm)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "PET.asc",ascii_text_for_PET)
			write_to(ascii_out + str(year_) + "_" + str(month_) + "SURQ.asc",ascii_text_for_SURQ_CNTmm)
			month_ = month_ + 1
			ascii_text_for_replace = default_ascii
			ascii_text_for_SW_INITmm = default_ascii
			ascii_text_for_GW_RCHGmm = default_ascii
			ascii_text_for_PRECIPmm = default_ascii
			ascii_text_for_WYLDmm = default_ascii
			ascii_text_for_GW_Qmm = default_ascii
			ascii_text_for_PET = default_ascii
			ascii_text_for_SURQ_CNTmm = default_ascii




		if int(line[30:34])>1000:
			year_ = int(line[30:34])
			month_ = 1
			continue
		ascii_text_for_replace = ascii_text_for_replace.replace(" " + str(int(line[5:9])) + " ", " " + str( round((float(line[98:104])+float(line[158:164])),2)) + " ")#ET+RVAP
		ascii_text_for_SW_INITmm = ascii_text_for_SW_INITmm.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[108:114]),2)) + " ") #SW_INITmm
		ascii_text_for_GW_RCHGmm = ascii_text_for_GW_RCHGmm.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[138:144]),2)) + " ") #GW_RCHGmm
		ascii_text_for_PRECIPmm = ascii_text_for_PRECIPmm.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[48:54]),2)) + " ") #PRECIPmm
		ascii_text_for_WYLDmm = ascii_text_for_WYLDmm.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[258:264]),2)) + " ") #WYLDmm
		ascii_text_for_GW_Qmm = ascii_text_for_GW_Qmm.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[248:254]),2)) + " ") #GW_Qmm or baseflow
		ascii_text_for_PET = ascii_text_for_PET.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[87:94]),2)) + " ") #PET
		ascii_text_for_SURQ_CNTmm = ascii_text_for_SURQ_CNTmm.replace(" " + str(int(line[5:9])) + " ", " " + str(round(float(line[218:224]),2)) + " ") #SURQ_CNTmm
		count = count + 1
	#print(line[23:24])
	update_progress(count,len(sub_results)-10,22)

print "\nDone\nWriting to file.."


print "\nFinnished!"
print "_______________________________________________\n"

sys.exit()






















