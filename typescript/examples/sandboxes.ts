import { Sandboxes } from "pethost/sandboxes";

const sandboxes = new Sandboxes({ token: process.env.PETHOST_TOKEN! });
const { sandboxId } = await sandboxes.createSandbox({ template: "base" });
await sandboxes.writeFiles({ sandboxId, changes: [{ path: "hello.py", text: "print(6 * 7)" }] });
const command = await sandboxes.runCommand({ sandboxId, command: "python3 hello.py" });
console.log(command.exitCode, command.stdout); // 0 "42\n"
const turn = await sandboxes.promptAgent({ sandboxId, prompt: "Add a test for hello.py" });
console.log(turn.state, turn.reply);
await sandboxes.pauseSandbox({ sandboxId });
