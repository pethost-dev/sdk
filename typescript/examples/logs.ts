import { Pethost } from "pethost";

const pethost = new Pethost({ token: process.env.PETHOST_TOKEN! });

// The newest lines of the project "notes", and where a stream goes on from them without
// missing one.
const newest = await pethost.queryContainerLogs({ projectId: "notes" });
for (const line of newest.lines) console.log(line.service, line.text);

// Each later line as it is written. The loop ends when the stream fails; to stop it sooner,
// leave the loop or abort a signal given as `{ signal }`.
const request = { projectId: "notes", afterCursor: newest.tailCursor };
for await (const { line } of pethost.tailContainerLogs(request)) {
  if (line) console.log(line.service, line.text);
}
