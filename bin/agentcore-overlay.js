#!/usr/bin/env node

const fs = require('node:fs');
const path = require('node:path');

const PACKAGE_NAME = 'agentcore-overlay';
const ROOT_DIR = path.resolve(__dirname, '..');
const DEFAULT_ASSETS = ['ai', 'AGENTS.md'];

function printHelp() {
  console.log(`Usage:
  ${PACKAGE_NAME} init [target-directory] [--force] [--dry-run]
  ${PACKAGE_NAME} --help

Scaffolds the reusable AgentCore overlay into a target directory.

What gets copied:
  - ai/       portable governance, skills, templates, and context
  - AGENTS.md repo entrypoint that points readers into /ai

Why not copy the other root docs:
  - README.md, FAQ.md, and CHANGELOG.md stay in the source repo/package as reference docs.
  - Keeping the scaffold small reduces noise inside the target project.

Options:
  --force    overwrite existing files and directories
  --dry-run  show what would be copied without writing files
  --help     show this help message

Examples:
  npx ${PACKAGE_NAME} init
  npx ${PACKAGE_NAME} init my-project
  ${PACKAGE_NAME} init . --force`);
}

function fail(message) {
  console.error(`Error: ${message}`);
  process.exitCode = 1;
}

function parseArgs(argv) {
  const args = argv.slice(2);

  if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    return { command: 'help' };
  }

  const force = args.includes('--force');
  const dryRun = args.includes('--dry-run');
  const positional = args.filter((arg) => !arg.startsWith('--'));
  const command = positional[0];
  const targetDir = positional[1] || '.';

  return { command, targetDir, force, dryRun };
}

function walkConflicts(sourcePath, destinationPath, conflicts) {
  if (!fs.existsSync(destinationPath)) {
    return;
  }

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

function ensureSafeToCopy(targetRoot, force) {
  if (force) {
    return;
  }

  const conflicts = [];

  for (const asset of DEFAULT_ASSETS) {
    walkConflicts(
      path.join(ROOT_DIR, asset),
      path.join(targetRoot, asset),
      conflicts
    );
  }

  if (conflicts.length > 0) {
    const preview = conflicts.slice(0, 10).map((entry) => `  - ${entry}`).join('\n');
    const remainder = conflicts.length > 10 ? `\n  ...and ${conflicts.length - 10} more` : '';
    throw new Error(
      `target contains existing files. Re-run with --force to overwrite.\n${preview}${remainder}`
    );
  }
}

function copyAsset(sourcePath, destinationPath) {
  const stat = fs.statSync(sourcePath);

  if (stat.isDirectory()) {
    fs.mkdirSync(destinationPath, { recursive: true });
    for (const entry of fs.readdirSync(sourcePath)) {
      copyAsset(path.join(sourcePath, entry), path.join(destinationPath, entry));
    }
    return;
  }

  fs.mkdirSync(path.dirname(destinationPath), { recursive: true });
  fs.copyFileSync(sourcePath, destinationPath);
}

function runInit(targetDir, force, dryRun) {
  const targetRoot = path.resolve(process.cwd(), targetDir);
  ensureSafeToCopy(targetRoot, force);

  console.log(`${dryRun ? 'Planned' : 'Scaffolding'} overlay into ${targetRoot}`);

  for (const asset of DEFAULT_ASSETS) {
    const sourcePath = path.join(ROOT_DIR, asset);
    const destinationPath = path.join(targetRoot, asset);
    console.log(`- ${asset}`);

    if (!dryRun) {
      copyAsset(sourcePath, destinationPath);
    }
  }

  console.log('Next: open AGENTS.md, then ai/README.md.');
}

function main() {
  const parsed = parseArgs(process.argv);

  if (parsed.command === 'help') {
    printHelp();
    return;
  }

  if (parsed.command !== 'init') {
    fail(`unknown command \"${parsed.command}\". Use --help for usage.`);
    return;
  }

  try {
    runInit(parsed.targetDir, parsed.force, parsed.dryRun);
  } catch (error) {
    fail(error.message);
  }
}

main();
