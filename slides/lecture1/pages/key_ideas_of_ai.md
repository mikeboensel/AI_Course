---
layout: center
---
# If you had to pick 3 key ideas to explain ML...

<!-- Useful exercise. Can we condense this down to some central kernel?-->
---
layout: image-right
image: /public/functional_world.webp
---
# Key 1: The Universe is describable (aka has structure)
- The world is full of functions
- Neural Nets are f(x) approximators 
  - They just need data

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
---
# Functions can describe anything

A bunch of coaches with whistles and windblowers are trying to discover the next Tom Brady.
<div style="display:flex; justify-content: center;margin-top:5%">
<img src="/public/nfl_draft.webp" width="45%">
<img src="/public/nfl_draft.jpg" width="45%" style="margin-left:5%">
</div>

<!--
They may not even know how. 
- "My gut". 

But given inputs (combine numbers, physical attributes, years of college success, etc.) and results (# of Pro Bowls, years in the league) we can discover what matters.
-->

---
layout: center
---
# Another unexpected function (Inpainting)
<img src="/public/nn_as_functions3.jpg" width="95%">


<!-- 
If a human can do it, it can be solved algorithmically

Somewhat philosophical. 
- Some believe in some greater, undefined quantity ("spirit/essence"). - I think we're all bounded by the laws of nature and math. 
- Not really a provable point either way, just worth mentioning
-->

---
layout: image-right
image: /public/software2.0.webp
backgroundSize: "95%"
---

# Software 2.0
<img src="/public/andrej_karpathy.jpg" width="50%">

- <a href="https://karpathy.medium.com/software-2-0-a64152b37c35">Andrej Karpathy blog post</a>
  - Exploring a large State space
  - Anticipate different scenarios + respond intelligently

<!--
Andrej
- OpenAI
- TSLA director of AI
- Very influential "thought leader"
- Great teacher

Coined this term to describe a paradigm shift
-->

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

# Key 2: We can interpolate over this structure
- What is interpolation?
  - Start point -> End point in a space we performing a blending
<div grid="~ cols-2 gap-2" m="t-2">
<img src="/public/interpolation_linear.avif" width="80%">
<img src="/public/interpolation_rgb_color_wheel.jpg" width="60%" style="margin-left:30%">
</div>

<!--
Color space
We can transition between points
At every point we get a valid color

Ties into:
- Latent spaces/embeddings
  - Where I'm getting my AI images
- Model merging (a task dimension)
-->

---
---
# Interpolation Station
- Even things that might not seem interpolatable
    - <a href="https://thispersondoesnotexist.com/">Human faces</a>
    - Language concepts
    <img src="/public/king_queen_gender_vector.png" width="65%">

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
Hypothetical example:
- Capture the essence of people in some mathematical space
- Lebron James is basketball. 
- You might look at me and think "that guy probably played a long time ago for a little bit". 
- Yoyo Ma, famous cellist, you assume would explode if he ever touched a basketball.

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

<!--
Magnus Carlsen.
- Chess GOAT
- Wouldn't look at him and think "Yeah, but its checkers. I'll smoke him"
- Probably pretty good at any strategy type board game
-->

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
layout: image-right
image: /public/nn_layer_viz_chains.webp
backgroundSize: "75%"
---
# Key 3 (cont.)
- The <a href="https://towardsdatascience.com/how-to-visualize-convolutional-features-in-40-lines-of-code-70b7d87b0030">image domain</a> tends to be the most intuitive
  - But this is happening in all Models!
- Clearly these networks are learning complex shapes
- You can re-purpose these layers for other purposes



---
---
# Key Idea Summary
- There's an underlying structure to the universe that
    - Can be learned
    - Can be interpolated over
