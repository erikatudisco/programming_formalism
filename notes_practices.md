# Common development practices

## Social coding

> [Social coding](https://github.com/coderefinery/social-coding/blob/main/content/social-coding.md) by [https://coderefinery.org/ CodeRefinery] is licensed under [http://creativecommons.org/licenses/by/4.0/ CC BY 4.0] Minor changes were made to adjust the content to the layout of this page

```{objectives}
- Get an overview of motivations, benefits, but also risks of sharing and reusing code.
- Learn to identify whether you can use other peoples software.
```

### Discussion/questions/poll: basics of sharing

```{instructor-note}
These questions 1-4 below can be used as a starting point and copied to the collaborative
document or form input for an online poll.

Alternatively, they can be discussed in voice or free-form text (discussion box below).
```

```{discussion} Social-1: Think about if and how you share
- Did you ever share your code? If yes, what motivated you? Come up with
  **reasons for sharing** your scripts/code/data.
- Also think about **reasons for not sharing**.
```

````markdown
### Question 1: Why would I want to share my scripts/code/data?

- A: Easier to find and reproduce (scientific reproducibility)
- B: More trustworthy: others can verify correctness and find and report bugs
- C: Enables others to build on top of your code
  (derivative work, provided the license allows it)
- D: Others can submit features/improvements
- E: Others can help fixing bugs
- F: Many tools and apps are free for open source, so no financial cost for this
  (GitHub, GitLab, Appveyor, Read the Docs)
- G: Good for your CV: you can show what you have built
- H: Discourages competitors. If others can't build on your work,
  they will make competing work
- I: When publicly shared, usually we timestamp or set a version,
  so it is easier to refer to a specific version
- J: You can reuse your own code later after change of job or affiliation
- K: It encourages me to code properly from the start

**Choose many**. Vote on Menti.com (code: XYZ)

### Quesion 2: The most concerning thing for me, If I share my software now

-A: It will be scooped (stolen) by someone else
-B: It will expose my "ugly code"
-C: Others may find bugs and mistakes. What if the algorithm is wrong?
-D: I will get too many questions, I do not have time for that
-E: Losing control over the direction of the project
-F: Low quality copies will appear
-G: I won't be able to sell this later. Someone else will make money from it
-H: It is too early, I am just prototyping, I will write version to distribute later
-I: Worried about licensing and legal matters, as they are very complicated

**Choose many**. Vote on Menti.com (code: XYZ)

### Question 3: Why is software often treated differently from papers?

**Free-form answers**. Vote on Menti.com (code: XYZ)

### Question 4: When you find a repository with code/library you would like to reuse, what are the things you look at to decide whether you use it?

**Free-form answers**. Vote on Menti.com (code: XYZ)

### Comparing sharing papers and sharing code

```{figure} https://coderefinery.github.io/social-coding/_images/sharing-papers.jpg
:alt: Image shows that we are motivated sharing our published papers since we get rewarded with academic credit in form of citations

Citation as one form of academic credit to motivate sharing papers.
```

Sharing papers and academic credit:

- The goal is maximum visibility and maximum reuse.
- The more interesting science is done referencing my paper, the better for me.
- Nobody actively tries to limit the reach of their papers.

```{figure} https://coderefinery.github.io/social-coding/_images/sharing-code.jpg
:alt: Getting improvements back and also getting citations can motivate us to share code

Different ways we can benefit from sharing code.
```

Sharing code:

- "I did all the ground work and they get to do the interesting science?"
- Sharing code and encouraging _derivative work_ may boost your academic impact.
- But will your work be visible if it is used two levels deep down?

### Journal policies as motivation for sharing

From [Science editorial policy](https://www.sciencemag.org/authors/science-journals-editorial-policies):

> "We require that **all computer code used for modeling and/or data analysis**
> that is not commercially available be deposited in a **publicly accessible repository**
> upon publication. In rare exceptional cases where security
> concerns or competing commercial interests pose a conflict, code-sharing
> arrangements that still facilitate reproduction of the work should be
> discussed with your Editor no later than the revision stage."

From [Nature editorial policy](https://www.nature.com/authors/policies/availability.html):

> "An inherent principle of publication is that others should be able to
> replicate and build upon the authors' published claims. A condition of
> publication in a Nature Research journal is that authors are required to make
> **materials, data, code, and associated protocols promptly available** to readers
> without undue qualifications. Any restrictions on the availability of
> materials or information must be disclosed to the editors at the time of
> submission. Any restrictions must also be disclosed in the submitted
> manuscript."

However [a study](https://www.pnas.org/content/115/11/2584) showed that despite
these policies, many people still do not share their code 😞. This paper
includes samples of charming author responses such as:

> "When you approach a PI for the source codes and raw data, you better explain
> who you are, whom you work for, why you need the data and what you are going
> to do with it."

### Benefits of sharing software

```{instructor-note}
We revisit answers to question 1 (above).
```

#### Motivation for open source software

- Enable derivative work
- Do not lock yourself out of own code
- Attract developers who want to be able to show the coding work on their CVs
- Tightly regulated domains require open source
- Open-source software (OSS) can lead to more engagement from industry which may lead to more impact
- If it's not open, it is not likely to become standard

### Sharing software is also scary

```{instructor-note}
We revisit answers to question 2 (above).
```

- **Fear of being scooped**
  > A license can avoid it, and you can release when you are ready. Anyway, it is
  > very unlikely that others will understand your code and publish before you
  > without involving you in a collaboration. Sharing is a form of publishing.
- **Exposes possibly "ugly code"**
  > In practice almost nobody will judge the quality of your code.
  > "Software, once written, is never really finished" (N. Asparouhova).
- **Others may find bugs and mistakes**
  > Isn't this good? Would you not like to use a code which gives people the chance to locate bugs?
  > If you don't release, people will assume there are bugs anyway.
- **Others may require support and ask too many questions**
  > This can become a problem: use tools and community and protect your time.
  > You aren't required to support anyone. You can also "archive" a repository to disable
  > most forms of interaction (issues, PRs). Also a note in README on support level helps.
- **Fear of losing control over the direction of the project**
  > Open source does not mean everybody can change **your version**.
- **"Bad" derivative projects may appear**
  > It will be clear which is the official version.

```{discussion} Social-2: Discussion about "You aren't required to support anyone"
- Have you experienced an implicit expectation of support?
- Supporting all requests can lead to overworking and mental health issues.
- Not supporting requests can also induce guilt.
- Most projects are maintained by 1 or 2 persons.
- Most projects cannot retain contributors for a longer time. Interests change.
  "Casual contributors are like tourists visiting NYC for a weekend" (Nadia
  Asparouhova, book below).
- If you maintain all projects that you start forever, at some point it may be difficult to start new projects.
- What are your experiences? Do you agree with the above thoughts?
- Book recommendation: Nadia Asparouhova (formerly Nadia Eghbal): "Working in
  Public: The Making and Maintenance of Open Source Software (Stripe Press)"
```

### Code reusability

Should you reuse things that others have done?

Types of things that can be reused:

- Main libraries (e.g. NumPy, SciPy)
- Special scientific libraries
- Random code from website
- Copying from Stack Overflow

Do you want others to reuse what you make?
How do you turn your own small project into the next NumPy? Do you want to?

#### What contributes to reusability?

What contributes to you being able to reuse stuff that others make, and others
(or you) being able to reuse your stuff? When you find a repository with code
you would like to reuse, you may look at the following things to determine its
reusability:

```{instructor-note}
This can be now reconnected to question 4 (above).
```

- Date of last code change
  > ... is the project abandoned?
- Release history
  > ... how about stability and backwards-compatibility?
- Versioning
  > ... will it be painful to upgrade?
- Number of open pull requests and issues
  > ... are they followed-up?
- Installation instructions
  > ... will it be difficult to get it running?
- Example
  > ... will it be difficult to get started?
- License
  > ... am I allowed to use it?
- Contribution guide
  > ... how to contribute and decision process?
- Code of conduct
  > ... how to make clear which behaviors are unacceptable and discouraged? How violations of Code of conduct will be handled?
- Trust and community
  > ... somebody you trust recommended it?

... most of which you have or will learn during this
[CodeRefinery](https://coderefinery.org) workshop!

### Sharing or not sharing?

```{figure} img/in-out.jpg
:alt: Our work depends on ideas, articles, data, and software

Whether and what we can share depends on how we obtained the components.
```

- Our work depends on outputs from others. Research of others depends on our outputs.
- Whether you can share your output depends on how you obtained your input.
- A repository that is private today might become public one day.
- Sometimes "OTHERS" are you yourself in the future in a different group/job.
- **Software licenses** matter. And this is what we will discuss in the next episode.

### A successful story after sharing code

> [Someone improved my code by 40,832,277,770%](https://www.youtube.com/watch?v=c33AZBnRHks)" by [https://www.youtube.com/user/standupmaths Stand-up Maths]

https://www.youtube.com/watch?v=c33AZBnRHks

## Code Review

> [Code Review](https://github.com/carpentries-incubator/managing-computational-projects/blob/gh-pages/_episodes/09-codereview.md) by [https://carpentries.org/ The Carpentries] is licensed under [http://creativecommons.org/licenses/by/4.0/ CC BY 4.0] Some additions were made to extend the content about the Pair Programming section

> The most difficult part of writing code is always to make it understandable to other people, including yourself a few months down the track. There’s certainly no shame in finding out that your code wasn’t as easy to understand or use as you’d hoped, so don’t take it personally when it happens (which it always does, at least in my experience), but treat it as an opportunity to improve.
>
> **Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)**

A simple objective of the review process is to catch bugs and elementary errors that might have been missed during the development phase.
Code review can also help improve the overall quality while ensuring that code is readable and easy to understand.
As a group leader, you can also make sure code is functional and literate as early as possible, and encourage your students to avoid messy "good enough" code that causes chaos later.

Code review is often done in pairs, with each reviewer also having some of their code reviewed by their partner.
Doing this can help programmers to see and discuss issues and alternative approaches to tasks, and to learn new tips and tricks.

![Garden of code](https://zenodo.org/api/iiif/v2/5c8c70c9-4119-4917-91d1-bc955943f586:328322b3-ab2f-43c8-a4ba-eb6e11d48ac0:reusable-code-garden-with-text.jpg/full/750,/0/default.jpg)

_The Turing Way project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807._

There are different methods for code review.

### Synchronous - Pair Programming

**Helping the student go through their scripts, catch errors and debug side by side**

- The PI sits down with her PhD student who has been writing a function for cleaning bioinformatics data.
- The PI knows Python well and takes the opportunity to discuss code while helping their student organise the code better.
- The student shows the PI some odd errors and so they run some tests with expected outcomes to find what the problem is and solve it.
- The PhD student learns and applies to test practices to help make code robust.

The problem with synchronous coding sessions is making time for it and whether or not the supervisor has experience with the specific language.

### Synchronous - Group Code Tour or Informal Walkthroughs

**Narrating code and software steps**

The researcher may present their pipeline to describe the logical steps using documentation, pseudocode, or describing how to run the code.

- A postdoc has been working on some analysis that provides statistics results that he hopes to publish soon. During a lab meeting, the postdoc presents the steps of the analysis code as logical steps.
- The lines of code are shown for those in the meeting that know R, but the postdoc explains the steps verbally as well for those who don't understand R.
- The group discuss and provides comments on the choices and order of the analysis pipeline, a PhD student notices a jump in logic that wasn't picked up previously, and an advanced R user in the lab makes suggestions about making some parts run faster.

These sessions do not rely on everyone knowing the language, and it is the responsibility of the coder to present their work clearly and logically for everyone to follow.
Group discussions can be very informative for everyone involved and put the analysis under scrutiny.

> ## Suggestions for the meeting leader
>
> - Keep it a safe environment, i.e. make sure chastising is relatively gentle even when deserved (but do point out when code doesn’t meet the required standard – frame it as a learning experience though).
> - Make sure there’s a core of vocal participants so it isn’t always you.
> - Make it clear when you’re presenting yourself that your code isn’t perfect, point out some of those imperfections yourself if the audience is slow to do so, and do present yourself.
> - Patiently explain when things are not wrong but just stylistic differences (but make it clear that some styles are bad, often helpful e.g. asking people to guess what a function returns from its name).
>
> _Shared by Rob Knight with Fernando Perez in the post [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)_

### Asynchronous - I'll get back to you on that

Making sure everyone is free at the same time for a lab meeting can be challenging.
Hence, asynchronous code review practices are more suitable for busy supervisors or collaborators in different time zones.

The asynchronous review process allows others to run the code themselves using a reproducible environment, or simply reads through the scripts and share their feedback asynchronously.

Consider a scenario:

> A postdoc has created a model in Python and creates a Binder with all the dependencies necessary.
> She sends the file to her supervisor who can run the code within her browser, no installation is required.
> The supervisor can then run the code herself to review it and check the individual parts over the next week.
> The supervisor adds a commented version of the script to the postdoc's repo with a merge request.

Reviewing code in small chunks incrementally as the project is developing can help make the code review process a lot more efficient.
Asynchronous feedback removes the time pressure but can be easily forgotten!

> Reviewing more than 400 lines of code (LoC) can have an adverse impact on your ability to find bugs, and in fact, most are found in the first 200 lines. - Recommendation from Code Review at Cisco Systems
>
> **[5 code review best practices. Work Life by Atlassian](https://www.atlassian.com/blog/add-ons/code-review-best-practices**), Usman Ghani\*\*

## Multiple people can also review the code asynchronously.

> [Turing Way: Recommendations for Code Reviewing](https://the-turing-way.netlify.app/reproducible-research/reviewing/reviewing-recommend.html)
>
> Unlike traditional, “academic-style” peer review, most code review systems have several advantages: they’re rarely anonymous, they’re public-facing, and without the broker of an editor, contact between reviewer and reviewee can be direct and rapid.
> This means code review is typically a fast, flexible, and interactive process.

> ## Github features to help with code review (Click to see)
>
> **Commit changes**: uploading snapshots when the code changes. The history of all changes are therefore saved and can be reverted.
>
> <img src="https://i.postimg.cc/MHm8X1zX/Screenshot-2022-02-10-at-16-35-50.png" alt="drawing" width="600"/>
>
> **Branching**: keep a version of the code separate while making experimental changes or keeping track of collaborative work. Can try out new functionality or edit in parallel without impacting the code base.
>
> <img src="https://i.postimg.cc/6p5v0Nb1/Screenshot-2022-02-10-at-18-52-47.png" alt="drawing" width="200"/>
>
> **Pull Request**: Bring the changes made on a branch over to the main code base. Can be used to request a code review (see Reviewers on the right panel)
>
> <img src="https://i.postimg.cc/5tgv5Rpm/Screenshot-2022-02-10-at-18-44-07.png" alt="drawing" width="600"/>
>
> **Review**: A pull request can be reviewed and commented on.
>
> <img src="https://i.postimg.cc/9XDbVyWQ/Screenshot-2022-02-10-at-19-11-58.png" alt="drawing" width="400"/>
>
> **Author: Lydia France (Junior Data Scientist, The Alan Turing Institute, UK)**

### Reviewing is not about creating more work, nor the PI rewriting everything

Instead, it is just another part of peer review and accountability within the scientific process.
It is also an opportunity for everyone to learn better practices from each other, and solve issues that have plagued one person for weeks!

> _Scientists are very aware that their understanding of code dissipates over time and that this is a large hidden cost. Equally, they suspect that they spend a lot of time reinventing wheels.
> They may not know how code review will help with that, but they hope that it will._
>
> _One of the mentors expected scientists to overhaul complete code bases. The advice from one mentor was cogent: if you check the docstring and write a test every time you touch a method, the code improvements will accumulate over time with minimal effort._
>
> _Someone who isn’t intimately involved with your project should understand from the module documentation and the comments what you are trying to do, what approach you’re taking, and why they should expect it to work._
>
> _Take some time to prepare a presentation about your code that will answer the above questions even for someone who hasn’t read the code. You’re more likely to get useful feedback, rather than nitpicking about syntax, if the audience can see the big picture._
>
> _Keep it a safe environment, i.e. make sure chastising is relatively gentle even when deserved (but do point out when code doesn’t meet the required standard – frame it as a learning experience though)._
>
> **_Marian Petre and Greg Wilson. "Code review for and by scientists: preliminary findings." (2014)._**

For further considerations in code review, please read [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) chapter in _The Turing Way_.

### What to look for during Code Review

<img src="https://the-turing-way.netlify.app/_images/readable-code.jpg" alt="drawing" width="400"/>

Reviewing code makes a big difference. Knowledge of the language is not always necessary!

These are very common, everyone does this.

**Bugs/Potential bugs**

- Repetitive code
- Code saying one thing, documentation saying another
- Off-by-one errors
- Making sure each function does one thing only
- Lack of tests and sanity checks for what different parts are doing
- Magic numbers (a number hardcoded in the script)

**Unclear, messy code**

- Bad variable/method names
- Inconsistent indentation
- The order of the different steps
- Too much on one line
- Lack of comments and signposting

**Fragile and non-reusable code**

- Tailor-made and manual steps
- Only works with the given data

*Modified from [*What to look for when code reviewing*](https://www.cs.swarthmore.edu/~alinen/cs71/labs/lab03.html)*

### Benefits of Code Review

> In a group of 11 programs developed by the same group of people, the first 5 were developed without reviews.
> The remaining 6 were developed with reviews. After all the programs were released to production, the first 5 had an average of 4.5 errors per 100 lines of code.
> The 6 that had been inspected had an average of only 0.82 errors per 100. Reviews cut the errors by over 80 percent.
>
> **[Code Complete](https://www.oreilly.com/library/view/code-complete-2nd/0735619670) by Steve McConnell**

The main benefit is finding problems, and finding them early enough that there aren't frustrating consequences.
The penalty for finding a bug once all the figures have been produced and conclusions drawn, or, worst-case scenario, after a publication, is much higher than the penalty for taking the time to review.

> ## Writing code collaboratively also benefit directly your team members:
>
> - Less time redoing work or refactoring
> - Increased productivity
> - Greater confidence in own work
> - Learning better techniques
> - Reduced time debugging alone
> - Knowledge exchange and group cohesion

> ## For a group leader, the benefits include:
>
> - Better understanding of the projects
> - More maintainable and better-documented code that is easy to understand and modify
> - Better insight into any problems with data
> - Earlier visibility of quality issues
> - Group reviews reduce the work burden
> - More robust analysis pipelines that can be reused and modified
> - High-quality code that can be released

**Important things to bear in mind:**

Code reviews should not be used to evaluate individuals and their skill levels.
An open and safe environment where revealing mistakes and errors should not come with penalties or shame.
Code reviews should also be done early and often, to normalise this practice in the research team.

In their book **Peer Reviews in Software: A Practical Guide**, Karl E. Wiegers says:

_The temptation to perfect the product before you allow another pair of eyes to see it.
This is an ego-protecting strategy: you won’t feel embarrassed about your mistakes if no one else sees them.
...review [is not] a seal of approval but rather in-process quality-improvement activity.
Such reluctance has several unfortunate consequences.
If your work isn’t reviewed until you think it’s complete, you are psychologically resistant to suggestions for changes._

If the program runs, how bad can it be? You are likely to rationalise away possible bugs because you believe you’ve finished and you’re eager to move on to the next task. Relying on your own desk checking and unit testing ignores the greater efficiency of a peer review for finding many defects\*

## Group Code Writing

As well as reviewing specific scripts and analyses written by a single individual, can be very beneficial to solving programming problems as a team.
Setting aside an afternoon to work as a group will help teach less experienced members of the group and more efficiently solve very difficult problems.

Groups of people working on a specific problem are often known as "Hackathons" in programming.
These can last multiple days (hopefully with downtime!). With very large groups, people can work in pairs or small groups with delegated parts of the problem to solve and regularly meet back together to discuss and evaluate.
If there is a complex solution in computational methods that most people in the group need, it makes sense to find it together.

Similarly, documentation sprints are useful to dedicate time to regularly bring a codebase to a good minimum standard.
Splitting the task across the team as an event, creating documentation and working examples for code repos and releasing it can help others use your computational methods and tools to increase the impact of your work.
Having regularly updated documentation also reduces onboarding time for new members picking up the shared methods in the lab.

Group work shares the burden and allows knowledge exchange and support within the team.

## References

- _The Turing Way_ Community. (2021). The Turing Way: A handbook for reproducible, ethical and collaborative research (1.0.1). Zenodo. https://doi.org/10.5281/zenodo.5671094. [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) Chapter.
- Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)

## Exercise: pair programming

In this exercise you will try out pair programming from the two different roles: driver and navigator.

In this task you will have to:

1. Work in pairs and try to code the [Fibonacci function](https://en.wikipedia.org/wiki/Fibonacci_number)

> In mathematics, the Fibonacci numbers, commonly denoted Fn , form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones.

2. Switch navigator/driver roles
3. Work in pairs and try to code the [Tribonacci function](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers)
   > The tribonacci numbers are like the Fibonacci numbers, but instead of starting with two predetermined terms, the sequence starts with three predetermined terms and each term afterwards is the sum of the preceding three terms.

## Exercise: reviewing each other's code

Take the code produced by one of the group in the previous exercise and write a formal code review following the [NBIS code development guidelines](https://github.com/NBISweden/development-guidelines). Share your review with the authors and discuss. Take into consideration the NBIS guidelines when writing reviews.
````
