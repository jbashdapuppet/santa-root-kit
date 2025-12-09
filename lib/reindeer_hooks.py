"""
reindeer_hooks — Simulated kernel hooking layer.
Nothing here modifies the system. It only pretends to expose hooks.
"""

FAKE_HOOKS = {
    "rudolph_syscall_hide": "Pretends to hide processes with a red nose.",
    "dasher_filecloak": "Pretends to conceal holiday-related files.",
    "vixen_shadow": "Pretends to cloak network connections.",
}

def get_available_hooks():
    """Return a dictionary of simulated hooks."""
    return FAKE_HOOKS

def load_hook(name):
    """Pretend to load a hook."""
    if name not in FAKE_HOOKS:
        raise ValueError("Hook not found")
    print(f"[reindeer] Loading hook: {name} — {FAKE_HOOKS[name]}")
    print("[reindeer] (No actual hooking happens.)")
