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

> Why bother about sharing our code?

# Comparing sharing papers and sharing code

<img src="https://github.com/coderefinery/social-coding/blob/main/content/img/sharing-papers.jpg?raw=tru" width="800" height="600" style="display: block; margin: 0 auto" />

---

# Comparing sharing papers and sharing code

<img src="https://github.com/coderefinery/social-coding/blob/main/content/img/sharing-code.jpg?raw=true" width="800" height="600" style="display: block; margin: 0 auto" />

---

# Science editorial policy

From [Science editorial policy](https://www.sciencemag.org/authors/science-journals-editorial-policies):

> "We require that **all computer code used for modeling and/or data analysis**
> that is not commercially available be deposited in a **publicly accessible repository**
> upon publication. In rare exceptional cases where security
> concerns or competing commercial interests pose a conflict, code-sharing
> arrangements that still facilitate reproduction of the work should be
> discussed with your Editor no later than the revision stage."

---

# Nature editorial policy

From [Nature editorial policy](https://www.nature.com/authors/policies/availability.html):

> "An inherent principle of publication is that others should be able to
> replicate and build upon the authors' published claims. A condition of
> publication in a Nature Research journal is that authors are required to make
> **materials, data, code, and associated protocols promptly available** to readers
> without undue qualifications. Any restrictions on the availability of
> materials or information must be disclosed to the editors at the time of
> submission. Any restrictions must also be disclosed in the submitted
> manuscript."

---

# Are these policies working?

> "When you approach a PI for the source codes and raw data, you better explain
> who you are, whom you work for, why you need the data and what you are going
> to do with it."

---

# Motivation for open source software

- Enable derivative work
- Do not lock yourself out of own code
- Attract developers who want to be able to show the coding work on their CVs
- Tightly regulated domains require open source
- Open-source software (OSS) can lead to more engagement from industry which may lead to more impact
- If it's not open, it is not likely to become standard

---

# Sharing software is also scary

- Fear of being scooped
- Exposes possibly "ugly code"
- Others may find bugs and mistakes
- Others may require support and ask too many questions
- Fear of losing control over the direction of the project
- "Bad" derivative projects may appear

---

# Code reusability

Types of things that can be reused:

- Main libraries (e.g. NumPy, SciPy)
- Special scientific libraries
- Random code from website
- Copying from Stack Overflow

> Do you want others to reuse what you make?
> How do you turn your own small project into the next NumPy? Do you want to?

---

# What contributes to reusability?

What contributes to you being able to reuse stuff that others make, and others
(or you) being able to reuse your stuff? When you find a repository with code
you would like to reuse, you may look at the following things to determine its
reusability:

---

# Sharing or not sharing?

> Whether and what we can share depends on how we obtained the components.

- Our work depends on outputs from others. Research of others depends on our outputs.
- Whether you can share your output depends on how you obtained your input.
- A repository that is private today might become public one day.
- Sometimes "OTHERS" are you yourself in the future in a different group/job.
- **Software licenses** matter. And this is what we will discuss in the next episode.

---

# References

This material is based on the Social Coding lecture by Code Refinery:

> [Social coding](https://github.com/coderefinery/social-coding/blob/main/content/social-coding.md) by [CodeRefinery](https://coderefinery.org/) is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).
