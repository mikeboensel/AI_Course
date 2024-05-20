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
- Seems too simple? **We're going to use a lot of them!**

---
---
# Core operations
- Multiplication
- Addition
- 2 things that sound more complicated than they are:
  1. A non-linearity (aka `Activation f(x)`)
  2. Calculus
<img src="/public/calculus.webp" width="39%">

---
---
# Calculus simplified
- Simple concepts, made hard
- `"What if I have a wiggly line?"`
- Advanced area finding 
<div style="display:flex; justify-content: center;">
<img src="/public/calculus/area-of-a-Trapezoid.png" width="39%">
<img src="/public/calculus/riemann_sum_convergence.png" style="margin-left:30px" width="39%">
</div>

---
---
# Calculus simplified (cont.)
- Advanced slope calculations
<div style="display:flex; justify-content: center;">
<img src="/public/calculus/grad_descent_slope_calculation.jpg" width="49%">
<img src="/public/calculus/derivative.webp" style="margin-left:30px" width="49%">
</div>

---
---
# Why is this useful?
<div style="display:flex; justify-content: center;">
<img src="/public/calculus/rocket.jpg" width="49%">
<img src="/public/calculus/integration_differentiation_usage.png" style="margin-left:30px" width="49%">
</div>

---
---
# Easy example
<img src="/public/calculus/integration_example.png" width="149%">

---
layout: image-right
image: /public/calculus/3D_Scatter_with_Colormap.png
backgroundSize: "95%"
---
# Going interdimensional!
- We are limited to 3 dimensions, but math is not
- Going to be using 100s of dimensions
- Visualization is tough...
- These don't have an easy interpretation all the time. Somewhat mindbending

---
---
# Basic math still works in high dimensional space!
- Can't directly visualize (more on this later)
- Trig distance/angle ideas still hold
<img src="/public/calculus/pythagorean.png" width="60%">

<!-- 
Distance of 2 points, just the difference. 
3 points = Triangle
>3 = Just extend triangle concept
-->

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
# Traditional Stick and Ball
<img src="/public/nn_architecture_stick_and_ball.jpg" width="60%">

---
---
# Going Deeper
<img src="/public/nn_going_deeper1.JPG" style="margin-bottom:5px">

<img src="/public/nn_going_deeper2.JPG">

---
---
# Model capacity
- More line segments allow for more accurate following of the data
- Can get those 2 ways:
  - Siblings
  - Children
<img src="/public/nn_deeper_are_more_efficient.JPG">



---
---
# Matrices
- As a programmer, how do you represent a bunch of variables?
- Calling out each one? Nope
```python
w_0 = 1.1
w_1 = .043
# ... Great suffering later
w_99012 = 3.30
```
- A list? Better.
```python
w = [1.1, .043,...,3.30]
```
- List of lists => Matrix. Better still
```python
w = [[1.1, .043,...,3.30], [6.54, ....]]
```
- In practice, having these in source would be terrible, so we have serialized model files
```python
model.load_state_dict(torch.load(PATH))
```

---
---
# Matrices (2)

- Well studied mathematics around this (Linear Algebra)
- Lends itself to parallel operations (like multiplying/adding a lot)
- http://matrixmultiplication.xyz/
- https://www.intmath.com/matrices-determinants/matrix-addition-multiplication-applet.php

---
---
# Tensors
- WTF is this?
<img src="/public/tensor_def.jpg" width="75%">

---
---
# Wow, lots of math... must be important
Better learn what this is...

<div style="display:flex; justify-content: center; margin-bottom:10px">
<img src="/public/tensorflow.jpg" width="35%">
<img src="/public/tensor_TPU.jpg" width="25%" style="margin-left:20px">
</div>


<img src="/public/physics_envy.jpg">

---
---
# How do we fit our line segments?
2 step process:
1. How well are we doing? 
    - Measured via running our Data thru a Loss f(x) (aka Objective f(x))
2. Let's improve! 
    - Gradient Descent

<!--
This is a very simple, very nice Loss f(x). Real ones will be many dimensional, not smoothe, etc.
-->

---
---
# How good is our current Model?
- How to measure?
  - Depends on what the Model is targeting.
  - Categorical
<img src="/public/grad_descent/alexnet_predictions.png" width="50%">

---
layout: image-right
image: /public/nn_linear_fitting.jpg
---
# Numeric output is simpler 
- Sum of errors?
  - +/- cancel. Bad property!
- Sum of absolute errors?
  - Linear cost, less effective in practice
- Sum of squared errors?
  - Widely used

---
layout: image-right
image: /public/grad_descent/smoothe_vs_non_smoothe.jpg
backgroundSize: "95%"
---
# Loss Landscape is likely complex
- From https://www.telesens.co/loss-landscape-viz/viewer.html 

---
---
# Gradient Descent
<img src="/public/grad_descent/grad_descent_simple.JPG" width="75%">


---
---
# Gradient Descent (cont.)

<div style="display:flex; justify-content: center;">
<img src="/public/grad_descent/grad_descent_detailed.png" width="45%">
<img src="/public/grad_descent/grad_descent_slope_calculation.JPG" width="45%" style="margin-left:20px">
</div>

---
---
# We want to learn quickly
<img src="/public/grad_descent/grad_descent_speed.png">

---
---
# Remember the path is not likely to be straightforward
<img src="/public/grad_descent/grad_descent_3d.JPG">

---
---
# One last thing, then code!
- Holding out data for testing/validation is important
- Simulates the underlying reality that we almost always have insufficient data to know the true underlying distribution (the "World")
- Model is over-parametericized, can easily just memorize the training examples (vs learning good features that will broadly generalize)

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
