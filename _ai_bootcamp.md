# Sources to cite
- Jeremy Howard
- Jon K
- Sinan
- Andrew Ng
- Sebastian
- Many more I'm forgetting

# Misc Tools/Viz/Demos
- [TensorFlow Embedding Projector](https://projector.tensorflow.org/)

# General notes/intro to how I will teach
- Going to have a few areas where I just sum this up as "It philosophical", by which I mean I've yet to see a good answer and IMO, while its fun to debate, its ultimately just a way to pass time.
- Artificial Intelligence
  - Catch-all term. Machines did something useful. Ta-da, AI! In popular press, anything cutting edge. 
    - Generally there is a decay that happens as tasks become common-place and are not considered noteworthy anymore.
    - Arthur C Clarke: "Any sufficiently advanced tech is indistinguishable from magic". 
      - Would like to coin my own phrase: "Any tech, regardless of how advanced, becomes familiar and underappreciated with increasing use."
  - Spell checker. "Is it in the dictionary? No? Then present options for all words that contain the same set of letters". Not particularly intelligent, but doing something + useful.
  - AGI.
    - Ill defined. "What humans can do. Having agency. Etc."
    - My personal prediction, we'll see machines increasingly doing things that only we could do and keep moving the boundary line for this.
      - AI is threatening. We want to be unique + special.

- Going to consistently argue that there aren't many new ideas here, we keep calling things different names, but the underlying similarities are big

- Also going to be reductive at times. I'm an engineer, not a researcher. If a description gets 90% of the intuition and is much easier, I'm going with that. So just a heads up. 

- Want to both explain at a simple level to start, then get into details. 
  - Tough to serve both a general audience and practictioners, but if successful, results in a rich course that hopefully yields more insights as you re-watch.
    - Personal frustration about courses/learning. End up re-doing a lot. But you are not the same each time thru. Get more out of it (or can go thru faster/skipping or FF'ing)

- I'm going to ask for a show of hands at times ("How many people know about X") or if you ask me a question. Please participate in that and if you don't know things, don't feel embarassed and pressured to say you do. If its new, thats great, you're expanding what you know. That's admirable. What I'm trying to do is calibrate how much detail I need to give based off where people are. 
  - Want to avoid situations where I'm just talking and no one is getting anything from it, either because I'm going too slow or fast.

# Biological inspiration
- Tenuous at best. Not worth discussing. We aren't modeling the brain or really imitating it in any non-trivial way.

# Content
- What's possible?
  - Anything humans can do
  - Maybe more
  - Kind of a philosophical area, not going to debate it with anyone, know there are people out there who believe there's some intangible spirit that separates us from the rest of creation. I don't personally believe that. We're bound by math/physics like anything else. My brain is running some kind of function (hopefully a complex one). NN are function approximators. 
    - What's a function?
      - Formally: f(x) = x^2
        - Graph
      - Informally
        - Basketball example: Heuristic for drafting. Height is good. But there have been smaller guys. College performance is good too, but sometimes their game might not translate. Etc. Not a solved problem. Hard. Unclear what the right metrics are (even past performance, maybe an all-star for 5 years, then hits 30... how are they now?). Then sometimes it just comes down to "He feels like a good fit. Going with my gut!"
          - GOAT debate. Even applies across decades. Hear people arguing about whether someone who was a Hall of Famer in the 70s would even be able to make a team now.
          - Lot noisier, fuzzier, different for every person, changing over time (game has changed, more spread, someone like Shaq might struggle in today's 3 point game)
          - Classifier (NBA caliber? Or not?)
        - Humans are attracted to problems that are ill-defined, have no clear answer. We call them games
          - Chess, videogames, poker
            - Again, there's some function that would give ideal play. But its hard, which interests us.
          - Proposed other game
            - Tic tac toe, with a single box. Winner is whoever goes first.
      - Will see that recent advances in AI have taken us further into the fuzzy problems (like language). 

- What's needed? Only 3 things
  1. Data (labeled or unlabeled)
    - "Clean" (not noisy) helps a lot
  2. A defined structure (conducive to the task)
    - Almost always over-parameterized (many more params/dimensions than data points)
    - "Model capacity" = ability to learn
      - If the task is much smaller, we will learn a lot of extra stuff/overfit.
  3. Compute to run the structure
     - Priors or proper structure can reduce what is essentially a search problem down hugely. 

- Historical overview of the field
  - "This might take several months" (said in the 50s)
  - LeNET/MNIST
    - Feature creation, not feature engineering! Human priors help to reduce search size, but limit overall expressivity
    - Gradient Descent
  - Extreme dimensionality (thousands of dims, huge space)
  - AlexNET/ImageNet
    - Convolutions + GPU training
  - Transfer Learning
  - Latent Spaces
  - Image techniques for everything (audio)
  - GANs
    - https://thispersondoesnotexist.com/
  - Diffusion
    - Is it fair to say this is basically GANs w/ the generator/discrimator changed to a noise scheduler/noise predictor?
  - Sequence to sequence (translation)
    - LSTMs
    - Transformers
    - LLMs
      - Language understanding as the backbone for giving semantic understanding of the broader world

3 types of ML:
1. Supervised 
- Simplest conceptually. Very effective. 
- Needs labels, not great!
- Regression or Classification
  - Regression + cut-off can become a Classification
1. Unsupervised 
- No labels required. 
- [KMeans video](https://www.youtube.com/watch?v=5I3Ei69I40s) 
- (Fair to argue that most of the NLP advancement is just Clustering? The embeddings really are clustering in high dimensional space.)
- [Kmeans interactive](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
1. Reinforcement Learning 
- Super cool. Learn from environment 
- Sample inefficient. 
- Reward function very important. Sparsity of rewards (injection of human prior or not? Ex: Playing Go games where the only reward occurs if you win vs more incremental (which may lead to sub-optimal performance, but at lower compute costs (AlphaGo vs AlphaGo Zero))).
- Atari games mastered from pixels + scoore
- Robot arm farms video
- Heard compared to sprinkles on top of cake. Has some critical roles (alignment), but overall underperforming other areas IMO. 

- Feature engineering/Deep domain knowledge no longer important. Instead, ability to apply DL techniques.
  - Dataset is key! Expensive to assemble!
    - Language is the hack to get around this! Joint embedding/pre-training/transfer learning.
- [TF Playground very cool example (Jon K)](https://playground.tensorflow.org/#activation=relu&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=8,8,4,2&seed=0.32263&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
- [Fun, but less critical (Jon K) - Draw w/ Google](https://quickdraw.withgoogle.com/)
- Calculus - Just slope!
- Jeremy Howard interactive optimization demoo
- Visualizing the internal layers
  - Deep dream
  - Embeddings
    - Word2Vec
      - [Visualized](https://lamyiowce.github.io/word2viz/)
        - <img src="./imgs/ai_bootcamp/word2viz_prostitute.jpeg">
    - Modern embedding/RAG/Semantic Search

# Examples to do
- MNIST (Supervised)

# Frequently want to reduce down the dimensions of the input
- Makes for less compute, fewer parameters, easier training
- Max-pooling
- Strided convolutions

# Neuron Introduction
- Inputs
- Parameters
  - Weights (strengths we assign to each input)
  - Threshold for activation
    - Bias
## Activation f(x)s
- On/Off
  - Sharp, not smoothe, difficult to learn from
- Sigmoid/tanh
  - Smoothe, taper, but saturate at extremes
- ReLU
  - Simple, easier to compute derivatives of
  - 

# Beautiful infographic intro to ML
- http://www.r2d3.us/visual-intro-to-machine-learning-part-1/

# Stupid pet (training) tricks
- Normalizing inputs
  - Avoid exploding or disappearing gradients
- Dropout
- Normalizing intermediate layers
- Proper initialization

# Convolutions
- [Interactive Demo](https://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html)
- [DeepViz Toolkit showing filter activations](https://youtu.be/AgkfIQ4IGaM)

# Like the idea of a running list of things we've learned
- Some kind of table or visual overview to keep hitting on + adding to as we progress