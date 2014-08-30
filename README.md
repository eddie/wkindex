# WaniKani Add-on Project

Those of you who use userscripts and extensions for [WaniKani](https://wanikani.com) probably are already aware of the state of the ecosystem. This project aims to solve that, and provide an index of all userscripts/browser extensions and apps so that they can be used openly in projects.

# Goals 目標

- Provide an up to date index of WK add-ons.
- Provide a mirror for latest version of these scripts (userscripts only, with permission).
- Provide the data in a universal format for easy access.
- Make contributing easy, more help = better quality index.
- Contain information on userscripts, apps and browser extensions.

# Getting involved

All contributions are massively appreciated, 5 minutes of your time will help create a better WK add-on ecosystem.. The majority of the work will be in gathering the initial data, automated or not.  

Please submit a pull request, or if you are unable to do this,  post the required data in the WK forum thread or as an issue on this project.

# Schema

```
{

  "name": "",
  "latestVersion": "",
  "lastUpdate": "YYYY-MM-DD",
  "author": "",
  "type": "website, app, userscript",
  "platform": {},
  "supported": "updates, full, none",
  "status": "working, unsupported",
  "license": "",
  "threadUrl": "",
  "sourceUrl": "",
  "homepage": "",
  "screenshotUrl": "",
  "description": ""
}
```

## Platform

Platform should be specified in the format shown below:

```

"platform": {
  "browser": "*"
}

```

The above example shows an add-on which is supported in all major browsers.
If the add-on is only supported in Chrome version 30+ and Firefox version 31+ it might look something like this:

```

"platform": {
  "chrome": ">=30.0",
  "firefox": ">=31.0"
}

```

Available platforms values include Firefox, chrome, safari, android, OSX, windows. 
If a platform is missing, it is assumed that there is no support for that platform.

# Naming Conventions

When adding an add-on, please keep the following in mind:

- Lowercase filename. 
- Shorten wanikani to wk. e.g Some-Wanikani-extension.json -> some-wk-extension.json
- License field in the correct format - [Full list](https://spdx.org/licenses/).


# Linting + Utilities

A quick script has been written and needs work, to lint the script files. 
Eventually this tool will also act as a build tool, or as part of a build tool.

In the future, the lint script should be able to identify missing fields or inconsistent 
field data.

Example usage:

`./lint.py --dir=scripts`

```
ERROR:lint:file: duendcat.json error: Expecting , delimiter: line 15 column 391 (char 733)
ERROR:lint:file: override.json error: Invalid control character at: line 15 column 502 (char 1096)
ERROR:lint:file: override.json error: Invalid control character at: line 15 column 502 (char 1096)
ERROR:lint:file: duendcat.json error: Expecting , delimiter: line 15 column 391 (char 733)
```

# Tasks  

- [x] define initial schema for scripts
- [x] lint tool to check for errors in script JSON
- [ ] improve schema for scripts (needs input)
- [ ] a name for the project
- [ ] collect information for all scripts
- [ ] tools to scrape scripts and updates from userscripts
- [ ] store script content for each script (with permission)
- [ ] find a simple solution to contribute (for non-technical folk)
- [ ] decide and add license for project

# Final thoughts

頑張ってください！


