# Temu_ps — A Lightweight Multithreaded Port Scanner
---

## What is this?

`Temu_ps` is a command-line port scanner written in Python. It lets you check whether specific ports on a target IP address are open, either one at a time or across a range.

This project was built as a hands-on exercise to understand how TCP connections work at the socket level.

---

## Usage

```bash
python3 Temu_ps [ip_address] [port or port range] [number of threads]
```

### Single port scan
```bash
python3 Temu_ps 192.168.1.4 80 100
```

### Range scan
```bash
python3 Temu_ps 192.168.1.4 1-500 100
```

| Argument | Description |
|---|---|
| `ip_address` | Target host IP address |
| `port / port range` | A single port (e.g. `80`) or a range using `-` (e.g. `1-1024`) |
| `threads` | Number of worker threads. **Recommended: 100–200.** Don't go above 1024 |

---

## How it works

- Each port is checked using `socket.connect_ex()`, which returns `0` if the port is open and a non-zero error code if it isn't.
- A fresh socket is created **per connection attempt** — this is intentional. Sockets are stateful and not reusable across connections.
- For range scans, `ThreadPoolExecutor` is used to dispatch multiple connection checks concurrently, with each thread working independently.

---

## Known limitations & things I want to improve

This tool works, but it's not finished. Some things I'm aware of and plan to revisit:

-  **No timeout control** — slow or unresponsive hosts can cause threads to hang with no feedback
-  **No UDP support** — currently TCP only via `connect_ex()`
-  **No input validation** — bad arguments will crash ungracefully instead of giving a helpful error message

---

## What I learned building this

- How `socket.socket()` works and why a socket can't be shared across concurrent connections
- The difference between positional and keyword arguments in Python, and how `partial` + `executor.map` interact
- Why `ThreadPoolExecutor.map()` requires iterables of equal length when passing multiple arguments
- Why "more threads = faster" is not always true

---
