---
marp: true
size: 16:9
paginate: false
style: |
  :root {
    font-family: IBM Plex Sans;
    color: #003300;
  }
  h1 {
    font-size: 1rem;
    border-bottom: 1px solid #003300;
  }
  h2 {
    font-size: 0.75rem;
  }
---

# What social obstacles have you encountered in code reviews?

- Conflicts of interest
- Misunderstandings
- Misinterpretations
- Emotional reactions: code ownership
- Lack of feedback because of not great psychological safety

# Making code understandable

> The most difficult part of writing code is always to make it understandable to other people, including yourself a few months down the track. There’s certainly no shame in finding out that your code wasn’t as easy to understand or use as you’d hoped, so don’t take it personally when it happens (which it always does, at least in my experience), but treat it as an opportunity to improve.
>
> **Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)**

---

# Synchronous - Pair Programming

**Helping the student go through their scripts, catch errors and debug side by side**

- The PI sits down with her PhD student who has been writing a function for cleaning bioinformatics data.
- The PI knows Python well and takes the opportunity to discuss code while helping their student organise the code better.
- The student shows the PI some odd errors and so they run some tests with expected outcomes to find what the problem is and solve it.
- The PhD student learns and applies to test practices to help make code robust.

The problem with synchronous coding sessions is making time for it and whether or not the supervisor has experience with the specific language.

---

# Synchronous - Group Code Tour or Informal Walkthroughs

**Narrating code and software steps**

The researcher may present their pipeline to describe the logical steps using documentation, pseudocode, or describing how to run the code.

- A postdoc has been working on some analysis that provides statistics results that he hopes to publish soon. During a lab meeting, the postdoc presents the steps of the analysis code as logical steps.
- The lines of code are shown for those in the meeting that know R, but the postdoc explains the steps verbally as well for those who don't understand R.
- The group discuss and provides comments on the choices and order of the analysis pipeline, a PhD student notices a jump in logic that wasn't picked up previously, and an advanced R user in the lab makes suggestions about making some parts run faster.

These sessions do not rely on everyone knowing the language, and it is the responsibility of the coder to present their work clearly and logically for everyone to follow.
Group discussions can be very informative for everyone involved and put the analysis under scrutiny.

---

# Suggestions for the meeting leader

> - Keep it a safe environment, i.e. make sure chastising is relatively gentle even when deserved (but do point out when code doesn’t meet the required standard – frame it as a learning experience though).
> - Make sure there’s a core of vocal participants so it isn’t always you.
> - Make it clear when you’re presenting yourself that your code isn’t perfect, point out some of those imperfections yourself if the audience is slow to do so, and do present yourself.
> - Patiently explain when things are not wrong but just stylistic differences (but make it clear that some styles are bad, often helpful e.g. asking people to guess what a function returns from its name).
>
> _Shared by Rob Knight with Fernando Perez in the post [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)_

---

# Asynchronous - I'll get back to you on that

Consider a scenario:

> A postdoc has created a model in Python and creates a Binder with all the dependencies necessary.
> She sends the file to her supervisor who can run the code within her browser, no installation is required.
> The supervisor can then run the code herself to review it and check the individual parts over the next week.
> The supervisor adds a commented version of the script to the postdoc's repo with a merge request.

---

# Multiple people can also review the code asynchronously.

> Unlike traditional, “academic-style” peer review, most code review systems have several advantages: they’re rarely anonymous, they’re public-facing, and without the broker of an editor, contact between reviewer and reviewee can be direct and rapid.
> This means code review is typically a fast, flexible, and interactive process.

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

---

# Reviewing is not about creating more work, nor the PI rewriting everything

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

---

# What to look for during Code Review

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

---

# Benefits of Code Review

> In a group of 11 programs developed by the same group of people, the first 5 were developed without reviews.
> The remaining 6 were developed with reviews. After all the programs were released to production, the first 5 had an average of 4.5 errors per 100 lines of code.
> The 6 that had been inspected had an average of only 0.82 errors per 100. Reviews cut the errors by over 80 percent.
>
> **[Code Complete](https://www.oreilly.com/library/view/code-complete-2nd/0735619670) by Steve McConnell**

The main benefit is finding problems, and finding them early enough that there aren't frustrating consequences.
The penalty for finding a bug once all the figures have been produced and conclusions drawn, or, worst-case scenario, after a publication, is much higher than the penalty for taking the time to revie

---

# Writing code collaboratively also benefit directly your team members:

> - Less time redoing work or refactoring
> - Increased productivity
> - Greater confidence in own work
> - Learning better techniques
> - Reduced time debugging alone
> - Knowledge exchange and group cohesion

---

# For a group leader, the benefits include:

> - Better understanding of the projects
> - More maintainable and better-documented code that is easy to understand and modify
> - Better insight into any problems with data
> - Earlier visibility of quality issues
> - Group reviews reduce the work burden
> - More robust analysis pipelines that can be reused and modified
> - High-quality code that can be released

---

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

---

# Group Code Writing

As well as reviewing specific scripts and analyses written by a single individual, can be very beneficial to solving programming problems as a team.
Setting aside an afternoon to work as a group will help teach less experienced members of the group and more efficiently solve very difficult problems.

Groups of people working on a specific problem are often known as "Hackathons" in programming.
These can last multiple days (hopefully with downtime!). With very large groups, people can work in pairs or small groups with delegated parts of the problem to solve and regularly meet back together to discuss and evaluate.
If there is a complex solution in computational methods that most people in the group need, it makes sense to find it together.

Similarly, documentation sprints are useful to dedicate time to regularly bring a codebase to a good minimum standard.
Splitting the task across the team as an event, creating documentation and working examples for code repos and releasing it can help others use your computational methods and tools to increase the impact of your work.
Having regularly updated documentation also reduces onboarding time for new members picking up the shared methods in the lab.

Group work shares the burden and allows knowledge exchange and support within the team.

---

# References

This material is based on the Code Review lecture by The Carpentries:

> - [Code Review](https://github.com/carpentries-incubator/managing-computational-projects/blob/gh-pages/_episodes/09-codereview.md) by [The Carpentries](https://carpentries.org/) is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/). Some additions were made to extend the content about Pair Programming.
> - _The Turing Way_ Community. (2021). The Turing Way: A handbook for reproducible, ethical and collaborative research (1.0.1). Zenodo. https://doi.org/10.5281/zenodo.5671094. [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) Chapter.
> - Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)

---

# Exercise: pair programming

In this exercise you will try out pair programming from the two different roles: driver and navigator.

In this task you will have to:

1. Work in pairs and try to code the [Fibonacci function](https://en.wikipedia.org/wiki/Fibonacci_number)

> In mathematics, the Fibonacci numbers, commonly denoted Fn , form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones.

2. Switch navigator/driver roles
3. Work in pairs and try to code the [Tribonacci function](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers)
   > The tribonacci numbers are like the Fibonacci numbers, but instead of starting with two predetermined terms, the sequence starts with three predetermined terms and each term afterwards is the sum of the preceding three terms.

---

# Exercise: reviewing each other's code

Take the code produced by one of the group in the previous exercise and write a formal code review following the [NBIS code development guidelines](https://github.com/NBISweden/development-guidelines). Share your review with the authors and discuss. Take into consideration the NBIS guidelines when writing reviews.
