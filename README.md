Github-Travis CI build for Python
-----------------------------------

This is an example of a Github project for Python. The build is done on Travis, travis-ci.org. Builds are executed
on every commit. If a commit has a tag the build of the artifact will be uploaded as a release on Github for the 
project.

A tag must have the format of `relase-X.Y.Z` where X.Y.Z should follow valid semantic version specification.

To use Travis you should log in to Travis with your Github account, oauth.

To generate the correct API key for Travis to use when uploading an API key is created by Travis in Github in your 
personal account.

You must use the Travis cli for this process. Follow the instructions in https://github.com/travis-ci/travis.rb.

This is done by running standing in the check out project directory.
Make sure you first make a copy of the .travis.yml file in this project since the below command will overwrite the
release section of it. 
This creates a new github encrypted key. Use your Github username/password when running below.  

	$ travis setup releases -f 
	
> You can NOT use a pre created API token!

This will create a new personal token in "Developer settings"->"Personal access tokens" with name like 
`automatic releases for opsdis/sample_workflow — public_repo`

 
 
