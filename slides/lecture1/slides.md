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
s

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
layout: center
---
# Neural Network Introduction

<!--
I want to start by giving us solid theoretical underpinnings.

That said, when I was younger I read a book.
-->

---
layout: image
image: /public/fermat_last_theorem_book.jpg
backgroundSize: "35%"
---

<!--
Mathematical "Who dun it". Great mystery surrounding a mathematician named Fermat.
-->

---
layout: image
image: /public/fermat_last_theorem.jpg
backgroundSize: "85%"
---

<!--
- Thousands of pages of manuscripts. 
- Presented a result, claimed a proof, did not provide it
  - A marvelous proof
- No one can figure it out for 100s of years
- Brilliant minds
- $1M prize for solving (Millenium Prize Problem, 7 most complex outstanding mathematical problem)

-->

---
layout: image
image: /public/fermat_last_theorem_solver.jpg
backgroundSize: "85%"
---
<!--
- Finally, this guy comes along.
- Look at him, Truly a mathematician's mathematician.
  - Hair
  - Glasses
  - Even the sweater!
  - This guy does math!

- Creates a proof so complex, using math that only a handful of people in the world know. 
- Work can't be checked by mere mortals.
- Is it solved, is it not? More compelling than I'm making it sound

Ok, so Fermat probably didn't have a proof.
-->

---
---
# Universal Approximation Theorem
  - Neural Networks can learn any f(x)

<v-click>
<img src="/public/trust_me_bro.jpg" width="50%"  style="margin-left:25%; margin-top:5%">
</v-click>

<!--
My version:
"There is a proof that exists, a marvelous proof, but I'm too dumb to explain it." 
Look it up if you're interested.
I'm sold, I don't need to check their work.
-->

---
layout: image-right
image: /public/line_equation.jpg
backgroundSize: "85%"
---
# How?
- Remember lines from grade school math? That's 90% of what we're doing here. 
- Seems too simple? 
  - **We're going to use a lot of them!**

---
---
# Core operations
<v-clicks depth="3">

- Multiplication
- Addition
- 2 things that sound more complicated than they are:
  1. A non-linearity (aka `Activation f(x)`)
  2. Calculus
<img src="/public/calculus.webp" width="39%">
</v-clicks>

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

# Easy example
<img src="/public/calculus/integration_example.png" width="149%">

<!--
- velocity * time =  distance traveled
- slope of velocity = acceleration
-->

---
layout: image-right
image: /public/calculus/3D_Scatter_with_Colormap.png
backgroundSize: "95%"
---
# To infinity... and beyond!
- We are limited to 3 dimensions, but math is not
- Going to be using 100s of dimensions
- Visualization is tough...
- These don't have an easy interpretation all the time. 
  - Somewhat mindbending

---
---
# Basic math still works in high dimensional space!
- Can't directly visualize (more on this later)
- Trig distance/angle ideas still hold
<img src="/public/calculus/pythagorean.png" width="60%">

<!-- 
Distance of 2 points, just the difference. 

3 points = Triangle

\>3 = Just extend triangle concept
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
# How do I break the lines?
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
<img src="/public/nn_activation_functions.jpg" width="65%" style="margin-left:15%">

---
---
# Putting it all together
<img src="/public/nn_non_linearity_1.jpg" width="60%" style="margin-left:15%">

---
---
# Traditional Stick and Ball diagram
<img src="/public/nn_architecture_stick_and_ball.jpg" width="60%" style="margin-left:15%">

---
---
# Getting stronger now!
<img src="/public/nn_going_deeper1.JPG" style="margin-bottom:5px">

<img src="/public/nn_going_deeper2.JPG">

<!--
We can increase the Model's "Power" or "Capacity" by adding more parameters
- Can get those 2 ways:
  - Siblings
  - Children
-->

---
---
# Model capacity
- More line segments allow for more accurate following of the data
- Deeper networks tend to be more efficient

<img src="/public/nn_deeper_are_more_efficient.JPG" width="80%" style="margin-left:7%">



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
- Lends itself to doing operations across a lot of data in very little notation
  - Say calculating thousands of line segments...
- 2 nice visualizers:
  - http://matrixmultiplication.xyz/
  - https://www.intmath.com/matrices-determinants/matrix-addition-multiplication-applet.php

---
---
# Tensors
WTF is this?

<img src="/public/tensor_def.jpg" width="75%">

<!--
You'll see this term come up a lot. 

The Wikipedia page is very dense.

-->

---
---
# Wow, lots of math... must be important
Better learn what this is...

<div style="display:flex; justify-content: center; margin-bottom:10px">
<img src="/public/tensorflow.jpg" width="35%">
<img src="/public/tensor_TPU.jpg" width="25%" style="margin-left:20px">
</div>


<img src="/public/physics_envy.jpg">

<!--
Its a fancy word for a Matrix.
-->

---
layout: image-right
image: /public/measure_then_cut.png
backgroundSize: "95%"
---
# How do we fit our line segments?
2 step process:
  1. Measure
      - How well are we doing? 
      - Found by running our Data thru a Loss f(x) (aka Objective f(x))
  2. "Cut"
      - Improve via Gradient Descent

---
layout: image-right
image: /public/grad_descent/alexnet_predictions.png
backgroundSize: "95%"
---
# How good is our current Model?
- How to measure?
  - Depends on what the Model is targeting.
  - Categorical is interesting
  - ImageNet Model (AlexNet on the right)

<!--
ImageNet
- 1000 images classes
- Model is given a picture, must determine what the Label is

Some seem unfair
- How heavily should we penalize
- Dalmation w/ cherry in it (bad training example)
- Convertible/Grill

Tend to do pretty simple measures
- Right class or not?
-->

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
# Loss f(x) Landscape is likely complex
- From https://www.telesens.co/loss-landscape-viz/viewer.html 

<!--
Seeing several popular Models with their loss visualized relative to the weights.

How? Thought this was thousands of dimensions? 
- Dimensionality reduction techniques. Lose some stuff, but can keep the general idea.

-->

---
---
# Our beautiful, simple Loss Landscape 
- Nothing in the real world looks this nice and smoothe
- We can perform Gradient Descent
  - AKA: Walking down the slope
<img src="/public/grad_descent/grad_descent_simple.JPG" width="70%">

<!--
Really important to remember when looking at these:
- "Go there, go to the low point you dumb Model!"
- Creating a full graph of a real Model would be incredibly expensive (likely impossible)
- A graph like this involves plugging in #s at a bunch of places to generate points, then connecting them.

All we know is our current weights losses + our current slope

-->
---
---
# Gradient Descent (in more detail)

<div style="display:flex; justify-content: center;">
<img src="/public/grad_descent/grad_descent_detailed.png" width="45%">
<img src="/public/grad_descent/grad_descent_slope_calculation.JPG" width="45%" style="margin-left:20px">
</div>

---
---
# We want to learn quickly, but not too quickly
<img src="/public/grad_descent/grad_descent_speed.png">

---
---
# Remember the path is not likely to be straightforward
<img src="/public/grad_descent/grad_descent_3d.JPG" style="margin-left:15%">

---
---
# One last thing, then code!
- Holding out data for testing/validation is important
- Simulates the underlying reality that we almost always have insufficient data to know the true underlying distribution (the "World")
- Model is generally over-parametericized, very "powerful" relative to the problem. 
<img src="/public/underfit_overfit_tradeoff.jpg" width="70%" style="margin-left:15%">

<!-- - Can easily just memorize the training examples (vs learning good features that will broadly generalize)
- Why do we start like this? Because it would suck to do a whole bunch of training only to find out we don't have a powerful enough model. Err on side of caution here. 
- Model really shouldn't be very confident in any of its predictions as data is always sparse at high dimensionality
- Overfit/Underfit  -->

---
---
# Curse of dimensionality
- All datasets is sparse at high dimensions
- Our toy graphs are not representative
<img src="/public/curse_of_dimensionality.png" width="100%">
- https://github.com/mikeboensel/AI_Course/blob/main/slides/lecture1/_notebooks/curse_of_dimensionality/dimensionality.ipynb
- https://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/


---
layout: image-right
image: /public/contortionist.jpg
backgroundSize: "90%"
---
# Model will contort itself
- Just trying to hit all datapoints
- Doesn't look so bad in our low-D graphs
- Reality is its making these complex shapes based off very few examples relative to the overall space
<img src="/public/underfit_overfit_tradeoff_reality.jpg" width="90%">


---
---
# Test/Validation/Train split
<img src="/public/test_train_validation_split.webp" width="100%">

- Will act to `Regularize` the Model's surface (make it smoother), but having high loss if we overfit vs the underlying distribution
  - Model should be fairly uncertain given the data sparsity


---
background: "/public/fermat_last_theorem.jpg"
---
# Our toolbox
<v-clicks depth="2">

| Tool    | Description |
| -------- | ------- |
| <img src="/public/tools_python.png" width="30px" style="display:inline-block">`Python`  | Super popular, widely taught, very natural programming language. Huge library of useful stuff. Downside: slow!   |
| <img src="/public/tools_numpy.avif" width="35px" style="display:inline-block"> | Highly optimized CPU-based math operations     |
| <img src="/public/tools_pandas.svg" width="45px" style="display:inline-block"> pandas    | Data exploration    |
| matplotlib    | Graphing    |
| <img src="/public/tools_pytorch.png" width="45px" style="display:inline-block"> pytorch    | GPU based math operations, NN specifics, automatic gradient calculations (it handles our calculus!) |
| Jupyter   | "Notebook" concept from laboratory,  More convenient than pure code |
|  <img src="/public/tools_colab.png" width="65px" style="display:inline-block"> Google Colab     | Free hosted Jupyter    |

</v-clicks>

---
---

# MNIST w/ dense NN
- https://github.com/mikeboensel/AI_Course/blob/main/slides/lecture1/_notebooks/mnist/mnist_pytorch.ipynb
- <a href="https://adamharley.com/nn_vis/">Incredible visualizations of MNIST Model</a>

<!-- NFL Draft modeling -- https://github.com/nflverse/nflverse-data/releases  https://www.pro-football-reference.com/draft/2002-combine.htm -->


---
---
# It's ovah!?!
- What you just learned, a Neural Net with Fully Connected, can learn anything
- So we're done, right? Pack it up, call it a day
- Theory is great in theory

<video width="320" height="240" controls style="margin-left:30%">
  <source src="/public/vince_carter_its_over.mp4" type="video/mp4">
</video>

---
---
# You need a budget
Potential limiting factors:
- Transistor count
- Training time
- Power usage
- Total data
  - We can only collect so much and want it to **generalize**
- Model size (parameter count)
- Etc.

<!-- ::right::
<img src="/public/you_need_a_budget.jpg" width="95%"> -->

---
---
# The importance of Datasets
- Collection/labeling of data is a very expensive endeavor
- Even collection of "unlabeled data" is expensive
    - Scraping, storage
- Having readily available datasets for different domains facilitates research
<div style="display:flex; justify-content: center;">
<img src="/public/datasets/mnist_overview.jpg" width="35%">
<img src="/public/datasets/imagenet_banner.jpg" width="35%">
<img src="/public/datasets/the_pile.png" width="30%">

</div>

---
layout: image-right
image: /public/elo_system.jpg
backgroundSize: "90%"
---
# What gets measured gets done
- Competitions encourage regular progress
- Contests around different datasets
- Metrics can be hard! Accuracy used to be enough
- Most of the progress recently has been in LLMs, more difficult to score/setup challenges
    - Interesting approach from <a href="https://arena.lmsys.org/"> Chatbot arena</a> 
    - ELO system and head to head contests

---
layout: image-right
image: /public/elo_system2.png
backgroundSize: "100%"
---
# Elo in detail
- TLDR; Beat higher rated opponents, move up quickly


<!-- Love a good inscrutable graph! It must be telling me something really important, let's stare at it until it gives up its secrets.
-->

---
layout: image
backgroundSize: "90%"
---
# Valuable Resources

- <a href="https://replicate.com/">"AI behind an API" - Replicate</a>
- <a href="https://huggingface.co/">AI's Github - HuggingFaces</a>
- <a href="https://civitai.com/models">Anything goes shitshow - Civit AI</a>


---
---
# Credits
- https://udlbook.github.io/udlbook/


<!-- 
If you asked me for one book recommendation, this would be it.

If you asked me for 2 book recommendations, I would recommend this one twice.
-->

---
---
# Future plans + my LinkedIn
- Expanding outward towards the Generative AI stuff (specifically self-hosted stuff)
- Every 3-4 weeks
- More speakers ("How to clean/process a 100TB ML dataset")

<div style="display:flex; justify-content: center;">
  <img src="/public/common_profile_pic.jpg" width="35%">
  <img src="/public/qr_code_linked_in.png" width="35%" style="margin-left:20%">
</div>

