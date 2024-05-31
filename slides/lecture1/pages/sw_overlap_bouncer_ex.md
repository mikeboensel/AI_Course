---
layout: image-right
image: /public/job_training.jpg
---

# Common Sense isn't very common!
<v-clicks depth="3">

- Consider job training
  - Huge time/effort investment
  - A new hire is DRAMATICALLY smarter than a computer.

- Computers are dumb. 
  - Fast != Intelligence
  - Just follow instructions (SW)
    - SW is shit (state space modeling is challenging)
  - Equally happy to quickly shoot themselves in the foot repeatedly.

</v-clicks>

<!--
- Instructing them in the operation of the machine
  - As important is what he's not having to tell them
    - "This is a screen, it shows information. You can push buttons. Don't stick your hand in the hydraulic press"
    - People know a lot already
         - Intuitively (Stove is hot)
         - Schooling (At least 12 years)

Who has ever trained new employees?
- They get it right the first time?
- Can't have perfect instructions, have to just trust that they:
 - Are smart
 - Use good judgement
 - Figure it out

State space description is hard!
- May not even be able to describe (or know) how to find a solution.
-->

---
layout: image-right
image: /public/airline_announcement.jpg
---
# Fundamental problem of Engineering
<v-clicks depth="2">

1. The state space of the problem is huge.
2. Unlikely to anticipate all scenarios.
3. Unanticipated situations == disasters (Murphy's Law)
4. Especially difficult in SWE (non-linearity is everywhere)

</v-clicks>

<!-- 
The cartoon image on the right has never happened. It will never happen.

Consider what a plane is:
- A series of controlled explosions happen in a metal chamber so that a turbine rotates. This is all happening at 35,000. While you're going 500 mph. Its the only thing keeping you in a large metal tube.

We're fighting Thermodynamics
- States tend towards increasing entropy
- A plane is a state of high order!
  - Gets that way via:
    - Design
    - Precise manufacture
    - Regular maintenance
  - So much work!
  - Something goes wrong, it doesn't lead to an improvement.

Same thing in SW, but to a greater extent.
  - Non-linearity
  - Can test the weight a table can take by just measuring a couple points (400 lbs... 500lbs... breaks)
    - SW can't be sure about those intermediate points, could have crazy bad behavior based off conditional logic
-->

---
---
# I thought we were talking about AI/ML...
- Software Development is custom **function creation**.
<img src="/public/function_creator_1.webp" width="50%" style="margin-left:25%">

---
layout: image-right
image: "/public/robot_bouncer.webp"
---
# Bouncer example
<div v-click="+1">
Task: Don't allow anyone through the door unless they are of age.
</div>
<div v-click="+2">
Sounds simple. Let's formalize it:
```python
age = get_age(id_image)
if age >= 21:
  allow()
else:
  refuse()
```
</div>

<div v-click="+3">
<img src="/public/drivers_licence.webp" width="70%">
</div>
<div v-click="+4">
  12/1/1985 ✅
</div>
<div v-click="+5">
  5/22/2010 ❌
</div>


<!-- Heavily stylized for entertainment purposes. Might be something more like a kiosk that takes an ID, opens door if appropriate. 

Fairly low paying/low skill job.
-->

---
---
# Bouncer example gets hairier    
<v-clicks depth="2">

- Which IDs? <a href="https://www.businessinsider.com/what-drivers-license-looks-like-in-every-state">Other states?</a>
  - Where is DOB information? Left of label? Right? Above? 
  - Passports? Foreign IDs? God help us...

- Someone shows up with a 2 digit year `3/1/12`... 
  - Are they 12? <img src="/public/12_year_old.webp" width="10%" style="display:inline-block">
  - Or 112? <img src="/public/112_year_old.webp"  width="10%" style="display:inline-block">

- Not even touching on teenagers acting w/ malice...

</v-clicks>


<!--
All these will be required. 

Matt Levine: 
All large organizations have someone committing crime at a given time. That's different than being a criminal organization. How? Controls/making an attempt.

Real goal: sell as much alcohol as possible w/o legal problems.

Reasonable compliance: Not ever look in and have it look like there's a high school field trip.

So going to want to support a ton of different ID types because a default NO policy would be perfectly compliant, but no revenue. Shade toward being overly permissive.
-->

---
layout: center
---
# Tremendous amount of knowledge about the world must be encoded for this to succeed. 

# Many failure modalities!



---
layout: image
image: "/public/chatgpt_understands_memes_carpooling.JPG"
backgroundSize: "65%"

---
# Meanwhile... ChatGPT understand humor...

<!--
Think about all the Context and understanding you need of the world to understand this.

-->