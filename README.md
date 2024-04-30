# Debug: 03 - Play with ELF symbols

From inside the devcontainer:

1) Build the main executable: `gcc main.c -o bin/hashme -lm`
2) Run the infect script (might have to adjust for libm location): `python infect.py`
3) Make hashme.obf executable: `chmod +x bin/hashme.obf`
4) Run `bin/hashme.obf`
5) Observe the error: `bin/hashme.obf: symbol lookup error: bin/hashme.obf: undefined symbol: cos, version GLIBC_2.29`

When opening the `bin/hashme.obf` file in IDA I get the following warning:
```
Unexpected entries in the PLT stub.
The file might have been modified after linking.
```