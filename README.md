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
  "latest_version": "",
  "last_update": "YYYY-MM-DD",
  "author": "",
  "type": "website, app, userscript",
  "supported": "updates, full, none",
  "status": "working, unsupported",
  "license": "",
  "thread_url": "",
  "source_url": "",
  "homepage": "",
  "screenshot_url": "",
  "description": ""
}
```


# Naming Conventions

When adding an add-on, please keep the following in mind:

- Lowercase filename. 
- Shorten wanikani to wk. e.g Some-Wanikani-extension.json -> some-wk-extension.json

# Tasks  
- [x] define initial schema for scripts
- [ ] improve schema for scripts (needs input)
- [ ] a name for the project
- [ ] collect information for all scripts
- [ ] tools to scrape scripts and updates from userscripts
- [ ] store script content for each script (with permission)
- [ ] find a simple solution to contribute (for non-technical folk)
- [ ] decide and add license for project

# Final thoughts

頑張ってください！


