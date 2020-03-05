# Contributor Roadmap/Expectations
Hello, thank you for your interest in contributing to Matplotlib!

Matplotlib is primarily administered via github, so more information
on the exact permissions granted to each role is available at [github
help](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#repository-access-for-each-permission-level)




# Development
Responsible for the codebase (including documentation)

* https://github.com/orgs/matplotlib/teams/developers


**contribute**: https://matplotlib.org/devdocs/devel/index.html

**triage:**
- triaging issues and pull requests means:
    - assigning labels, milestones, and reviewers
    - closing and reopening as needed
    - marking duplicates
- get triage privileges: granted on 1st merged pull request
    - (We need to write the script for this, run as a service on heroku’s free tier?  can we do this with actions?)

**Get commit privileges:**
Significant or sustained merged pull requests
- including domain expertise as needed

**Lose Commit privileges:**
- no activity on the repository/calls/discourse/mailing lists in 6 months
- repeated or severe violations of [merge guidelines](https://matplotlib.org/devdocs/devel/coding_guide.html)
- potential repercussion of a [Code of Conduct](https://www.python.org/psf/conduct/) violation

# Release Powers
- has publish permissions to pypi
- has push access to macpython build system
- Who has this
    - Lead developer, steering council, release manager
- responsibilities
    - run release process

# Community / communications

Engages in community building, support, and outreach

* https://github.com/orgs/matplotlib/teams/community

## Blog
writes and reviews blog posts about all things Matplotlib and made with Matplotlib
* https://github.com/orgs/matplotlib/teams/blog
* https://github.com/matplotlib/matplotblog

**contribute**:
* https://matplotlib.org/matplotblog/posts/how-to-contribute/

**get commit privileges:**
* sustained constructive reviews of contributed blog posts
* at discretion of [communications lead](named_project_roles.md)

**lose commit privileges:**
- repeated or severe violations of communications and social media guidelines
- potential repercussion of a [Code of Conduct](https://www.python.org/psf/conduct/) violation
-  at discretion of [communications lead](named_project_roles.md)

## Teaching
Develops talks and tutorials to illustrated using and developing applications with Matplotlib

* https://github.com/orgs/matplotlib/teams/teaching

**contribute:**

- significant or sustained contributions to:
    - https://github.com/matplotlib/presentations
    - https://discourse.matplotlib.org/c/showcase/tutorial
- significant or sustained body of opens source teaching materials:
    - book, long running blog series

**content guidelines:**

-  [Social Media Guidelines](communications_guidelines.md)
- [Code of Conduct](https://www.python.org/psf/conduct/)

**removal from team:**
- repeated or severe violations of [Social Media Guidelines](communications_guidelines.md)
- potential repercussion of a [Code of Conduct](https://www.python.org/psf/conduct/) violation
-  at discretion of [communications or teaching lead](named_project_roles.md)

## Discourse
https://discourse.matplotlib.org/


 Foster engagement on the discourse

**contribute:**
* participate in discussion on https://discourse.matplotlib.org/

**increasing trust level to access more privileges:**

- https://blog.discourse.org/2018/06/understanding-discourse-trust-levels/
- sustained constructive participation in discussions

**get suspended or banned:**
- repeated or severe violations of [discourse guidelines](https://discourse.matplotlib.org/faq)
- potential repercussion of a [Code of Conduct](https://www.python.org/psf/conduct/) violation

## Instagram
instagram.com/matplotart/

Curate a gallery of data and scientific visualization art made using Matplotlib

**contribute:**  DM, tag #matplotlib, submit at http://bit.ly/matplotart

**curate the account:**

- sustained positive contributions to Instagram
- sustained positive contributions to https://discourse.matplotlib.org/c/showcase
- sustained positive tagging of matplotlib content on twitter

**revoke curation privileges:**

- repeated or severe violations of [Social Media Guidelines](communications_guidelines.md)
- potential repercussion of a [Code of Conduct](https://www.python.org/psf/conduct/) violation
-  at discretion of [communications lead](named_project_roles.md)

## Twitter
https://twitter.com/matplotlib

Signal boost what’s new with the library & 3rd party packages, promote new work built on Matplotlib, and engage with the community.

**contribute:** tweet @matplotlib or tag #matplotlib

**tweet as twitter account:**
- be a lead on at least one of the other community projects

**revoke twitter access:**

- repeated or severe violations of [+Social Media Guidelines](https://paper.dropbox.com/doc/Social-Media-Guidelines-GMgkvuznnxwtZpwFvPogS)
- potential repercussion of a [Code of Conduct](https://www.python.org/psf/conduct/) violation
-  at discretion of [communications lead](named_project_roles.md)

# Github

* https://github.com/matplotlib/matplotlib

## Github Organization ownership
Full control of everything on GH
**People:**
- Lead developer, steering council


Want to keep this set small enough that we don’t have too much
unneeded attack surface area, but big enough that we don’t have single
point of failure.

## Administration permissions

Manages the administration of the Matplotlib github repositories.

* https://github.com/orgs/matplotlib/teams/admin

- Made up of steering council members, appointment process discussed here:
    - https://github.com/matplotlib/governance/blob/master/governance.md#steering-council
    - should decouple SC and admin power going forward

**Responsibilities:**
- add new repositories and teams to the matplotlib org
- add members to Matplotlib teams
- can delete / moderate issues

- on a GH team that has “Admin” level permissions on all repositories
