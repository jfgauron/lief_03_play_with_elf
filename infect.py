#!/usr/bin/env python3
import lief

hashme = lief.parse("bin/hashme")
libm  = lief.parse("/usr/lib/x86_64-linux-gnu/libm.so.6")

def swap(obj, a, b):
    symbol_a = next(i for i in obj.dynamic_symbols if i.name == a)
    symbol_b = next(i for i in obj.dynamic_symbols if i.name == b)
    b_name = symbol_b.name
    symbol_b.name = symbol_a.name
    symbol_a.name = b_name

hashme_pow_sym = next(i for i in hashme.imported_symbols if i.name == "pow")
hashme_log_sym = next(i for i in hashme.imported_symbols if i.name == "log")

hashme_pow_sym.name = "cos"
hashme_log_sym.name = "sin"


swap(libm, "log", "sin")
swap(libm, "pow", "cos")

hashme.write("bin/hashme.obf")
libm.write("bin/libm.so.6")
