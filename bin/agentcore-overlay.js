#!/usr/bin/env node

const fs = require('node:fs');
const path = require('node:path');
const readline = require('node:readline');

const PACKAGE_NAME = 'agentcore-overlay';
const ROOT_DIR = path.resolve(__dirname, '..');

const AI_TARGETS = {
  'gentle-ai': {
    label: 'gentle-ai (default)',
    dirs: [
      { src: 'ai', dst: 'ai' },
    ],
    files: [
      { src: 'AGENTS.md', dst: 'AGENTS.md' },
    ],
  },
  opencode: {
    label: 'opencode',
    dirs: [
      { src: 'ai/skills', dst: '.opencode/skills' },
      { src: 'ai/agents', dst: '.opencode/agents' },
      { src: 'ai/context', dst: '.opencode/context' },
      { src: 'ai/templates', dst: '.opencode/templates' },
      { src: 'ai/schemas', dst: '.opencode/schemas' },
      { src: 'ai/governance', dst: '.opencode/governance' },
    ],
    files: [
      { src: 'AGENTS.md', dst: 'AGENTS.md' },
    ],
  },
  'claude-code': {
    label: 'claude-code',
    dirs: [
      { src: 'ai', dst: '.claude/ai' },
    ],
    files: [
      { src: 'AGENTS.md', dst: '.claude/AGENTS.md' },
    ],
  },
  codex: {
    label: 'Amazon Q Developer (codex)',
    dirs: [
      { src: 'ai/governance', dst: '.codex/governance' },
      { src: 'ai/templates', dst: '.codex/templates' },
      { src: 'ai/context', dst: '.codex/context' },
    ],
    files: [
      { src: 'AGENTS.md', dst: '.codex/AGENTS.md' },
    ],
  },
};

function printHelp() {
  console.log(`Usage:
  ${PACKAGE_NAME} init [target-directory] [options]

Scaffolds the reusable AgentCore overlay into a target directory.

Options:
  --ai <tool>  target AI tool (gentle-ai, opencode, claude-code, codex)
  --force      overwrite existing files and directories
  --dry-run    show what would be copied without writing files
  --help       show this help message

Examples:
  ${PACKAGE_NAME} init
  ${PACKAGE_NAME} init my-project --ai opencode
  ${PACKAGE_NAME} init . --force`);
}

function fail(message) {
  console.error(`Error: ${message}`);
  process.exitCode = 1;
}

async function askAI() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise((resolve) => {
    console.log('\nSelect the AI tool to configure:');
    const entries = Object.entries(AI_TARGETS);
    entries.forEach(([key, val], i) => {
      const marker = key === 'gentle-ai' ? ' (default)' : '';
      console.log(`  ${i + 1}. ${val.label}${marker}`);
    });
    rl.question(`\nEnter number [1]: `, (answer) => {
      rl.close();
      const idx = parseInt(answer.trim(), 10);
      if (answer.trim() === '' || idx === 1) return resolve('gentle-ai');
      const keys = Object.keys(AI_TARGETS);
      if (idx >= 1 && idx <= keys.length) return resolve(keys[idx - 1]);
      console.log(`Invalid option, using gentle-ai.`);
      resolve('gentle-ai');
    });
  });
}

function parseArgs(argv) {
  const args = argv.slice(2);

  if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    return { command: 'help' };
  }

  const force = args.includes('--force');
  const dryRun = args.includes('--dry-run');
  const aiIdx = args.indexOf('--ai');
  const ai = aiIdx !== -1 && aiIdx + 1 < args.length ? args[aiIdx + 1] : null;
  const positional = args.filter((arg) => !arg.startsWith('--'));
  const command = positional[0];
  const targetDir = positional[1] || '.';

  return { command, targetDir, force, dryRun, ai };
}

function walkConflicts(sourcePath, destinationPath, conflicts) {
  if (!fs.existsSync(sourcePath)) return;

  if (!fs.existsSync(destinationPath)) return;

  const sourceStat = fs.statSync(sourcePath);
  const destinationStat = fs.statSync(destinationPath);

  if (sourceStat.isDirectory() !== destinationStat.isDirectory()) {
    conflicts.push(destinationPath);
    return;
  }

  if (sourceStat.isFile()) {
    conflicts.push(destinationPath);
    return;
  }

  for (const entry of fs.readdirSync(sourcePath)) {
    walkConflicts(
      path.join(sourcePath, entry),
      path.join(destinationPath, entry),
      conflicts
    );
  }
}

function ensureSafeToCopy(targetRoot, aiTarget, force) {
  if (force) return;

  const conflicts = [];
  const target = AI_TARGETS[aiTarget];

  for (const item of target.dirs) {
    walkConflicts(
      path.join(ROOT_DIR, item.src),
      path.join(targetRoot, item.dst),
      conflicts
    );
  }
  for (const item of target.files) {
    const dstPath = path.join(targetRoot, item.dst);
    if (fs.existsSync(dstPath)) conflicts.push(dstPath);
  }

  if (conflicts.length > 0) {
    const preview = conflicts.slice(0, 10).map((entry) => `  - ${entry}`).join('\n');
    const remainder = conflicts.length > 10 ? `\n  ...and ${conflicts.length - 10} more` : '';
    throw new Error(
      `target contains existing files. Re-run with --force to overwrite.\n${preview}${remainder}`
    );
  }
}

function copyAsset(sourcePath, destinationPath, dryRun) {
  const stat = fs.statSync(sourcePath);

  if (stat.isDirectory()) {
    if (!dryRun) fs.mkdirSync(destinationPath, { recursive: true });
    for (const entry of fs.readdirSync(sourcePath)) {
      copyAsset(path.join(sourcePath, entry), path.join(destinationPath, entry), dryRun);
    }
    return;
  }

  if (!dryRun) {
    fs.mkdirSync(path.dirname(destinationPath), { recursive: true });
    fs.copyFileSync(sourcePath, destinationPath);
  }
}

function runInit(targetDir, force, dryRun, aiTarget) {
  const targetRoot = path.resolve(process.cwd(), targetDir);
  const target = AI_TARGETS[aiTarget];

  ensureSafeToCopy(targetRoot, aiTarget, force);

  console.log(`\n${dryRun ? 'Planned' : 'Scaffolding'} for ${target.label} into ${targetRoot}\n`);

  for (const item of target.dirs) {
    const src = path.join(ROOT_DIR, item.src);
    const dst = path.join(targetRoot, item.dst);
    if (fs.existsSync(src)) {
      console.log(`  ${item.src}/  →  ${item.dst}/`);
      if (!dryRun) copyAsset(src, dst, dryRun);
    }
  }
  for (const item of target.files) {
    const src = path.join(ROOT_DIR, item.src);
    const dst = path.join(targetRoot, item.dst);
    if (fs.existsSync(src)) {
      console.log(`  ${item.src}    →  ${item.dst}`);
      if (!dryRun) copyAsset(src, dst, dryRun);
    }
  }

  const tips = {
    'gentle-ai': 'Next: open AGENTS.md, then ai/README.md.',
    opencode: 'Next: open AGENTS.md. Skills are in .opencode/skills/.',
    'claude-code': 'Next: open .claude/AGENTS.md, then .claude/ai/README.md.',
    codex: 'Next: open .codex/AGENTS.md for instructions.',
  };
  console.log(`\n${tips[aiTarget] || 'Done.'}`);
}

async function main() {
  const parsed = parseArgs(process.argv);

  if (parsed.command === 'help') {
    printHelp();
    return;
  }

  if (parsed.command !== 'init') {
    fail(`unknown command "${parsed.command}". Use --help for usage.`);
    return;
  }

  let aiTarget = parsed.ai;
  if (!aiTarget) {
    aiTarget = await askAI();
  } else if (!AI_TARGETS[aiTarget]) {
    fail(`Unknown AI tool "${aiTarget}". Options: ${Object.keys(AI_TARGETS).join(', ')}`);
    return;
  }

  try {
    runInit(parsed.targetDir, parsed.force, parsed.dryRun, aiTarget);
  } catch (error) {
    fail(error.message);
  }
}

main();
