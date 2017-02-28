import random
import os
macaddress_prefix = ['9C99A0', 'E8BBA8', 'E44790', 'DC6DCD', 'CC2D83', 'C8F230', 'C09F05', 'BC3AEA', 'B0AA36', 'A81B5A', 'A43D78', 'A09347']
used_characters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
macaddress_string = random.choice(macaddress_prefix)
for i in range(6):
macaddress_string += random.choice(used_characters)
shell_command = "sudo ifconfig en0 ether {0}".format(macaddress_string)
command = "osascript -e  'do shell script \"{0}\" with administrator privileges'".format(shell_command)
os.popen(command)