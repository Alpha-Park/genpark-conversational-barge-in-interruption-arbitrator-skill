# genpark-barge-in

Apply transcript, supplied echo score and duration rules to conversational interruptions; estimate playback truncation. No audio echo detection or playback control.

Python 3.9+; standard library runtime; MIT license.

## Install and run

Download `genpark-barge-in.mcpb` from [GitHub Releases](https://github.com/Alpha-Park/genpark-conversational-barge-in-interruption-arbitrator-skill/releases/tag/v1.0.1) and install with an MCPB-compatible client. Python must be installed and available as `python`.

Alternatively clone this repository and configure an MCP stdio server with command `python` and arguments containing the absolute path to `mcp_server.py`.

[Smithery listing](https://smithery.ai/servers/krispang1020/genpark-barge-in)

## Tools

- `classify_utterance_intent`
- `evaluate_interruption_event`
- `compute_playback_rollback_state`
- `run_benchmark_barge_in_arbitration`

Run `python -m unittest discover -s tests` for regression checks. The official MCP SDK integration check uses the development dependency `mcp`: `python tests/check_mcp.py`.

## Limitations

These are deterministic helpers operating on supplied structured data, not machine-learning models. Input and output remain in the local process. No hosted endpoint, automatic file access or network access is required. State lasts only for the current process. Benchmark tools run synthetic examples in isolated state; their status is not a production-quality certification.

Echo scores are caller-supplied and incoming_audio_energy_db is currently informational. Confidence values are fixed heuristic weights, not calibrated probabilities. Playback rollback estimates whole-word text by character ratio, not actual audio alignment.
