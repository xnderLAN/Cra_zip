import os
print("""
 _                          __  __     _____     _   _            _
| |    ___  __ _ _ __ _ __ |  \/  | __|_   _|__ | | | | __ _  ___| | __
| |   / _ \/ _` | '__| '_ \| |\/| |/ _ \| |/ _ \| |_| |/ _` |/ __| |/ /
| |__|  __/ (_| | |  | | | | |  | |  __/| | (_) |  _  | (_| | (__|   <
|_____\___|\__,_|_|  |_| |_|_|  |_|\___||_|\___/|_| |_|\__,_|\___|_|\_\ 
                                                            By Mazy_Lan \n""")


def banner():
	print("""
 _                          __  __     _____     _   _            _
| |    ___  __ _ _ __ _ __ |  \/  | __|_   _|__ | | | | __ _  ___| | __
| |   / _ \/ _` | '__| '_ \| |\/| |/ _ \| |/ _ \| |_| |/ _` |/ __| |/ /
| |__|  __/ (_| | |  | | | | |  | |  __/| | (_) |  _  | (_| | (__|   <
|_____\___|\__,_|_|  |_| |_|_|  |_|\___||_|\___/|_| |_|\__,_|\___|_|\_\ 
                                                            By Mazy_Lan \n""")



def crack(Wpath, zipath):
	import zipfile
	from tqdm import tqdm
	wordlist = Wpath
	zip_file = zipath
	try:
		zip_file = zipfile.ZipFile(zip_file)
		n_words = len(list(open(wordlist, "rb")))
		print("Total passwords to test:", n_words)
		with open(wordlist, "rb") as wordlist:
		    for word in tqdm(wordlist, total=n_words, unit="word"):
		        try:
		            zip_file.extractall(pwd=word.strip())
		        except:
		            continue
		        else:
		            print("[+] Password found:", word.decode().strip())
		            exit(0)
		print("[!] Password not found, try other wordlist.")
	except FileNotFoundError:
		print('[!] Error PathFile...!')

def build(zipname, files):
	from zipfile import ZipFile
	zipname = zipname
	files = files
	file_list = files.split()

	zipobj = ZipFile(zipname, 'w')
	try:
		for file in file_list:
			zipobj.write(file)
		zipobj.close
	except FileNotFoundError:
		print('[!] Error PathFile...!')

def info(zipfilepath):
	from zipfile import ZipFile
	try:
	    inf = ZipFile(zipfilepath,'r')
	    print("[*]List of files in Zip archiv:")
	    for a in inf.infolist():
	    	print(a.filename,)
	except FileNotFoundError:
	    print('[!] Error PathFile...!')




while True:
	cmd=input("\nzip> ")
	if(cmd == "help") or (cmd == "?"):
		print(""" \n
extract				specify full path to your zip file
fullextract			extract all files in zip archiv
build				build you archive Zip
info 				info about archiv
crack				cracka zip file protected by pass 
banner				show banner""")

	elif(cmd == "crack"):
		Wlist = input("[+]wordlist path: ")
		zipath = input("[+]zipfile path: ")
		crack(Wlist, zipath)
	elif(cmd == "exit") or (cmd == "quit"):
		break
	elif(cmd == "build"):
		zipname = input("zip filename: ")
		files = input("[+]Liste of files Ex file1 file2 ...: ")
		build(zipname, files)
	elif(cmd == 'info'):
		zipfilepath = input("[+]specify path to your file: ")
		info(zipfilepath)
	elif(cmd == 'banner'):
		banner()

