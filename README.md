Testing Travis build

Must run 

	travis setup releases -f 

to create a new github encrypted key. Must use basic auth username/password of a member of the organisation - not the organisation it self.
Will create a personal token in "Developer settings"->"Personal access tokens" with name like `"automatic releases for opsdis/sample_workflow — public_repo"`
You can NOT create the token your self and share that any more. 
