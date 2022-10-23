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

---

# Suggestions for the meeting leader

> - Keep it a safe environment
> - Facilitate participation in the session
> - Make it clear that your code isn’t perfect
> - Patiently explain when things are not wrong but just not ideal

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

Instead, it is just another part of peer review and accountability within the scientific process.
It is also an opportunity for everyone to learn better practices from each other, and solve issues that have plagued one person for weeks!

For further considerations in code review, please read [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) chapter in _The Turing Way_.

---

# Who should do a Code Review?

> "Anyone" should be able to perform code reviews.

<img src="https://the-turing-way.netlify.app/_images/readable-code.jpg" alt="drawing" height="70%" width="70%" style="display: block; margin: 0 auto">

---

# What to look for during Code Review? - Bugs

- Repetitive code
- Code saying one thing, documentation saying another
- Off-by-one errors
- Making sure each function does one thing only
- Lack of tests and sanity checks for what different parts are doing
- Magic numbers (a number hardcoded in the script)

---

# What to look for during Code Review? - Unclear code

- Bad variable/method names
- Inconsistent indentation
- The order of the different steps
- Too much on one line
- Lack of comments and signposting

---

# What to look for during Code Review? - Reusability

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

> - [Code Review](https://github.com/carpentries-incubator/managing-computational-projects/blob/gh-pages/_episodes/09-codereview.md) by [The Carpentries](https://carpentries.org/) is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/). Some additions were made to extend the content about Pair Programming.
> - _The Turing Way_ Community. (2021). The Turing Way: A handbook for reproducible, ethical and collaborative research (1.0.1). Zenodo. https://doi.org/10.5281/zenodo.5671094. [Code Reviewing Process](https://the-turing-way.netlify.app/reproducible-research/reviewing.html) Chapter.
> - Fernando Perez, [Code reviews: the lab meeting for code](http://fperez.org/py4science/code_reviews.html)

---

# Exercise: pair programming

In this exercise you will try out pair programming from the two different roles: driver and navigator.

In this task you will have to:

1. Work in pairs and try to code the [Fibonacci function](https://en.wikipedia.org/wiki/Fibonacci_number) or other function that the instructors will suggest.

> In mathematics, the Fibonacci numbers, commonly denoted Fn , form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones.

2. Switch navigator/driver roles
3. Work in pairs and try to code the [Tribonacci function](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers) or other function that the instructors will suggest.

> The tribonacci numbers are like the Fibonacci numbers, but instead of starting with two predetermined terms, the sequence starts with three predetermined terms and each term afterwards is the sum of the preceding three terms.

---

# Exercise: reviewing each other's code

Take the code produced by one of the group in the previous exercise and write a formal code review following the [NBIS code development guidelines](https://github.com/NBISweden/development-guidelines). Share your review with the authors and discuss. Take into consideration the NBIS guidelines when writing reviews.
