from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'

conn = ssh(host='', user='', password='')
conn.set_working_directory('')
pro = conn.process('./')


#import kmpwn
sys.path.append('/home/vagrant/kmpwn')
from kmpwn import *
#fsb(width, offset, data, padding, roop)

#config
context(os='linux', arch='i386')
context.log_level = 'debug'

FILE_NAME = ""
HOST = ""
PORT = 0

#elf = ELF(FILE_NAME)
#libc = ELF('./')
#
#main_addr = elf.symbols["main"]
#libc_binsh = next(elf.search("/bin/sh"))
#addr_bss = elf.bss()
#addr_dynsym = elf.get_section_by_name('.dynsym').header['sh_addr']

def exploit():
	
	pro.interactive()

if __name__ == "__main__":
	exploit()	
