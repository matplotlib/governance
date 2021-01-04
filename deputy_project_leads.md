# Deputy Project Leaders


## Release Manager(s)

The Release Manager (RM) is appointed for a minor version (A.B.x) release series
of Matplotlib rather than for a fixed term.  They are responsible for the full
release life cycle of all minor releases in the series including:

- ensuring the whats new, API changes, and release notes are up to date
- the timing of the releases
- what changes should or should not be backported from the master
  branch
- rebuilding and publishing the website
- publishing sdist and wheels to pypi
- notifying down-stream packagers of the release
- announcing the release (in coordination with the Community Manager)

An individual may be the RM for more than one release series at the
same time.


## API Consistency Leader

Matplotlib is constantly making small changes to its API: enhancements
that add new features, bug fixes that unavoidably change behavior, and
deprecation of inconsistent or undesired functionality.  The API
Consistency Leader (ACL) is responsible for making sure that these
incremental changes to the library are done in a coherent and
consistent manner.

This include checking that:

- new functionality is not duplicating existing functionality
- deprecations are justified and properly documented
- new functionality does not "paint us into a corner" for future work
- new functionality is implemented with an API that is consistent with
  the existing functions


## Principal Engineer

Matplotlib relies on a wide and deep code base to implement its public
API; the low-level details need to be correct to faithfully implement
that API.  In contrast to the API Consistency Leader, who is
responsible for what the library does, the Principal Engineer is
responsible for how. They are the point of contact for:

- rendering
- file formats
- text/font handling
- integration with GUI toolkits
- internal data structures and API

## Reference Documentation Leader

The Matplotlib API reference documentation is split between the docstrings and
the rst source.  This documentation needs to be complete and accurate as our
users rely on it as the final authority of what a given method will do (short of
reading the source).

The Reference Documentation Leader (RDL) is responsible for ensuring that
the docstrings are:

- correctly formatted and render as intended
- technically correct
- complete

In addition to the docstrings the RDL is responsible for the sphinx build
machinery and our sphinx extensions.

## Narrative Documentation Leader

In addition to the reference documentation, Matplotlib has narrative documentation.
This documentation can take the form of short "cookbook" examples, longer tutorials,
and prose documenting the how and why of the internals of the library.  This includes
content that lives in both the main repository and  in other repositories
in the Matplotlib organization.

The Narrative Documentation Leader is responsible for shepherding all of this
content including the scope, organization, level, tone, and voice.

## Secretary

- Responsible for ensuring that there is an agenda for the weekly
  meeting at it is followed.
- Responsible for maintaining the weekly notes.


## Community Manager

The true strength of Matplotlib and why it has had such longevity as a
project is the community of people around the code.  That community
needs to be maintained.  The Community Manager (CM) is a catch-all
position for several very diverse tasks and this role may be split in
the future and may want to enlist further assistants.  The CM is responsible
for Matplotlib's evangelism, outreach, and user support as well as mainitaining
the venues for conversation with the community.
