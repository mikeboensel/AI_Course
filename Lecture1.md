# "Where are we going?"
- Too often things are taught academically to be 100% technically accurate
    - Taught by people who are experts in the field. 
    - I have a different approach. Get 90% of the meaning. Fill it in later. Explain it in a way that rather than saying "Goddam that guy is smart" its more like "Why didn't I get into engineering. A monkey could do this". 
        - There is OFC more to this than I'm initially discussing, but I think its hugely helpful to start from a place of "Oh, ok, I get what you're doing and where you're going" vs "I don't know any of those words. I'm not even sure what the point of this is, I'm drowing in terminology"

- Motivating example
    - I'd argue a lot of the Math that we all learn through school is just about developing a numbering system and some basic operations around that.
    - Pretty good student. Better at math than most as I ended up going into engineering, which means to me I can talk with authority to anyone other than mathematicians and physicists.
        - Did not have good intuitions on any of this, just really good at applying mechanical processes that were drilled into me via worksheets/hw
            - Competitive streak + gamifying
    - Many of these concepts are bizarre! We forget how hard they were for us initially. Worth exploring.
    - About 10 years ago I went back to kindergarten math -> Calc 2 using Khan Academy
        - Seeing the whole picture (and knowing where we're going is hugely helpful, otherwise you're being led around by the nose)
    - So let's work through most of what we spent 8+ years of schooling learning,  starting with a # line:
        - <0-> 10 # line>
        - Counting (ok, makes sense, I have fingers. Eventually I can imagine that there are even things beyond what I can enumerate on my fingers)
            - A more general concept, a displacement from the origin (0)
            - Eventual expansion to large #s (beyond what we've seen in front of us). Millions of blocks. Ok. 
                - Then infinity
        - Addition (Just expanding on counting)
        - Subtraction (Removal from some quantity)
            - What happens if we go beyond what we have?
                - Negatives are weird. More so than we think.
                    - Easier for us to reason about due to debt. We can understand oweing someone money. 
                    - But none of us have ever seen a "negative thing"
                        - All in relation to some state. A proton is denoted as "positive". What's the inverse of that? A "negative". It makes sense to use this terminology since the 2 cancel out +1/-1. But again, there's not such thing as a "negative thing". But, its a useful concept of moving to the left on the # line
        - Is 1 the smallest unit of measure?
            - Seems dumb, mostly because we've all absorbed the abstract concept, but you can make arguments about fractions also being in relation to something and not really existing.
            - 1/2 Pizza - Abstract idea that there should be more there. There isn't. But there should be. Hence you have half.
            - Most things if you take half, a quarter, a tenth, you just have junk. Possibly unrecognizable junk depending on how it was split.
                - 1/10 of a car engine. Misc parts.
        - Multiplication
            - Like repeated addition
            - Scaling a displacement
            - What if we scaled by a # less than 1?
                - Division!
            - By a negative #?
                - Flip along the axis
        - Exponents
            - Scaling even harder
            - Doing this by a # < 1?
                - Square (or arbitrary n) root
            - What about w/ a # < 1?
                - Imaginary # (a half flip!)

    - Ok, but that's leaving off some subjects
        - Algebra
            - Introduce the concept of an unknown value. Useful for solving things like word problems.
            - Let's manipulate it to solve for unknowns
            - We know how to setup an equation, let's expand that to a function
            - Let's graph the function
            
        - Trig - Triangle tricks
            - Why?
            - We've dealth with a single point (a #). Dealth with 2 points (slope, distance, etc.). Triangle is what you get when you have 3 points, actually turns out to be hugely useful.
            - Circular movement modeled as 3 points (origin, x-offset, y-offset)
                - AC current (generators)
                    - So that's why sin/cos show up everywhere in electrical engineering
        - Calc
            - We know how to do area and slope for simple stuff like lines
                - What about wiggly lines that go on forever?
                - core concept, everything else is just cool tricks to get there (years of cool tricks)


# Course intro
- No one wants to look dumb and so we end up all talking past each other, minimizing learning
    - I think that's an impulse that we all need to make concious efforts to suppress... hence this series' title : Mr Big Brain's Super Duper AI Course


# What is AI?
- Nebulous term. Basically, "computer doing something useful". 
- Spellcheck
    - Not particularly smart. 
    - But at one time revolutionary.
        - Brings up another 
- Marketing term
    - Mentions of AI during investor conference calls
    - <img src="./imgs/earning_call_ai_mentions.png" height="300px">
- Umbrella term
    - <img src="./imgs/venn_diagram_ai.JPG" height="300px">
    - Machine Learning is what has generated all the interesting progress, that's what we'll focus on
        - `Learning from data examples`
            - Instructing a machine is hard. Humans are bad at considering a state space. May not even be able to describe (or know) how to find a solution.
                - Bouncer example.
                    - Task: Don't allow anyone through the door unless they are of age.
                        - Sounds simple (Gate access to one entry point, )
                        - What does that mean? People should be 18+ years old
                        - Which IDs? Other states? Passports? Foreign IDs? Driver's licences only?
                        - Where to find the DOB information?
                        - Someone shows up with a 2 digit year "12" are they 112? Or 12?
                        - Stop people from entering the door w/o checking ID
                            - What about the window?
                        - Tremendous amount of prior knowledge about the world must either be present, or accounted for by programmer. 
                        - Many failure modalities
                - House pricing example. 
                    - Many examples. Pricing + features. Something discoverable.

# Key ideas
    1. Neural Nets are f(x) approximators (that much is uncontroversial, but I'd go further and say they are "DISCOVERERS") and the world is full of functions
        - F(x) for pricing a house, picking an NBA draftee, writing a letter, even art
        - If a human can do it, I take that as a prior indicating that it is a task that can be solved algorithmically (may not be able to state what the algo is, but it exists and can be discovered)
            - Somewhat philosophical. Some people believe in some greater, undefined quantity ("spirit/essence"). I don't. I think we're all bounded by the laws of nature and math. I can't prove it, but I've yet to see anyone prove the other case either. So that's my bias. You may not believe everything is this way, but I think we can agree most things are.
    2. There's a deep underlying structure to the universe (latent spaces/embeddings, model merging, generative AI ability to interpolate)
        - Even things that might not seem interolatable
            - Ex: human faces "ThisPersonDoesNotExist.com"
    3. Once you've learned something its easier to learn other similar things
        - Intuitively makes sense to us. Magnus Carlsen - Chess. If I told you he was also really good at checkers, backgammon, etc. You'd be pretty accepting of it.
        - `Transfer learning` -- makes sense because learning just means discovering some underlying structure about the universe. If you know some, easier to acquire others (vs being random unitialized)
    So...
        - There's an underlying structure to the universe that
            - Can be learned
            - Can be interpolated over

# Sequence to Sequence
- RNNs
    - Going to look very impressive, but really a simple idea
        - Just a NN w/ one more group of inputs coming in (hidden state)
    - Backpropogation thru time
        - Wow, very impressive term. Time travel! 
    - Hard to make work, in theory it should, but many times what's theoretically possible isn't possible w/in compute/data limitations


# Transformers - The Quest for Context
- Sutter's Dismal Truth
- Easier to apply compute to both during Training (as its non-sequential), and inference (brute forcing the context summary)
- Sidesteps the difficulty around context summarization entirely
- Even tho its a more brute force method, efforts are being made to be as efficient as possible (mostly due to necessity, otherwise we top out in the low thousands) - KV Cache, Flash Attention, etc.
- Encoder/decoder


# LLMs
- pretraining embeds knowledge into the weights
- aligment still required, you don't end up with a chatbot out of the gate, just auto-complete (RLHF or something similar is needed)
## LLM Context Window tricks
- Family of methods that offer an alternative to training/finetuning to improve performance on specific tasks
- Few shot examples
- Chain of Thought (bootstrapping your own examples/self reinforcing context "I do th smallest chunk of work correctly and then build from there to a final answer")
- RAG injection of the answer for it to then synthesize a response
    - Semantic Search
    - Other methods of info retrieval (Knowledge Graph, DB)
- Prompt Engineering - The dumbest + least stable of them all


# Semantic Search/Doc Chunking
- Maybe the most impactful thing to come out of this

# Diffusion
- Denoising as a training example generator
- Guidance w/in a latent space via joint embeddings

# Basic Learning Loop
- Given some dataset, create a Model (computational graph of parameters/operations)
- Define a Loss (Obective) f(x)
- Via Calculus take small steps for each parameter to minimize this Loss f(x)
## Model Complexity
- Needs to be >= order of complexity of the underlying function
  - <Show underparameterized polynomial>
  - <Show overparameterized polynomial>
## Regularization

## Hyperparameters
- Were using polynomial, but in practice just use a bunch of Matrix Mults + non-linearities
  - <Find example of this visualized>


# The Semantic Breakthru
- Sequence-> Sequence
  - Machine Translation
- Discovery of Embeddings (language as Math)
- Pre-training tasks
  - Next word prediction
    - Richer than it seems (critics like to dismiss this "Its just picking the next word". Yes... But...)
      - King _______ was an David's father and a wise man.
      - Portland is in _______. It's precise long/lat are .... (Many Portlands. Have to learn to distinguish from Oregon given context. Not easy!)
        - <img src="./imgs/portlands_of_the_us.jpeg" height="300px">
        - <img src="./imgs/portlands_of_the_us2.jpeg" height="300px">


## Bootstrapping into other Domains
- Contrastive Learning approaches (CLIP)
  - Given a Language Model (which has deep understanding of concepts) we can expand into areas like Images
  - Internet images have `alt` text that provides a (normally poor) description.
    - We have our langugage prior. We know where that maps in the Language Domain. Bring the 2 Domains together in a joint embedding. Now we can describe images.

# Transformers - The Quest for Context! (Lamest Michael Bay movie you will ever see)
- `Context Window` - What can I take into account when making my decision at time t?
  - Technical note: Window will only include past events when doing Inference, may include future as well when doing Training/PreTraining
- RNNs try to maintain Context via a Hidden State computed at each step
- Lazy approach, just have all Context available at all times (computationally much more expensive, approaches are moving back toward Hidden State, but currently this just works so well)
  - "here's a summary" vs "Here's everything that's happened to this point"
  -  constant vs Quadratic complexity
  - Unlimited range vs limited (altho increasing! Google advertising 1M Token Context Window)

# Misc
Graph - need to keep in mind what this represents (infinite resolution). Reality is limited sampling, which may not be representative


Over time some things `Drift`
- Gravity - pretty constant
- Housing prices - phase shift from 2007-> 2009