import { GetMachineResponse, Pethost } from "pethost";

const pethost = new Pethost({ token: process.env.PETHOST_TOKEN! });

// The machine and its projects as the API's own JSON: `apps_domain`, not `appsDomain`.
const json = GetMachineResponse.toJson(await pethost.getMachine());
const text = JSON.stringify(json, null, 2);
console.log(text);

// And back: the message again, typed as the call answered it.
const { machine } = GetMachineResponse.fromJson(JSON.parse(text));
console.log(machine?.appsDomain);
