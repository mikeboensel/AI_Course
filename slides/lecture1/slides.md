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
Chatbot arena: https://arena.lmsys.org/
MNIST: https://en.wikipedia.org/wiki/MNIST_database
      https://huggingface.co/datasets/mnist
Embedding viz: https://projector.tensorflow.org/
-->

---
src: ./pages/intro.md
---

---
src: ./pages/what_is_ai.md
---

---
src: ./pages/sw_overlap_bouncer_ex.md
---

---
src: ./pages/key_ideas_of_ai.md
---

---
---
# NN Introduction
- Can learn any f(x) (Universal Approximation Theorem)
- Remember lines from grade school math? That's 90% of what we're doing here. 
- <img src="/public/line_equation.jpg" width="45%">
- Seems too simple? We're going to use a lot of them!

---
---
# Core operations
  - Multiplication
  - Addition
  - A non-linearity (an Activation f(x))
    - Sounds way more complicated than it is!
  - A little calculus (but you don't have to w/ PyTorch!)
    - Bad rap, simple concepts (Advanced slope finding + area under the curve (how do I do area and slope for a wiggly line?))
    - https://www.desmos.com/3d
    - https://www.desmos.com/
  <img src="/public/calculus.webp" width="39%">

---
layout: image-right
image: /public/nn_linear_fitting.jpg
backgroundSize: "95%"
---
# Given data, we can fit lines!
- What's a good fit?
- Define a Loss Function
- Adjust the line until we are happy

---
layout: center
hide: False
---
# Great, but real life isn't a series of lines!

---
---
# But it could be a series of small line segments (a piecewise function)
<img src="/public/nn_non_linearity_2_fitting.JPG" width="75%">

---
---
# How do?!?!
Non-linearities (aka Activation Functions)
<img src="/public/nn_activation_functions_relu.jpg" width="75%">
Ridiculously simple:
```python
def relu(input):
  if input > 0:
    return input
  else:
    return 0
```

---
---
# There must be other, more complicated ones!
<img src="/public/nn_activation_functions.jpg" width="65%">

---
---
# Putting it all together
<img src="/public/nn_non_linearity_1.jpg" width="60%">


---
---

# MNIST w/ dense NN
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


---
layout: image
image: /public/huggingfaces.jpg
backgroundSize: "90%"
title: Huggingfaces Overview
---


---
---
# Measuring is getting harder...
- Most of the progress recently has been in LLMs, more difficult to score/setup challenges
    - Interesting approach from https://arena.lmsys.org/ (Chatbot arena) -- ELO system and head to head contests


----------------------
- House pricing example. 
    - Many examples. Pricing + features. Something discoverable.


---
---
# Credits
- https://udlbook.github.io/udlbook/
