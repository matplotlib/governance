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


## API Leader

A good API is essential for usability and user satisfaction. We strive for an
API that is intuitive, easy to use, consistent and stable. The API Leader (AL)
is responsible for the overall evolution of the API. In particular they ensure
that:

- additions are justified, i.e. they do not duplicate existing functionality
  and do not exceed the intended scope of the library
- additions are consistent with the existing API
- additions are designed to not cause any future liabilities, i.e. they do not
  unintendedly limit future extensions or expose internals
- changes are carefully balanced between their benefit for future users and
  their impact on existing code
- changes follow the deprecation policy so that they do not hit users
  unprepeared


## Principal Engineer

Matplotlib relies on a wide and deep code base to implement its public
API; the low-level details need to be correct to faithfully implement
that API.  In contrast to the API Leader, who is
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
