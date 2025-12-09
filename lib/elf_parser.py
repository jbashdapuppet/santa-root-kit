"""
elf_parser — A completely fake ELF parser used to mislead players.

It returns hard-coded, decorative output and does not inspect any binaries.
"""

def parse_elf(path):
    print(f"[elf_parser] Pretending to analyze ELF at: {path}")
    return {
        "magic": "0x7F454C46",
        "entry_point": "0x0000SANTA",
        "notes": [
            "This binary contains enhanced jolliness.",
            "Signed by NorthPole Security Authority."
        ]
    }
