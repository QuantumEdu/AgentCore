No construyas un CLI propio. GSD y Gentle-AI ya resuelven instalación, actualización y TUI.
Usa uv tool run o pipx si necesitas un comando ligero: uv tool run agentcore init --stack nextjs15
Distribuye como GitHub Template + curl | bash para setup. Es suficiente para el 95% de casos.
Delega el workflow a GSD/OpenSpec. AgentCore aporta el contexto validado, ellos el pipeline.