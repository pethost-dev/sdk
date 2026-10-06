import { Pethost, PethostError } from "pethost";

const pethost = new Pethost({ token: process.env.PETHOST_TOKEN! });

// The machine, and every project on it.
const { machine, projects } = await pethost.getMachine();
console.log(machine?.hostname);
for (const project of projects) console.log(project.projectId);

// A deploy to the project "notes": one file written, the others as they are. The call waits a
// while for the deploy to end: the operation's status says whether it did.
try {
  const { operation, project, violations } = await pethost.deployProject({
    projectId: "notes",
    files: [{ path: "/hello.txt", text: "Hello from the Pethost SDK\n" }],
  });
  for (const violation of violations) console.log(`${violation.location}: ${violation.violationMessage}`);
  if (operation) console.log(operation.status);
  if (project) console.log(project.url);
} catch (error) {
  if (!(error instanceof PethostError)) throw error;
  if (error.projectBusy) console.log(`busy with ${error.projectBusy.operationId}: try again when it ends`);
  else console.log(`${error.code}: ${error.message}`);
}
