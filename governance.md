# Main Governance Document

The official version of this document, along with a list of
individuals and institutions in the roles defined in the governance
section below, is contained in The Project Governance Repository at:

[https://github.com/matplotlib/governance](https://github.com/matplotlib/governance)

The Project
===========

The Matplotlib Project (The Project) is an open source software
project affiliated with the [NumFOCUS](https://numfocus.org)
Foundation. The goal of The Project is to develop open source software
and deploy open and public websites and services for data
visualization. The Software developed by The Project is released under
the BSD (or similar permissive) open source license, developed openly
and hosted in public GitHub repositories under the
[Matplotlib GitHub organization](https://github.com/matplotlib). Examples
of Project Software include the matplotlib library for data
visualization and its associated extensions and dependencies.  The
Services run by the Project consist of public websites and
web-services that are hosted under the matplotlib.org domain.

The Project is developed by a team of distributed developers, called
Contributors. Contributors are individuals who have contributed code,
documentation, designs or other work to one or more Project
repositories.  Contributors are also known by the name "Matplotlib
Development Team (MDT)" in the project license.  Anyone can be a
Contributor. Contributors can be affiliated with any legal entity or
none. Contributors participate in the project by submitting, reviewing
and discussing GitHub Pull Requests and Issues and participating in
open and public Project discussions on GitHub, discourse, Hackpad,
Gitter chat rooms and mailing lists. The foundation of Project
participation is openness and transparency.

For example, here is a partial list of the current Contributors to the
main Matplotlib repository:

[https://github.com/matplotlib/matplotlib/graphs/contributors](https://github.com/matplotlib/matplotlib/graphs/contributors)

There are also many other Contributors listed in the logs of other
repositories of the project.  This also notably does not include
contributions of items other than code, such as reporting and
commenting on issues, so is only a subset of the individuals
considered to be Contributors.

The Project Community consists of all Contributors and Users of the Project.
Contributors work on behalf of and are responsible to the larger Project
Community and we strive to keep the barrier between Contributors and Users as
low as possible.

The Project is formally affiliated with the NumFOCUS Foundation
([http://numfocus.org](http://numfocus.org)), a non-profit
organization covered by section 501(c)(3) of the United States
Internal Revenue Service code.  NumFOCUS serves as its fiscal sponsor,
may hold project trademarks and other intellectual property, helps
manage project donations and acts as a parent legal entity. NumFOCUS
is the only legal entity that has a formal relationship with the
project (see Institutional Partners section below).

Governance
==========

This section describes the governance and leadership model of The Project.

The foundations of Project governance are:

-   Openness & Transparency
-   Active Contribution
-   Institutional Neutrality

Project leadership was initially provided by the original author, John
D. Hunter.  Shortly before his passing in 2012, leadership was
transferred to Michael Droettboom, who later invited Thomas Caswell as
a co-lead.  Additional leadership has also been provided by a subset
of Contributors, called Developers, whose active and consistent
contributions have been recognized by their receiving “commit rights”
to the Project repositories. In general all Project decisions are made
through consensus among the Developers with input from the
Community.

While this approach has served us well, as the Project grows and faces
more legal and financial decisions and interacts with other
institutions, we see a need for a more formal governance model. Moving
forward, the Project leadership will consist of a Lead Developer,
several Deputy Leads, and a Steering Council. We view this governance
model as the formalization of what we are already doing, rather than a
change in direction.

Lead developer
--------------

The Project will have a Lead Developer (LD), who is currently Thomas A Caswell.
The LD has the authority to make all final decisions for The Project.  In
practice the LD chooses to defer that authority to the consensus of the
community discussion channels and the Steering Council (see below).  It is
expected, and in the past has been the case, that the LD will only rarely assert
their final authority.  Because rarely used, we refer to LD’s final authority as
a “special” or “overriding” vote.  When it does occur, the LD override typically
happens in situations where there is a deadlock in the Steering Council or if
the Steering Council asks the LD to make a decision on a specific matter.

The LD is chair of the Steering Council (see below) and may delegate their
authority on a particular decision or set of decisions to any other Council
member at their discretion.

The LD can appoint their successor, but it is expected that the Steering Council
would be consulted on this decision. If the LD is unable to appoint a successor,
the Steering Council will make a suggestion or suggestions to the Main NumFOCUS
Board. While the Steering Council and Main NumFOCUS Board will work together
closely on the LD selection process, the Main NumFOCUS Board will make the final
decision.

To ensure the benevolence of the LD, The Project encourages others to fork the
project if they disagree with the overall direction the LD is taking.

Steering Council
----------------

The Project will have a Steering Council that consists of Project Contributors
who have produced contributions that are substantial in quality and quantity,
and sustained over at least one year. The overall role of the Council is to
ensure, through working with the LD and taking input from the Community, the
long-term well-being of the project, technically, financially, and as a
community.

During the everyday project activities, council members participate in all
discussions, code review and other project activities as peers with all other
Contributors and the Community. In these everyday activities, Council Members do
not have any special power or privilege through their membership on the
Council. However, it is expected that because of the quality and quantity of
their contributions and their expert knowledge of the Project Software and
Services that Council Members will provide useful guidance, both technical and
in terms of project direction, to potentially less experienced contributors.

The Steering Council and its Members play a special role in certain
situations. In particular, the Council may:

- Develop funding sources and spending money (see Finance sub committee below).
- Make decisions about the overall scope, vision and direction of the project.
- Make decisions about strategic collaborations with other organizations or
  individuals.
- Make decisions about the Services that are run by The Project and manage those
  Services for the benefit of the Project and Community.
- Make decisions when regular community discussion doesn’t produce consensus on
  an issue in a reasonable time frame.
- Granting or revoking commit rights.

The steering council will be between 5 and 7 people including the LD.  Being on
the steering council is a responsibilty, not a recongnition of being a long-time
contributor.


### Council membership

To become eligible for being a Steering Council Member an individual must be a
Project Contributor who has produced contributions that are substantial in
quality and quantity, and sustained over at least one year.  Potential Council
Members are nominated by existing Council members and voted upon by the existing
Council after asking if the potential Member is interested and willing to serve
in that capacity.  The Council will be initially formed through LD nomination
from the set of existing Developers who meet the above criteria.

When considering potential Members, the Council will look at candidates with a
comprehensive view of their contributions.  This will include but is not limited
to code, code review, infrastructure work, mailing list and chat participation,
community help/building, education and outreach, design work, etc.  We are
deliberately not setting arbitrary quantitative metrics (like “100 commits in
this repo”) to avoid encouraging behavior that plays to the metrics rather than
the project’s overall well-being.  We want to encourage a diverse array of
backgrounds, viewpoints and talents in our team, which is why we explicitly do
not define code as the sole metric on which council membership will be
evaluated.

When invited to join the Steering Council Contributors are commiting to serve
for 2 years.  At the end of the two years they may elect to, with consent of the
rest of the council, re-join the council.  If they chose to not re-join the
council the process above is used to recruit new members.

The Steering Council members, other than the LD, will serve in 2 equal classes
whose terms are offset by 1 year.  This will help preserve the continuity on the
Steering Council over time.

A Steering Council member can step down at anytime.  If a Council Member becomes
inactive for a period of 2 months, they will be approached by the LD to see if
they plan on returning to active participation.  If not they will be asked to
step down, if the Council Member indicates they intend to be active again but
have not done so after 1 month the Council my vote to remove them.

If a Council Member leaves the council early they may be replaced, using the
same process as above.  Their replacement will join the same class and serve the
remainder of the 2 years.

Each class can fluctuate between 2 and 3 members so long as the total council
size (including the LD) is between 5 and 7.  If a class gets too small, an
additional member must be recruited.

All former Council members can be considered for membership again at any time in
the future, like any other Project Contributor. Retired Council members will be
listed on the project website, acknowledging the period during which they were
active in the Council.

The Council reserves the right to eject current Members, other than the LD, if
they are deemed to be actively harmful to the project’s well-being, and attempts
at communication and conflict resolution have failed.

### Conflict of interest

It is expected that the LD, DLDs, and Council Members will be employed at a wide
range of companies, universities and non-profit organizations. Because of this,
it is possible that Members will have conflict of interests. Such conflict of
interests include, but are not limited to:

-   Financial interests, such as investments, employment or contracting work,
    outside of The Project that may influence their work on The Project.
-   Access to proprietary information of their employer that could potentially
    leak into their work with the Project.

All members of the Council, LD included, shall disclose to the rest of the
Council any conflict of interest they may have. Members with a conflict of
interest in a particular issue may participate in Council discussions on that
issue, but must recuse themselves from voting on the issue. If the LD has
recused themselves for a particular decision, they will appoint a substitute
LD for that decision.

### Private communications of the Council

Unless specifically required, all Council discussions and activities will be
public and done in collaboration and discussion with the Project Contributors
and Community through the normal communication channels. The Council will have a
private mailing list that will be used sparingly and only when a specific matter
requires privacy. When private communications and decisions are needed, the
Council will do its best to summarize those to the Community after eliding
personal/private/sensitive information that should not be posted to the public
internet.

### Subcommittees

The Council can create subcommittees that provide leadership and guidance for
specific aspects of the project. Like the Council as a whole, subcommittees
should conduct their business in an open and public manner unless privacy is
specifically called for. Private subcommittee communications should happen on
the main private mailing list of the Council unless specifically called for.

### NumFOCUS Subcommittee

The Council will maintain one narrowly focused subcommittee to manage its
interactions with NumFOCUS.

-   The NumFOCUS Subcommittee is comprised of 4 persons who manage project
    funding that comes through NumFOCUS. It is expected that these funds will
    be spent in a manner that is consistent with the non-profit mission of
    NumFOCUS and the direction of the Project as determined by the full
    Council.
-   This Subcommittee shall NOT make decisions about the direction, scope or
    technical direction of the Project.
-   This Subcommittee will have 4 members, at least 2 of whom are
    also on the Steering Council and 1 of whom will be external to the
    Steering Council. No Subcommitee Member can report to the same
    person as any other member of the Subcommittee through employment
    or contracting work (including the reportee, i.e. the reportee + 1
    is the max). This avoids effective majorities resting on one
    person.


Institutional Partners and Funding
==================================

The LD and Steering Council are the primary leadership for the project. No
outside institution, individual or legal entity has the ability to own,
control, usurp or influence the project other than by participating in the
Project as Contributors and Council Members. However, because institutions are
the primary funding mechanism for the project, it is important to formally
acknowledge institutional participation in the project. These are Institutional
Partners.

An Institutional Contributor is any individual Project Contributor who
contributes to the project as part of their official duties at an Institutional
Partner. Likewise, an Institutional Council Member is any Project Steering
Council Member who contributes to the project as part of their official duties
at an Institutional Partner.

With these definitions, an Institutional Partner is any recognized legal entity
in the United States or elsewhere that employs at least one Institutional
Contributor or Institutional Council Member. Institutional Partners can be
for-profit or non-profit entities.

Institutions become eligible to become an Institutional Partner by employing
individuals who actively contribute to The Project as part of their official
duties. To state this another way, the only way for an Institutional Partner to
influence the project is by actively contributing to the open development of the
project, on equal terms with any other member of the community of Contributors
and Council Members. Merely using Matplotlib Software in an institutional
context does not allow an entity to become an Institutional Partner. Financial
gifts do not enable an entity to become an Institutional Partner. Once an
institution becomes eligible for Institutional Partnership, the Steering Council
must nominate and approve the Partnership.

If an existing Institutional Partner no longer has a contributing employee,
they will be given a one-year grace period for other employees to begin
contributing.

An Institutional Partner is free to pursue funding for their work on The
Project through any legal means. This could involve a non-profit organization
raising money from private foundations and donors or a for-profit company
building proprietary products and services that leverage Project Software and
Services. Funding acquired by Institutional Partners to work on The Project is
called Institutional Funding. However, no funding obtained by an Institutional
Partner can override The Project LD and Steering Council. If a Partner has
funding to do Matplotlib work and the Council decides to not pursue that
work as a project, the Partner is free to pursue it on their own. However in
this situation, that part of the Partner’s work will not be under the
Matplotlib umbrella and cannot use the Project trademarks in a way that
suggests a formal relationship.

To acknowledge institutional contributions, Institutional Partners receive the
following benefits:

-   Acknowledged on the Matplotlib websites, in talks and T-shirts.
-   Ability to acknowledge their own funding sources on the Matplotlib websites,
    in talks and T-shirts.


Changing the Governance Documents
=================================

Changes to the governance documents are submitted via a GitHub pull
request to The Project's governance documents GitHub repository at
[https://github.com/matplotlib/governance](https://github.com/matplotlib/governance).
The pull request is then refined in response to public comment and
review, with the goal being consensus in the community.  After this
open period, a Steering Council Member proposes to the Steering
Council that the changes be ratified and the pull request merged
(accepting the proposed changes) or proposes that the pull request be
closed without merging (rejecting the proposed changes).  The Member
should state the final commit hash in the pull request being proposed
for acceptance or rejection and briefly summarize the pull request. A
minimum of 80% of the Steering Council must vote and at least 2/3 of
the votes must be positive to carry out the proposed action (fractions
of a vote rounded up to the nearest integer). Since the LD holds
ultimate authority in The Project, the LD has authority to act alone
in accepting or rejecting changes or overriding Steering Council
decisions.
