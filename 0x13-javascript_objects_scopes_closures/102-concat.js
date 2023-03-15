#!/usr/bin/node

const fs = require('fs');
const fFileArg = fs.readFileSync(process.argv[2]).toString();
const sFileArg = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], fFileArg + sFileArg);
