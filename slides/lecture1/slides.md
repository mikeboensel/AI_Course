---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides, markdown enabled
title: Foundations of AI
info: |
  ## Foundations of AI
  A Boston AI User Group presentation
# apply any unocss classes to the current slide
class: text-center
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# https://sli.dev/guide/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/guide/syntax#mdc-syntax
mdc: true
---

# Foundations of AI

A Boston AI User Group presentation

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/mikeboensel/AI_Course" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
layout: image-right
image: /public/common_profile_pic.jpg
backgroundSize: "90%"
---

# Who am I?

- SW Dev at MIT Lincoln Lab
  - (Standard disclaimer... views not endorsed by them)
<br>
<br>
- "Is this going to take my job yet?"
  - 2010 - Pandora, other recommender systems
  - 2015 - GANs
  - 2022 - Transformer-based

<style>
  h1{text-align:center;}
</style>

<!--    
- 2010 - Andrew Ng Machine Learning coursera course
- 2015 - GAN hype
- 2021 - Stable Diffusion/ChatGPT/Dall-E
-->

---
layout: image-right
image: /public/mystery_person.webp
backgroundSize: "90%"
---
# Who are you?
<br><br><br>
- Want to target this at the audience
- Appropriate level of detail
- Audience participation required! 

<!-- 
I'm going periodically ask for a show of hands. Please participate as it helps me to understand the level of detail I should go into.  
-->

---
---
# Where are we going? (An overview and a philosophy)
- Filler text

<!--
- Too often things are taught academically to be 100% technically accurate
    - Taught by people who are experts in the field. 
    - I have a different approach. Get 90% of the meaning. Fill it in later. Explain it in a way that rather than saying "Goddam that guy is smart" its more like "Why didn't I get into engineering. A monkey could do this". 
        - There is OFC more to this than I'm initially discussing, but I think its hugely helpful to start from a place of "Oh, ok, I get what you're doing and where you're going" vs "I don't know any of those words. I'm not even sure what the point of this is, I'm drowing in terminology"
 -->

---
layout: image
image: /public/DartmouthWorkshop.JPG
backgroundSize: "50%"
---
# What is AI?
Coined in the 50s, at a Dartmouth Summer Workshop


---
layout: image
image: /public/DartmouthWorkshop2.JPG
backgroundSize: "55%"
---
# Just another day at Summer Camp

<style>
  h1{text-align:center;}
</style>

---
---

# How hard could this be?
<br>
<br>
<br>
<div style="display:flex; justify-content:center">

> We propose that a 2-month, 10-man study of artificial intelligence be carried out during the summer of 1956 at Dartmouth College in Hanover, New Hampshire. The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it. An attempt will be made to find how to make machines use language, form abstractions and concepts, solve kinds of problems now reserved for humans, and improve themselves. We think that  <span v-mark.red="1">a significant advance can be made</span> in one or more of these problems if a carefully selected group of scientists work on it together for  <span v-mark.red="2"> a summer.</span>
</div>

<style>
  h1{text-align:center;}
</style>

---
layout: intro
---
# It turned out to take a little longer than anticipated...


---
layout: image
image: /public/HistoryOfAI.JPG
backgroundSize: "75%"
transition: fade-out

---


---
layout: image
image: /public/HistoryOfAI-Annotated.JPG
backgroundSize: "75%"
---



---
---
# In practice
- Nebulous umbrella term now. Basically, **computer doing something useful and impressive**.
- I'd argue its also a moving target.
- Ex: Spellcheck, probably revolutionary when initially released. Not particularly smart. 
- <img src="/public/spellcheck.JPG" width="300px">

---
---
# Marketing term
- A way to juice your stock price. 
- Mentions of AI during investor conference calls:
<img src="/public/earning_call_ai_mentions.png" height="300px">

---
layout: image
image: /public/venn_diagram_ai.JPG
backgroundSize: "75%"
---
# Umbrella term

---    
---
# Machine Learning
- is what has generated all the interesting progress, that's what we'll focus on
- `Learning from data examples`
- Let's examine why this is interesting

---
---
# Common Sense isn't very common
- Instructing a machine is hard. Humans are bad at considering a state space or the algorithm they use to navigate it. May not even be able to describe (or know) how to find a solution.
- Consider how much effort/time/expense goes into training a new hire. Its a ton. 
- A new hire is DRAMATICALLY smarter than a computer. Computers are dumb. They work quickly, which can give them impression they aren't and they can be instructed to do intelligent/useful things, but fundamentally dumb
- What do I mean by dumb? 

---
---
# Fundamental problem of Software Engineering
- The state space under consideration for everything is big. 
- Unlikely to anticipate it all.
- Unlikely that unanticipated situations will be handled in a satisfactory way (Murphy's Law)
  - >The airplane's control SW ran into an unexpected scenario. We're now going to be there 30 minutes earlier.
    - Has never happened.
  - <img src="/public/airline_announcement.webp" width="20%">

  - Most likely going to crash, because disorder is the fundamental state of the world


---
---
# I thought we were talking about AI...
- Bear with me, on this sojourn into software. It will become obvious later why I'm equating the 2.
- The business of writing SW, is the business of custom **function creation**.
<img src="/public/function_creator.webp" width="50%" style="margin-left:25%">

---
layout: image-right
image: "/public/robot_bouncer.webp"
---

# Bouncer example
- Task: Don't allow anyone through the door unless they are of age.
    - Sounds simple. Let's try to formalize it.
      - Don't let anyone thru the door if the date string on their driver's license doesn't indicate their age >= 21.
      - <img src="/public/drivers_licence.webp" width="70%">
    - 12/1/1985 ✅
    - 5/22/2010 ❌
---
---
# Bouncer example gets hairier    
- Which IDs? Other states? https://www.businessinsider.com/what-drivers-license-looks-like-in-every-state
  - Where to find the DOB information? Most call it `DOB`, but label might be above OR to the left of, or below
  - God help us... Passports? Foreign IDs?
- Someone shows up with a 2 digit year "3/1/12" are they 112? Or 12?
- We stop people from entering the door w/o checking ID
    - What about the window? Or another door? Task really doesn't just involve this door, more general security...
- Not even touching on teenagers acting w/ malice...
- Tremendous amount of knowledge about the world must be encoded for this to succeed. 
- Many failure modalities

---
---
# If you had to pick 3 key ideas to explain ML
1. Neural Nets are f(x) approximators and the world is full of functions
- Quick f(x) definition - Equation that takes an input and gives some output
  - F(x) for pricing a house, picking an NBA draftee, writing a letter, even art
  - <img src="/public/nfl_draft.webp" width="20%">
  - <img src="/public/nfl_draft.jpg" width="20%">
- If a human can do it, I take that as a prior indicating that it is a task that can be solved algorithmically (may not be able to state what the algo is, but it exists and can be discovered)
    - Somewhat philosophical. Some people believe in some greater, undefined quantity ("spirit/essence"). I don't. I think we're all bounded by the laws of nature and math. I can't prove it, but I've yet to see anyone prove the other case either. So that's my bias. You may not believe everything is this way, but I think we can agree most things are.

---
---
# 3 Key ideas (continued)
2. There's a deep underlying structure to the universe (latent spaces/embeddings, model merging, generative AI ability to interpolate)
- Even things that might not seem interpolatable
    - Ex: human faces https://thispersondoesnotexist.com/
---
---
# 3 Key ideas (continued)
3. Once you've learned something its easier to learn other similar things
- Intuitively makes sense to us. Magnus Carlsen - Chess. If I told you he was also really good at checkers, backgammon, etc. You'd be pretty accepting of it.
- `Transfer learning` -- makes sense because learning just means discovering some underlying structure about the universe. If you know some, easier to acquire others (vs being random unitialized)
So...
- There's an underlying structure to the universe that
    - Can be learned
    - Can be interpolated over

---
---
# NN Introduction
- Can learn any f(x) (Universal Approximation Theorem)
- Uses multiplication, addition, and a non-linearity to make predictions (sometime a little more, but pretty simple!)
- Uses a loss function and calculus to train
## MNIST w/ dense NN
    - Show MNIST, explain how a labeled dataset works
    - Graph losses
## NFL Draft modeling -- https://github.com/nflverse/nflverse-data/releases  https://www.pro-football-reference.com/draft/2002-combine.htm

---
---
# Datasets/Contests/Leaderboards
- What gets measured gets done
- Collection/labeling of data is a very expensive endeavor
- Even collection of "unlabeled data" is expensive
    - Scraping, storage
- Having readily available datasets for different domains facilitates research
- MNIST - https://huggingface.co/datasets/mnist
- ImageNET - https://huggingface.co/datasets/imagenet-1k
- Most of the progress recently has been in LLMs, more difficult to score/setup challenges
    - Interesting approach from https://arena.lmsys.org/ (Chatbot arena) -- ELO system and head to head contests






----------------------
- House pricing example. 
    - Many examples. Pricing + features. Something discoverable.