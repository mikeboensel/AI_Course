
---
layout: center
---
# If you had to pick 3 key ideas to explain ML...

<!-- Useful exercise. Can we condense this down to some central kernel?-->
---
---
# Key 1: The world is full of f(x)'s and we can discover them
- Neural Nets are f(x) approximators and the world is full of functions
- <img src="/public/functional_world.webp" width="40%">

---
layout: two-cols-header
---
# What is a function?
Equation that takes an input and gives some output
::left::
<img src="/public/nn_as_functions.jpg" width="95%">
::right::
<img src="/public/nn_as_functions2.jpg" width="95%">

---
layout: two-cols-header
---
# f(x) cont.
Anything you can imagine
::left::
<img src="/public/nfl_draft.webp" width="95%">
::right::
<img src="/public/nfl_draft.jpg" width="95%">


---
layout: center
---
# f(x) cont.
<img src="/public/nn_as_functions3.jpg" width="95%">


<!-- If a human can do it, I take that as a prior indicating that it is a task that can be solved algorithmically (may not be able to state what the algo is, but it exists and can be discovered)
    - Somewhat philosophical. Some people believe in some greater, undefined quantity ("spirit/essence"). I don't. I think we're all bounded by the laws of nature and math. I can't prove it, but I've yet to see anyone prove the other case either. So that's my bias. You may not believe everything is this way, but I think we can agree most things are.
-->

---
---
# Software 2.0
- Andrej Karpathy blog post: https://karpathy.medium.com/software-2-0-a64152b37c35
- Highly related effort to what I've spent my career on (SW Dev)
  - Exploring a large State space
  - Attempting to anticipate different scenarios and respond intelligently
- <img src="/public/software2.0.webp" width="60%">

---
layout: image-right
image: /public/software2.0_2.webp
background-size: 90%
---
# Software 2.0 (cont.)
- 2.0 implies a replacement. 
- I'm less sure of that. 
- Certainly a different tool to have on your belt w/ radically different trade-offs.


---
hide: False
---
# Key 2: Deep underlying structure exists in the universe
- We can interpolate over this structure
  - What is interpolation?
    - Start point -> End point in a space we performing a blending
<div grid="~ cols-2 gap-2" m="t-2">
<img src="/public/interpolation_linear.avif" width="80%">
<img src="/public/interpolation_rgb_color_wheel.jpg" width="60%" style="margin-left:30%">
</div>
  

<!-- 
latent spaces/embeddings, model merging (a task dimension)
-->

---
---
# Interpolation Station
- Even things that might not seem interpolatable
    - Ex: human faces https://thispersondoesnotexist.com/


---
---
# Interpolation Station (cont.)
- Me vs Lebron James vs Yo-yo Ma

| Person    | Height | Level of Fame | Basketball-ness | 
| :--------: | :-------: | :-------: | :-------: | 
| <img src="/public/common_profile_pic.jpg" width="100px">  | 8 | 10 | 10 |
| <img src="/public/lebron_james.avif" width="100px"> | 6 | 0 | 3 |
| <img src="/public/yoyo_ma.jpg" width="100px">   | 4 | 6 | 0 |

- What are these dimensions?
<style>
  img{
  /* text-align:center; */
   margin-left:25%;
  }
</style>

<!--
Lebron James is basketball. You might look at me and think "that guy probably played a long time ago for a little bit". Yoyo ma you assume would explode if he ever touched one.

What are these dimensions? Unfortunately, rarely end up this clear cut in terms of "this dimension encodes this thing we understand".

 What range can they take? Lazily just put things on a 0-10 scale here. 
-->

---
layout: center
image: text-center
title: ENHANCE
---

<div style="text-align:center">
<span style="color:blue">ENHANCE!</span>

https://projector.tensorflow.org/
</div>

---
layout: two-cols-header
---
# Key 3: Subsequent learning is easier
- Intuitively makes sense to us.
::left::
<img src="/public/magnus_chess.jpeg" width="95%">
::right::
<img src="/public/checkerboard.jpg" width="95%">

---
---
# Key 3 (cont.)

- `Transfer learning`
- Learning just means discovering some underlying structure about the universe. 
- If you know some structure its easier to acquire others
- Baby (random unitialized) vs adult (existing skillset/knowledge)
<img src="/public/babies_learning.jpg" width="65%">

<!--
Antropomorphize with care... Useful analogies, but still just analogies
-->
---
---
# Key Idea Summary
- There's an underlying structure to the universe that
    - Can be learned
    - Can be interpolated over
