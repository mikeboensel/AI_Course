---
layout: image-right
image: /public/job_training.jpg
---

# Common Sense isn't very common!
<v-clicks depth="3">

- Consider how much effort/time/expense goes into training a new hire. (A lot!)
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
# Fundamental problem of (Software) Engineering
- The state space under consideration for everything is big. 
- Unlikely:
  - To anticipate all scenarios
  - That unanticipated situations will be handled in a satisfactory way (Murphy's Law)

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

Same thing in SW

-->

---
---
# I thought we were talking about AI...
- Bear with me, on this sojourn into software. It will become obvious later why I'm equating the 2.
- The business of writing SW, is the business of custom **function creation**.
<img src="/public/function_creator_1.webp" width="50%" style="margin-left:25%">

---
layout: image-right
image: "/public/robot_bouncer.webp"
---
# Bouncer example
<v-clicks depth="3">

- Task: Don't allow anyone through the door unless they are of age.

- Sounds simple. Let's formalize it:
```python
age = get_age(id_image)
if age >= 21:
  allow()
else:
  refuse()
```
</v-clicks>

<div v-click="+2">
  <v-clicks>

  - <img src="/public/drivers_licence.webp" width="70%">
  - 12/1/1985 ✅
  - 5/22/2010 ❌
  </v-clicks>
</div>


<!-- Heavily stylized for entertainment purposes. Might be something more like a kiosk that takes an ID, opens door if appropriate. 
-->

---
---
# Bouncer example gets hairier    
<v-clicks depth="2">

- Which IDs? <a href="https://www.businessinsider.com/what-drivers-license-looks-like-in-every-state">Other states?</a>
  - Where is DOB information? Left of label? Right? Above? 
  - Passports? Foreign IDs? God help us...

- Someone shows up with a 2 digit year `3/1/12`... are they 112? Or 12? 

- We stop people from entering the door w/o checking ID
  - What about the window? Or another door? Task really doesn't just involve this door, more general security...

- Not even touching on teenagers acting w/ malice...

</v-clicks>

<div v-click>
<h2> Tremendous amount of knowledge about the world must be encoded for this to succeed. Many failure modalities!</h2>

</div>


<!--
All these will be required. 

Matt Levine: 
All large organizations have someone committing crime at a given time. That's different than being a criminal organization. How? Controls/making an attempt.

Real goal: sell as much alcohol as possible w/o legal problems.

Reasonable compliance: Not ever look in and have it look like there's a high school field trip.

So going to want to support a ton of different ID types because a default NO policy would be perfectly compliant, but no revenue. Shade toward being overly permissive.
-->
