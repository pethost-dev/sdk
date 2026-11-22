// The checks of every surface of the package, which each test file adds to through its harness
// and run.ts runs: one list, so that one run says how many of all failed.
const checks: { name: string; run: () => Promise<void> }[] = [];

export function check(name: string, run: () => Promise<void>): void {
  checks.push({ name, run });
}

/** Runs every check and says which failed; the process then exits with 1. */
export async function runChecks(): Promise<void> {
  const failures: string[] = [];
  for (const { name, run } of checks) {
    try {
      await run();
    } catch (error) {
      failures.push(`${name}\n  ${error instanceof Error ? error.message.replaceAll("\n", "\n  ") : String(error)}`);
    }
  }

  if (failures.length > 0) {
    console.error(`${failures.join("\n\n")}\n\n${failures.length} of ${checks.length} checks failed`);
    process.exit(1);
  }
  console.log(`ok: ${checks.length} checks`);
}
