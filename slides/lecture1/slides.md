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

<!-- I'm going periodically ask for a show of hands. Please participate as it helps me to understand the level of detail I should go into.  -->

---
# Where are we going? (An overview and a philosophy)


<!--
- Too often things are taught academically to be 100% technically accurate
    - Taught by people who are experts in the field. 
    - I have a different approach. Get 90% of the meaning. Fill it in later. Explain it in a way that rather than saying "Goddam that guy is smart" its more like "Why didn't I get into engineering. A monkey could do this". 
        - There is OFC more to this than I'm initially discussing, but I think its hugely helpful to start from a place of "Oh, ok, I get what you're doing and where you're going" vs "I don't know any of those words. I'm not even sure what the point of this is, I'm drowing in terminology"
 -->


---
layout: center
class: text-center
---

# Their proposal
> We propose that a 2-month, 10-man study of artificial intelligence be carried out during the summer of 1956 at Dartmouth College in Hanover, New Hampshire. The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it. An attempt will be made to find how to make machines use language, form abstractions and concepts, solve kinds of problems now reserved for humans, and improve themselves. We think that a significant advance can be made in one or more of these problems if a carefully selected group of scientists work on it together <span v-mark.red="2"> for a summer.</span>

---
# In practice
- Nebulous term now. Basically, "computer doing something useful".

- <img src="/public/spellcheck.JPG" height="300px">

- Spellcheck
    - Not particularly smart (for each word, look in the dictionary, if an exact match isn't found, look for the nearest match (Levenstein distance or something similar))
    - But at one time revolutionary.

- Marketing term
    - Mentions of AI during investor conference calls
    - <img src="/public/earning_call_ai_mentions.png" height="300px">
- Umbrella term
    <!-- - <img src="../imgs/venn_diagram_ai.JPG" height="300px"> -->
    - Machine Learning is what has generated all the interesting progress, that's what we'll focus on
        - `Learning from data examples`
            - Instructing a machine is hard. Humans are bad at considering a state space. May not even be able to describe (or know) how to find a solution.
                - Bouncer example.
                    - Task: Don't allow anyone through the door unless they are of age.
                        - Sounds simple (Gate access to one entry point, )
                        - What does that mean? People should be 18+ years old
                        - Which IDs? Other states? Passports? Foreign IDs? Driver's licences only?
                        - Where to find the DOB information?
                        - Someone shows up with a 2 digit year "12" are they 112? Or 12?
                        - Stop people from entering the door w/o checking ID
                            - What about the window?
                        - Tremendous amount of prior knowledge about the world must either be present, or accounted for by programmer. 
                        - Many failure modalities
                - House pricing example. 
                    - Many examples. Pricing + features. Something discoverable.


---
# Where are we going? (An overview and a philosophy)
