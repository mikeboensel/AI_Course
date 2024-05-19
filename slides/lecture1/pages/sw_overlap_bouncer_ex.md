
---
---
# Common Sense isn't very common
- Instructing a machine is hard. Humans are bad at considering a state space or the algorithm they use to navigate it. May not even be able to describe (or know) how to find a solution.
- Consider how much effort/time/expense goes into training a new hire. Its a ton. 
- A new hire is DRAMATICALLY smarter than a computer. 
- Computers are dumb. Don't mistake working quickly with intelligence
- They're equally happy to quickly shoot themselves in the foot repeatedly.
- They do anything you instruct them to (regardless of consequences)

---
---
# Fundamental problem of Software Engineering
- The state space under consideration for everything is big. 
- Unlikely to anticipate it all.
- Unlikely that unanticipated situations will be handled in a satisfactory way (Murphy's Law)
  - >The airplane's control SW ran into an unexpected scenario. We're now going to be there 30 minutes earlier.
    - Has never happened.
  - <img src="/public/airline_announcement.webp" width="20%">

  - Most likely going to crash, because disorder is the fundamental state of the world


---
---
# I thought we were talking about AI...
- Bear with me, on this sojourn into software. It will become obvious later why I'm equating the 2.
- The business of writing SW, is the business of custom **function creation**.
<img src="/public/function_creator.webp" width="50%" style="margin-left:25%">

---
layout: image-right
image: "/public/robot_bouncer.webp"
---

# Bouncer example
- Task: Don't allow anyone through the door unless they are of age.
    - Sounds simple. Let's try to formalize it.
      - Don't let anyone thru the door if the date string on their driver's license doesn't indicate their age >= 21.
      - <img src="/public/drivers_licence.webp" width="70%">
    - 12/1/1985 ✅
    - 5/22/2010 ❌
---
---
# Bouncer example gets hairier    
- Which IDs? Other states? https://www.businessinsider.com/what-drivers-license-looks-like-in-every-state
  - Where to find the DOB information? Most call it `DOB`, but label might be above OR to the left of, or below
  - God help us... Passports? Foreign IDs?
- Someone shows up with a 2 digit year "3/1/12" are they 112? Or 12?
- We stop people from entering the door w/o checking ID
    - What about the window? Or another door? Task really doesn't just involve this door, more general security...
- Not even touching on teenagers acting w/ malice...
- Tremendous amount of knowledge about the world must be encoded for this to succeed. 
- Many failure modalities
