import lief

hashme = lief.parse("bin/hashme")
libm   = lief.parse("/usr/lib/x86_64-linux-gnu/libm.so.6")


def swap(obj, a, b):
    symbol_a = next(filter(lambda e : e.name == a, obj.dynamic_symbols))
    symbol_b = next(filter(lambda e : e.name == b, obj.dynamic_symbols))
    b_name = symbol_b.name
    symbol_b.name = symbol_a.name
    symbol_a.name = b_name

hashme_log_sym = next(filter(lambda e : e.name == "logl", hashme.imported_symbols))
hashme_pow_sym = next(filter(lambda e : e.name == "powl", hashme.imported_symbols))

hashme_pow_sym.name = "cosl"
hashme_log_sym.name = "sinl"

swap(libm, "logl", "sinl")
swap(libm, "powl", "cosl")

hashme.add(lief.ELF.DynamicEntryRunPath("."))
hashme.write("bin/hashme.obf")
libm.write("bin/libtest.so.6")

print("done")
