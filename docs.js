const widdershins = require('widdershins');
const options = {
  clipboard: true,
  customApiKeyValue: 'APITOKEN',
  expandBody: false,
  headings: 2,
  omitBody: false,
  resolve: false,
  codeSamples: true,
  shallowSchemas: false,
  sample: true,
  httpsnippet: true,
  discovery: false,
  language_tabs: [{ shell: 'Shell' }],
};
const fs = require('fs');
const fileData = fs.readFileSync('openapi.yaml', 'utf8');
const yaml = require('yaml');
const swaggerFile = yaml.parse(fileData);

widdershins
  .convert(swaggerFile, options)
  .then((markdownOutput) => {
    // markdownOutput contains the converted markdown
    fs.writeFileSync('myOutput.md', markdownOutput, 'utf8');
  })
  .catch((err) => {
    // handle errors
    console.log(err);
  });
