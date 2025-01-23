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
sssssss

---
src: ./pages/what_is_ai.md
---

---
src: ./pages/sw_overlap_bouncer_ex.md
---

---
src: ./pages/key_ideas_of_ai.md
---
s
---
layout: center
---
# Neural Network Introduction

---
---
# Universal Approximation Theorem
  - Neural Networks can learn any f(x)

<v-click>
<img src="/public/trust_me_bro.jpg" width="50%"  style="margin-left:25%; margin-top:5%">
</v-click>


---
layout: image-right
image: /public/line_equation.jpg
backgroundSize: "85%"
---
# How?
<v-clicks depth="3">

- Remember lines from grade school math? That's 90% of what we're doing here. 
- Seems too simple? 
  - **We're going to use a lot of them!**

</v-clicks>
---

# Core operations
<v-clicks depth="3">

- Multiplication
- Addition
- 4 things that sound more complicated than they are:
  1. A non-linearity (aka `Activation f(x)`)
  2. High dimensionality
  3. Linear Algebra
  4. Calculus
<img src="/public/calculus.webp" width="30%">
</v-clicks>

<!--
We'll break this all down + you'll feel comfortable with it by the end
-->

---
layout: image-right
image: /public/nn_linear_fitting.jpg
backgroundSize: "95%"
---
# Let's talk about lines
- Given data we can fit a line to it
<img src="/public/line_equation.jpg" width="80%">
<a href="https://www.desmos.com/calculator">Desmos Graphing</a>
- What's a good fit? Something close to our data (define a Loss Function)
  - Adjust the line until we are happy



<!-- Our source of multiplications/additions
-->

---
layout: center
hide: False
---
# Great, but real life isn't a line! Its more complicated...

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
layout: image-right
image: /public/calculus/3D_Scatter_with_Colormap.png
backgroundSize: "95%"
---
# To infinity... and beyond!
- We are limited to 3 dimensions, but math is not
- Going to be using 100s of dimensions
- Each dimension is easy to view, but all of them together... impossible
  - <a href="https://www.desmos.com/3D">Desmos 3D Graphing</a>
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

<!--
Didn't even bother to mention in our
-->

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

# Wow, lots of math... must be important
Better learn what this is...

<div style="display:flex; justify-content: center; margin-bottom:10px">
<img src="/public/tensorflow.jpg" width="35%">
<img src="/public/tensor_TPU.jpg" width="25%" style="margin-left:20px">
</div>


<img src="/public/physics_envy.jpg">

<!--
Its a fancy word for a Matrix.

Theme of the talk: This is easier/more accessible than you think. Just using a ton of jargon.
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
- <a href="https://www.telesens.co/loss-landscape-viz/viewer.html">View more loss landscapes</a>

<!--
Loss landscape = How the Loss changes as we change our line segment fits

Seeing several popular Models with their loss visualized relative to the weights.

How? Thought this was thousands of dimensions? 
- Dimensionality reduction techniques. Lose some stuff, but can keep the general idea.
-->

---
---
# Our dream Loss Landscape 
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
layout: two-cols-header
---
# Calculus simplified

Simple concepts are taught poorly. Seem hard. Just trying to answer a simple question.

::left::
<v-click>
"Can you find the area?"
<img src="/public/calculus/area-of-a-Trapezoid.png" width="100%">
</v-click>

::right::
<v-click>
"How about now with a wiggly line?"
  <img src="/public/calculus/riemann_sum_convergence.png" width="75%" style="margin-left:15px">
  </v-click>


---
layout: two-cols-header
---
# Calculus simplified (cont.)

::left::
<v-click>
"Can you find the slope?"
<img src="/public/calculus/grad_descent_slope_calculation.jpg" width="80%">
</v-click>

::right::
<v-click>
"How about now with a wiggly line?"
<img src="/public/calculus/derivative.webp" style="margin-left:30px" width="100%">
</v-click>


---
---
# Why is this useful?
Allows us to answer:
- "How much is there?" 
- "How quickly is that amount changing?"
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

# Gradient Descent (in more detail)

<div style="display:flex; justify-content: center;">
<img src="/public/grad_descent/grad_descent_detailed.png" width="53%">
<!-- <img src="/public/grad_descent/grad_descent_slope_calculation.JPG" width="45%" style="margin-left:20px"> -->
</div>

<!--
Gradient - Just slope in many dimensions
-->

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
- All data is sparse at high dimensions
- Our toy graphs are not representative
<img src="/public/curse_of_dimensionality.png" width="100%">

- <a href="https://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/">Illustrated with Puppies!</a>

<!--
https://github.com/mikeboensel/AI_Course/blob/main/slides/lecture1/_notebooks/curse_of_dimensionality/dimensionality.ipynb

-->

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

<!--
No loss signal for any points w/o data (and most places don't have data), so any shape is equally valid! Not good!
-->

---
---
# Test/Validation/Train split
<img src="/public/test_train_validation_split.webp" width="100%">

- Will act to `Regularize` the Model's surface (make it smoother), but having high loss if we overfit vs the underlying distribution
  - Model should be fairly uncertain given the data sparsity


---
---
# Our toolbox
<v-clicks depth="2">

| Tool    | Description |
| -------- | ------- |
| <img src="/public/tools_python.png" width="30px" style="display:inline-block">`Python`  | Super popular, widely taught, very natural programming language. Huge library of useful stuff. Downside: slow!   |
| <img src="/public/tools_numpy.avif" width="35px" style="display:inline-block"> | Highly optimized CPU-based math operations     |
| PyTorch    | GPU based math operations, NN specifics, automatic gradient calculations (it handles our calculus!) |
| Jupyter   | "Notebook" concept from laboratory,  more convenient than pure code (Google Colab) |

</v-clicks>

---
---

# MNIST w/ dense NN
- You've all been very patient, now we finally deliver on our <a href="https://adamharley.com/nn_vis/mlp/3d.html">promise</a>

- <a href="https://github.com/mikeboensel/AI_Course/blob/main/slides/lecture1/_notebooks/mnist/mnist_pytorch.ipynb">MNIST Notebook</a>



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
layout: image
backgroundSize: "90%"
---
# How to get started in Generative AI
- <a href="https://chatgpt.com/">ChatGPT - Easy, low investment/high reward</a>
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

<div style="display:flex; justify-content: center;">
  <img src="/public/common_profile_pic.jpg" width="35%">
  <img src="/public/qr_code_linked_in.png" width="35%" style="margin-left:20%">
</div>

---
layout: image-right
image: /public/meetup_group.jpg
backgroundSize: "90%"
---
# The Meetup Group
<br>
<br>
<br>

<img src="/public/meetup_qr_code.jpg" width="35%" style="margin-left:20%">

https://www.meetup.com/boston-ai-ml-user-group/
