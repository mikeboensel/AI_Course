---
layout: image
image: /public/DartmouthWorkshop.JPG
backgroundSize: "50%"
---
# What is AI?
Coined in the 50s, at a Dartmouth Summer Workshop

<!--
You look at a picture like this:
- B/W old guys in suits
OFC these are the august genius who started this. That's Claude Shannon, mathematical demi-god.
Which is why I included the next slide:

-->

---
layout: image
image: /public/DartmouthWorkshop2.JPG
backgroundSize: "55%"
---
# Just another day at Summer Camp

<style>
  h1{text-align:center;}
</style>

<!--
At one point just a bunch of geeky looking people running around Harvard.
-->

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
image: /public/HistoryOfAI-Annotated.JPG
backgroundSize: "75%"
---

---
layout: image
image: /public/venn_diagram_ai.JPG
backgroundSize: "83%"
---
# Umbrella term

<!-- Inner elements are normally some mix of: 
- Stats
- Computer Science
- Machine Learning
- Neural Networks
- Deep Learning
- "Big Data"
- Data Science
A fair amount of these terms are themselves vague catch-alls.
-->

---
---
# In practice: AI is "the new hotness"
- A way to juice your stock price. 
- Mentions of AI during investor conference calls:
<img src="/public/earning_call_ai_mentions.png" height="300px">

---
---
# A moving target
- Basically, **a computer doing something useful and impressive**.
- Ex: Spellcheck, probably revolutionary when initially released. Now, not so much.
- <img src="/public/spellcheck.JPG" width="70%">

<!--
Simple enough algo:
- For each word
- Check if in dictionary
- If not, add a red squiggle below
BONUS: Add suggestions on hover via something like nearest Levenstein distance
  - The # of single-character edits (insertions, deletions or substitutions) required to change one word into the other. 

Intentionally picked something that the audience would find trite to make a point. 
- Been in this field a while, I can remember things that blew my mind at the time:
  - Google auto-complete
  - GMail updating w/o page refreshes (AJAX)
- All common place/unexceptional now. Revolutionary at the time. This is the course of all technology

-->

---
---
# Clarke's Law

> Any sufficiently advanced tech is indistinguishable from magic

<div style="display:flex;justify-content: space-around;">
    <img src="/public/arthur_c_clark2.jpg" width="30%" style="margin:auto">
    <img src="/public/arthur_c_clark.jpg" width="20%" style="margin:auto">
</div>

---
layout: center
---
# Any tech, regardless of how advanced, becomes familiar and underappreciated with increasing use!
<!-- I'd like to propose my own Law.

Falls out naturally from human nature. -->

---
src: ./hedonic_treadmill.md
hide: false
---

---
hide: false
---
# We will focus on Machine Learning
- AI is a buzzword
- ML has been the main driver of recent progress.
- Best simple definition: 
    - ### Learning an underlying structure from limited data examples

Let's examine why this is interesting