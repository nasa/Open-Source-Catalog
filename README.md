# Open-Source-Catalog

[![Build Status](https://travis-ci.org/nasa/Open-Source-Catalog.svg?branch=master)](https://travis-ci.org/nasa/Open-Source-Catalog)

## About

This GitHub repository is maintained by the [NASA OCIO Open Innovation Team](http://open.nasa.gov/about/) and contains a catalog of publicly available NASA open source projects that are published on [code.nasa.gov](http://code.nasa.gov). The catalog is persisted as a JSON file ```catalog.json``` and contains an array of projects.  As Code Sharing at NASA is a community effort, we encourage NASA developers to add a meta-record in to this catalog to publish their open source projects on [code.nasa.gov](http://code.nasa.gov/).

## Requirements
* Open Source software project approved for open source release by your [NASA Field Center SRA](http://code.nasa.gov/#/guide)
* Code Project hosted in a code repository (preferably GitHub.com) and visible to Internet Users
* Meta record of your software project; instantiate ```required_fields_project_template.json```

## Add your project

* Create a project meta-record using the template from file required_fields_project_template.json:
  * Note that Category labels longer than 24 characters will be truncated.
```
{
    "NASA Center": "Ames Research Center",
    "Contributors": [
      "jasonduley"
    ],
    "Software": "My Software Project",
    "External Link": "https://github.com/nasa/my-software-project/wiki",
    "Public Code Repo": "https://github.com/nasa/my-software-project",
    "Description": "This is a description of the software project.",
    "License": [
      "NASA Open Source"
    ],
    "Categories": [
      "Framework",
      "Toolkit",
      "Web"
    ],
    "Update_Date": "2014-09-23",
    "Labor_Hours": 24
}
```

* Add your instantiated meta-record to the array in the catalog.json file via a pull request
* Once the merge is complete, your project will be published on [code.nasa.gov](http://code.nasa.gov/)

## Thanks
Special thanks goes out to [Chris Mattmann (NASA JPL)](https://github.com/chrismattmann), Sean Kelly (NASA JPL) and [Eric Whyne (DARPA)](https://github.com/ericwhyne) for their inspiration for this effort.
appended text
appended text
NEW
dfadsfadsf
dfadsfadsf
11232312312
