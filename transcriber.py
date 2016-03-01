''' PYngwar Transcriber version 0.2
Mar 1, 2016
Ondo Carniliono - Pedro Bernardinelli
ondo@quenya101.com

Current problems: possible final vowel being deleted?

Usage: the load_and_transcribe function gets a text in Roman alphabet and transcribe for the Tengwar LaTeX codes.
the main function outputs to a file. It isn't needed for the usage of the script 
'''

letters_change = {"\n": "\n ", "tt": "T", "pp" : "P", "k" : "c", "kk" : "C", "cc" : "C", "qu" : "q", "nd" : "d", "mb" : "b", "ngw" : "G", "ng" : "g", "th" : "1", "ff" : "F", "hw" : "2", "nt" : '3', "mp" : "4", "nc" : "5", "nq" : '6', 'nn' : 'N', 'mm' : "M", "ñw" : "Ñ", "rd" : "7", "ll" : "L", "ld" : "8", "ss" : "z", "hy" : "9", " r" : " R", "hl" : "#l", "hr" : "#R", " h" : " H",  "ë" : "e", "ai" : "@a", "ei" : "@e", "oi" : "@o", "ui" : "@u", "au" : "0a", "eu" : "0e", "iu" : "0u", "ou" : "0o", " ea" : " EA",  "ea" : "eA", "eo" : "eO", "ae" : "aE", "oe" : "oE", "ua" : "uA", "ue" : "uE", "oa" : "oA", "uo" : "uO", "ia": "iA", "ie" : "iE", "io" : "iO", "iu" : "iU"," a" : " A", " e" : " E", " i": " I", " o" : " O", " u": " U", " y" : " Y", "s " : "ç ", "ks" : "x", "\n " : "\n"}

# " á" : " Á", " é" : " É", " í" : " Í", " ó" :  " Ó", " ú" : " Ú"
tengwar_equivalence = {"t" : "\Ttinco ", "p" : "\Tparma ", "c" : "\Tcalma ", "q" : "\Tquesse ", "d" : "\Tando ", "b" : "\Tumbar ",  "g" : "\Tanga ", "G" : "\Tungwe ", "1" : "\Tthuule ", "f" : "\Tformen ", "h" : "\Taha ", "2" : "\Thwesta ", "3" : "\Tanto ", "4" : "\Tampa ", "5" : "\Tanca ", "6" : "\Tunque ", "n" : "\Tnuumen ", "m" : "\Tmalta ", "ñ" : "\Tnoldo ", "Ñ" : "\Tnwalme ", "r" : "\Toore ", "v" : "\Tvala ", "Y" : "\Tanna \TTtwodotsbelow ", "w" : "\Tvilya ",  "R" : "\Troomen ", "7" : "\Tarda ", "l" : "\Tlambe ", "8" : "\Talda ", "s" : "\Tsilme ", "S" : "\Tsilmenuquerna ", "z" : "\Tesse ", "Z" : "\Tessenuquerna ", "H" : "\Thyarmen ", "@" : "\Tyanta ", "0" : "\Tuure ", "#" : "\Thalla ", " " : " \Ts ", "a" : "\TTthreedots ", "e" : "\TTacute ", "i" : "\TTdot ", "o" : "\TTrightcurl ", "u" : "\TTleftcurl ", "y" : "\TTtwodotsbelow ", "A" : "\Ttelco \TTthreedots ", "E" : "\Ttelco \TTacute ", "I" : "\Ttelco \TTdot ", "O" : "\Ttelco \TTrightcurl ", "U" : "\Ttelco \TTleftcurl ", "á" : "\Taara \TTthreedots ", "é" : "\Taara \TTacute ", "í": "\Taara \TTdot ", "ó" : "\Taara \TTrightcurl ", "ú" : "\Taara \TTleftcurl ", "T" : "\Ttinco \TTdoubler ", "P" : "\Tparma \TTdoubler ", "C" : "\Tcalma \TTdoubler ", "F" : "\Tfoormen \TTdoubler ", "N" : "\Tnuumen \TTdoubler ", "M" : "\Tmalta \TTdoubler ", "L" : "\Tlambe \TTdoubler ", "ç" : "\Tcurlyhook ", "x" : "\Tcalma \Tlefthook ", "\n" : "\n\n", "!" : "\Texclamation", "." : "\Tcolon", "?" : "\Tquestion", "(" : "\Tparenthesis", ")" : "\Tparenthesis", "," : "\Tcentereddot", "-" : " ", ';' : "\Tcentereddot", "'" : " "}

vowels = ["a", "e", "i", "o", "u"]

accented_vowels = vowels +  ["á", "é", "í", "ó", "ú", "ë", "ä", "ö"]


def replacer(text):
	''' (str) -> str
	Takes special characters (doubled consonants, consonants like nt or th, nuquerna cases)
	and substitutes for the single characters in letters_change
	'''
	cons_keys = list(letters_change.keys())

	text = " " + text.lower()

	for i in range(0, len(cons_keys)):
		text = text.replace(cons_keys[i], letters_change[cons_keys[i]])
	for i in range(0, len(vowels)):
		esse = "z" + vowels[i]
		esse_nuquerna = "Z" + vowels[i]
		text = text.replace(esse, esse_nuquerna)

	for i in range(0,len(vowels)):
		silme = "s" + vowels[i]
		silme_nuquerna = "S" + vowels[i]
		text = text.replace(silme, silme_nuquerna)

	for i in range(0, len(accented_vowels)):
		romen = "r" + accented_vowels[i]
		romen_change = "R" + accented_vowels[i]
		text = text.replace(romen, romen_change)
	
	return text[1:]

def transcriber(text):
	a = ""
	for i in range(len(text)):
		a = a + tengwar_equivalence[text[i]]

	return a


def tengwar_roman_to_tex(text):
	a = replacer(text)
	tengwar = transcriber(a)
	return tengwar

'''
def load_and_transcribe():
	file_name = input("Enter the input file name: ")

	with open(file_name, 'r', encoding='utf-8') as input_file:
		text = input_file.read()

	scribe = tengwar_roman_to_tex(text)

	return scribe
'''

def load_and_transcribe():
	file_name = input("Enter the input file name: ")

	scribe = ''

	with open(file_name, 'r', encoding='utf-8') as input_file:
		for line in input_file:
			scribe = scribe + tengwar_roman_to_tex(line)


	return scribe




def save(text):
	file_name = input("Enter the output file name: ")

	with open(file_name, "w", encoding='utf-8') as output_file:
		output_file.write(text)

def main():
	text = load_and_transcribe()

	save(text)
