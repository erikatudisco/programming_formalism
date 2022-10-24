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
    font-size: 1.3rem;
    border-bottom: 1px solid #003300;
  }
  h2 {
    font-size: 0.9rem;
  }
---

<style scoped>
p {
  font-size: 80px;
}
</style>

> What is code reviewing and how can it improve our code?

---

# Making code understandable

> The most difficult part of writing code is always to make it understandable to other people, including yourself a few months down the track. There’s certainly no shame in finding out that your code wasn’t as easy to understand or use as you’d hoped, so don’t take it personally when it happens (which it always does, at least in my experience), but treat it as an opportunity to improve.
>
> **Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)**

---

# Synchronous - Pair Programming

**Helping the student go through their scripts, catch errors and debug side by side**

- The PI sits down with her student who has been writing some code
- They discuss how the code could better.
- The student shows the PI some issues and they manage to solve it.
- The PhD student learns and makes the code more robust

---

# Pair Programming - Driver and Navigator

<img src="https://martinfowler.com/articles/on-pair-programming/driver_navigator.png" alt="drawing" height="70%" width="70%" style="display: block; margin: 0 auto">

---

# Pair Programming - Ping Pong

<img src="https://martinfowler.com/articles/on-pair-programming/ping_pong.png" alt="drawing" height="70%" width="70%" style="display: block; margin: 0 auto">

---

# Pair Programming - Strong-Style Pairing

<img src="https://www.thekguy.com/wp-content/uploads/2017/06/StrongStylePairing-1-1024x324.png" alt="drawing" height="75%" width="90%" style="display: block; margin: 0 auto">

---

# Pair Programming - Benefits and challenges

## Benefits

- We can produce better code working together
- We will ship fast for a longer time
- We build a "default" collaborative workflow in the group
- Less interruptions and happier people
- Recovering the flow becomes easier

## Challenges

- ??

---

# Pair Programming - The Pomodoro technique

<img src="https://martinfowler.com/articles/on-pair-programming/pomodoro.png" alt="drawing" height="75%" width="50%" style="display: block; margin: 0 auto">

---

# Synchronous - Group Code Tour or Informal Walkthroughs

**Narrating code and software steps**

The researcher may present their pipeline to describe the logical steps using documentation, pseudocode, or describing how to run the code.

- During a lab meeting, the postdoc presents the steps of his analysis R code as logical steps.
- The code is explained both to R programmers and non-experts.
- The group discuss and finds room for improvements on the choices and order of the analysis pipeline.

---

# Suggestions for the meeting leader

- Keep it a safe environment
- Facilitate participation in the session
- Make it clear that your code isn’t perfect
- Patiently explain when things are not wrong but just not ideal

---

# Asynchronous - I'll get back to you on that

Consider a scenario:

- A postdoc has created a model in Python and creates a Binder with all the dependencies necessary.
- She sends the file to her supervisor who can run the code within her browser, no installation is required.
- The supervisor can then run the code herself to review it and check the individual parts over the next week.
- The supervisor adds a commented version of the script to the postdoc's repo with a merge request.

---

# Multiple people can also review the code asynchronously.

> Unlike traditional, “academic-style” peer review, most code review systems have several advantages: they’re rarely anonymous, they’re public-facing, and without the broker of an editor, contact between reviewer and reviewee can be direct and rapid.

> This means code review is typically a fast, flexible, and interactive process.

---

# Branching

> **Branching**: keep a version of the code separate while making experimental changes or keeping track of collaborative work.

<img src="https://i.postimg.cc/6p5v0Nb1/Screenshot-2022-02-10-at-18-52-47.png" alt="drawing" height="70%" style="display: block; margin: 0 auto" />

---

# Pull Requests

> **Pull Request**: a code review request prior to merging the changes made on a branch over to the main branch.

<img src="https://i.postimg.cc/5tgv5Rpm/Screenshot-2022-02-10-at-18-44-07.png" alt="drawing" height="70%" style="display: block; margin: 0 auto" />

---

# Reviewing is not about creating more work, nor the PI rewriting everything

- Instead, it is just another part of peer review and accountability within the scientific process.
- It is also an opportunity for everyone to learn better practices from each other, and solve issues that have plagued one person for weeks!

> For further considerations in code review, please read [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) chapter in _The Turing Way_.

---

# What to look for during Code Review?

- Repetitive code
- Code saying one thing, documentation saying another
- Off-by-one errors
- Making sure each function does one thing only
- Lack of tests and sanity checks for what different parts are doing
- Magic numbers (a number hardcoded in the script)

---

# What to look for during Code Review?

- Bad variable/method names
- Inconsistent indentation
- The order of the different steps
- Lack of comments and signposting
- Tailor-made and manual steps
- Only works with the given data

*Modified from [*What to look for when code reviewing*](https://www.cs.swarthmore.edu/~alinen/cs71/labs/lab03.html)*

---

# Who should do a Code Review?

> "Anyone" should be able to perform code reviews.

<img src="https://the-turing-way.netlify.app/_images/readable-code.jpg" alt="drawing" height="70%" width="70%" style="display: block; margin: 0 auto">

---

# Benefits of Code Review

> In a group of 11 programs developed by the same group of people, the first 5 were developed without reviews.
> The remaining 6 were developed with reviews. After all the programs were released to production, the first 5 had an average of 4.5 errors per 100 lines of code.
> The 6 that had been inspected had an average of only 0.82 errors per 100. Reviews cut the errors by over 80 percent.
>
> **[Code Complete](https://www.oreilly.com/library/view/code-complete-2nd/0735619670) by Steve McConnell**

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

# To bear in mind when doing reviews

- Code reviews should not be used to evaluate individuals and their skill levels.
- An open and safe environment where revealing mistakes and errors should not come with penalties or shame.
- Code reviews should also be done early and often, to normalise this practice in the research team.

---

# What obstacles can we encounter in Code Reviews?

- Conflicts of interest
- Strong personal views about non crucial matters
- Misunderstandings and/or misinterpretations
- Code ownership
- Psychological safety

---

# Group Code Writing

- To work as a group will help teach less experienced members of the group and more efficiently solve very difficult problems.
- If there is a complex solution in computational methods that most people in the group need, it makes sense to find it together.
- Regular documentation updates are useful to dedicate time to regularly bring a codebase to a good minimum standard.
- Faster onboarding of members and greater impact of your work

---

# References

This material is based on the Code Review lecture by The Carpentries:

> - [Code Review](https://github.com/carpentries-incubator/managing-computational-projects/blob/gh-pages/_episodes/09-codereview.md) by [The Carpentries](https://carpentries.org/) is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/). Modifications were made in several chapters.
> - _The Turing Way_ Community. (2021). The Turing Way: A handbook for reproducible, ethical and collaborative research (1.0.1). Zenodo. https://doi.org/10.5281/zenodo.5671094. [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) Chapter.
> - Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)
> - Martin Fowler, [On Pair Programming](https://martinfowler.com/articles/on-pair-programming.html)
