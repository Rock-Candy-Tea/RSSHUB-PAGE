
---
title: """""""""'Learning to Summarize with Human Feedback'"""""""""
categories: 
    - 新媒体
    - OpenAI - Blog
author: OpenAI - Blog
comments: false
date: Fri, 04 Sep 2020 00:00:00 GMT
thumbnail: 'https://cdn.openai.com/learning-to-summarize-with-human-feedback/assets/approach.svg'
---

<div>   
<div class="js-excerpt">
<p>We've applied reinforcement learning from human feedback to train language models that are better at summarization. Our models generate summaries that are better than summaries from 10x larger models trained only with supervised learning. Even though we train our models on the Reddit TL;DR dataset,<span class="js-rfref" data-id="tldr-dataset"></span> the same models transfer to generate good summaries of CNN/DailyMail news articles<span class="js-rfref" data-id="cnndm"></span> without any further fine-tuning. Our techniques are not specific to summarization; in the long run, our goal is to make aligning AI systems with human preferences a central component of AI research and deployment in many domains.</p>
</div>
<section class="btns">
<a href="https://arxiv.org/abs/2009.01325" class="btn btn-padded icon-paper">Read paper</a><a href="https://github.com/openai/summarize-from-feedback" class="btn btn-padded icon-code">View code</a><a href="https://openaipublic.blob.core.windows.net/summarize-from-feedback/website/index.html" class="btn btn-padded icon-layers">View samples</a>
</section>
<div class="my-2" id="fig1">
<h5 class="medium-small-copy">Human feedback models outperform much larger supervised models and reference summaries on TL;DR</h5>
<div id="chart-tldr" class="mt-0.5"></div>
<div class="caption mt-0">Figure 1: The performance of various training procedures for different model sizes. Model performance is measured by how often summaries from that model are preferred to the human-written reference summaries. Our pre-trained models are early versions of GPT-3, our supervised baselines were fine-tuned to predict 117K human-written TL;DRs, and our human feedback models are additionally fine-tuned on a dataset of about 65K summary comparisons.</div>
</div>
<div class="full d-none d-md-block"><hr class="my-0"></div>
<hr class="d-md-none">

<hr class="d-md-none">
<p>Large-scale language models are becoming increasingly capable on NLP tasks. These models are usually trained with the objective of next word prediction on a dataset of human-written text. But this objective doesn’t capture exactly what we want; usually, we don’t want our models to imitate humans, we want them to give high-quality answers. This mismatch is clear when a model is trained to imitate low-quality human-written text, but it can also happen in more subtle ways. For example, a model trained to predict what a human would say might make up facts when it is unsure, or generate sentences reflecting harmful social bias, both failure modes that have been well-documented.<span class="js-rfref" data-id="lying"></span><span class="js-rfref" data-id="bias1"></span><span class="js-rfref" data-id="bias2"></span><span class="js-rfref" data-id="bias3"></span></p>
<p>As part of our work on safety, we want to develop techniques that align our models’ objectives with the end behavior we really care about. As our models become more powerful, we believe aligning them with our goals will be very important to ensure they are beneficial for humans. In the short term, we wanted to test if human feedback techniques could help our models improve performance on useful tasks.</p>
<p>We focused on English text summarization, as it's a challenging problem where the notion of what makes a “good summary” is difficult to capture without human input. We apply our method primarily to an existing dataset<span class="js-rfref" data-id="tldr-dataset"></span> of posts submitted to the social network Reddit<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn1" id="fnref1">[1]</a></sup> together with human-written “TL;DRs,” which are short summaries written by the original poster.</p>
<p>We first train a reward model via supervised learning to predict which summaries humans will prefer.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn2" id="fnref2">[2]</a></sup> We then fine-tune a language model with reinforcement learning (RL) to produce summaries that score highly according to that reward model. We find that this significantly improves the quality of the summaries, as evaluated by humans, even on datasets very different from the one used for fine-tuning.</p>
<p>Our approach follows directly from <a href="https://openai.com/blog/fine-tuning-gpt-2/">our previous work</a> on learning from human feedback.<span class="js-rfref" data-id="ziegler"></span> There has also been other work on using human feedback to train summarization models.<span class="js-rfref" data-id="bohm"></span> We push the technique further by scaling to larger models, collecting more feedback data, closely monitoring researcher-labeler agreement, and providing frequent feedback to labelers. Human feedback has also been used to train models in several other domains, such as dialogue,<span class="js-rfref" data-id="dialogue1"></span><span class="js-rfref" data-id="dialogue2"></span><span class="js-rfref" data-id="dialogue3"></span> semantic parsing,<span class="js-rfref" data-id="semantic-parsing"></span> translation,<span class="js-rfref" data-id="translation1"></span><span class="js-rfref" data-id="translation2"></span> story<span class="js-rfref" data-id="story"></span> and review<span class="js-rfref" data-id="review"></span> generation, evidence extraction,<span class="js-rfref" data-id="evidence"></span> and more traditional RL tasks.<span class="js-rfref" data-id="rl1"></span><span class="js-rfref" data-id="rl2"></span></p>
<h2 id="results">Results</h2>
<!-- start #tldr-samples -->
<div id="tldr-samples" class="full mt-2 py-0.5 position-relative" style="background-color:var(--color-hf-bg)">
<div class="samples-nav sticky js-sticky" style="background-color:var(--color-hf-bg);visibility:hidden;pointer-events:none" id="tldr-navigate">
  <div class="container">
    <div class="samples-nav-inner d-flex justify-content-between align-items-center">
      <button class="prev-next-button small-caps faded-light btn p-1 m-n1" onclick="navigateSample('tldr-samples', 'prev')" style="pointer-events:auto">
        <div class="pl-7/12 ml-n0.2 position-relative">
          <span class="icon font-small position-absolute" style="top:-3px;left:-2px">previous</span>Prev
        </div>
      </button>
      <button class="prev-next-button small-caps faded-light btn p-1 m-n1" onclick="navigateSample('tldr-samples', 'next')" style="pointer-events:auto">
        <div class="pr-7/12 mr-n0.2 position-relative">
          <span class="icon font-small position-absolute" style="top:-3px;right:-2px">next</span>Next
        </div>
      </button>
    </div>
  </div>
</div>
<div class="samples-nav-after py-2.5">
<div class="container">
<div class="row">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Post from Reddit (r/<span data-sample-id="tldr-site"></span>)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div data-sample-id="tldr-title" class="medium-small-copy font-bold mb-0.5"></div>
  <div class="js-truncate medium-small-copy"><div data-sample-id="tldr-context"></div><span class="js-more">show more</span></div>
  <hr>
</div>
</div>
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Human-written reference summary</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px dotted var(--color-hf-neutral)">
    <div class="medium-small-copy" data-sample-id="tldr-ref"></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg font-bold text-xl-right mt-0.125 mb-1/3 balance-text">Human feedback 6B model</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-human)">
    <div class="medium-small-copy"><samp data-sample-id="tldr-human"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Supervised 6B model</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-supervised)">
    <div class="medium-small-copy"><samp data-sample-id="tldr-supervised"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Pre-trained 6B model</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-pretrained)">
    <div class="medium-small-copy"><samp data-sample-id="tldr-pre-trained"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
</div>
</div><!-- end container -->
</div><!-- end #tldr-samples -->
<p>We evaluated several different summarization models—some pre-trained on a broad distribution of text from the internet, some fine-tuned via supervised learning to predict TL;DRs, and some fine-tuned using human feedback.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn3" id="fnref3">[3]</a></sup> To evaluate each model, we had it summarize posts from the validation set and asked humans to compare their summaries to the human-written TL;DR. The results are shown in <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fig1">Figure 1</a>.</p>
<p>We found that RL fine-tuning with human feedback had a very large effect on quality compared to  both supervised fine-tuning and scaling up model size. In particular, our 1.3 billion parameter (1.3B) model trained with human feedback outperforms our 12B model trained only with supervised learning. Summaries from both our 1.3B and 6.7B human feedback models are preferred by our labelers to the original human-written TL;DRs in the dataset.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn4" id="fnref4">[4]</a></sup></p>
<p>People make different trade-offs when writing summaries, including between conciseness and coverage of the original text; depending on the purpose of the summary, different summary lengths might be preferred. Our labelers tended to prefer longer summaries, so our models adapted to that preference and converged to the longest allowable length. Controlling for length reduced human preferences for our 6.7B model’s summaries from 70% to 65%, explaining a minority of our gains.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn5" id="fnref5">[5]</a></sup></p>
<h2 id="transferresults">Transfer results</h2>
<h5 class="medium-small-copy">Human feedback models trained on Reddit transfer to generate excellent summaries of CNN/DM news articles without further training</h5>
<div class="clearfix mt-1 mb-0.5">
<div class="switch" style="max-width:22rem">
  <input type="radio" class="switch-input" name="switch-continuation" value="size-switch" id="size-switch" onclick="toggle(['size'], ['length'])" checked>
  <label for="size-switch" class="switch-label switch-label-off small-copy">Raw scores</label>
  <input type="radio" class="switch-input" name="switch-continuation" value="length-switch" id="length-switch" onclick="toggle(['length'], ['size'])">
  <label for="length-switch" class="switch-label switch-label-on small-copy">Length-controlled</label>
  <span class="switch-selection"></span>
</div>
</div>
<div class="position-relative">
<div id="size">
<div id="chart-cnndm"></div>
<div class="caption mt-0">
<p>The performance (human-rated summary quality on a 1–7 scale) of various training procedures and model sizes.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn6" id="fnref6">[6]</a></sup> Note that our human feedback models generate summaries that are significantly shorter than summaries from models trained on CNN/DM.</p>
</div>
</div>
<div id="length" class="position-absolute w-100 trbl-0" style="opacity:0;visibility:hidden">
<div id="chart-cnndm-length"></div>
<div class="caption mt-0">
<p>At a given summary length, our 6.7B human feedback model trained on Reddit performs almost as well as a fine-tuned 11B T5 model, despite not being re-trained on CNN/DM.</p>
</div>
</div>
</div>
<!-- start #cnndm-samples -->
<div id="cnndm-samples" class="full py-0.5 position-relative" style="background-color:var(--color-hf-bg)">
<div class="samples-nav sticky js-sticky" style="background-color:var(--color-hf-bg);visibility:hidden;pointer-events:none" id="cnndm-navigate">
  <div class="container">
    <div class="samples-nav-inner d-flex justify-content-between align-items-center">
      <button class="prev-next-button small-caps faded-light btn p-1 m-n1" onclick="navigateSample('cnndm-samples', 'prev')" style="pointer-events:auto">
        <div class="pl-7/12 ml-n0.2 position-relative">
          <span class="icon font-small position-absolute" style="top:-3px;left:-2px">previous</span>Prev
        </div>
      </button>
      <button class="prev-next-button small-caps faded-light btn p-1 m-n1" onclick="navigateSample('cnndm-samples', 'next')" style="pointer-events:auto">
        <div class="pr-7/12 mr-n0.2 position-relative">
          <span class="icon font-small position-absolute" style="top:-3px;right:-2px">next</span>Next
        </div>
      </button>
    </div>
  </div>
</div>
<div class="samples-nav-after py-2.5">
<div class="container">
<div class="row">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Article from CNN/DM (<span data-sample-id="cnndm-site"></span>)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div data-sample-id="cnndm-title" class="medium-small-copy font-bold mb-0.5"></div>
  <div class="js-truncate medium-small-copy"><div data-sample-id="cnndm-context" class="medium-small-copy"></div><span class="js-more">show more</span></div>
  <hr>
</div>
</div>
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Human-written reference summary</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px dotted var(--color-hf-neutral)">
    <div class="medium-small-copy" data-sample-id="cnndm-ref"></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg font-bold text-xl-right mt-0.125 mb-1/3 balance-text">Human feedback 6B model (transfer)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-human)">
    <div class="medium-small-copy"><samp data-sample-id="cnndm-human-transfer"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Supervised 6B model (transfer)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-supervised)">
    <div class="medium-small-copy"><samp data-sample-id="cnndm-supervised-transfer"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Pre-trained 6B model</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-pretrained)">
    <div class="medium-small-copy"><samp data-sample-id="cnndm-pre-trained"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">T5 11B model (fine-tuned on CNN/DM)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-t5)">
    <div class="medium-small-copy"><samp data-sample-id="cnndm-t5"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Supervised 6B model (fine-tuned on CNN/DM)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-hf-neutral)">
    <div class="medium-small-copy"><samp data-sample-id="cnndm-supervised"></samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
</div>
</div><!-- end container -->
</div><!-- end #cnndm-samples -->
<p>To test our models' generalization, we also applied them directly to the popular CNN/DM news dataset.<span class="js-rfref" data-id="cnndm"></span> These articles are more than twice as long as Reddit posts and are written in a very different style. Our models have seen news articles during pre-training, but all of our human data and RL fine-tuning was on the Reddit TL;DR dataset.</p>
<p>This time we evaluated our models by asking our labelers to rate them on a scale from 1–7.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn7" id="fnref7">[7]</a></sup> We discovered that our human feedback models transfer to generate excellent short summaries of news articles without any training. When controlling for summary length, our 6.7B human feedback model generates summaries that are rated higher than the CNN/DM reference summaries written by humans. This suggests that our human feedback models have learned something more general about how to summarize text, and are not specific to Reddit posts.</p>
<h2 id="approach">Approach</h2>
<div class="wide mt-1.5 mb-0">
<div class="mx-xl-auto" style="max-width:1000px">
<img src="https://cdn.openai.com/learning-to-summarize-with-human-feedback/assets/approach.svg" referrerpolicy="no-referrer">
</div>
</div>
<div class="caption mt-0 mb-1.5">A diagram of our method, which is similar to the one used in our previous work.<span class="js-rfref" data-id="ziegler"></span></div>
<p>Our core method consists of four steps: training an initial summarization model, assembling a dataset of human comparisons between summaries, training a reward model to predict the human-preferred summary, and then fine-tuning our summarization models with RL to get a high reward.</p>
<p>We trained several supervised baselines by starting from GPT-style transformer models trained on text from the Internet,<span class="js-rfref" data-id="gpt3"></span> and fine-tuning them to predict the human-written TL;DR via supervised learning. We mainly use models with 1.3 and 6.7 billion parameters. As a sanity check, we confirmed that this training procedure led to competitive results<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn8" id="fnref8">[8]</a></sup> on the CNN/DM dataset.</p>
<p>We then collected a dataset of human quality judgments. For each judgment, a human compares two summaries of a given post and picks the one they think is better.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn9" id="fnref9">[9]</a></sup>  We use this data to train a reward model that maps a <em>(post, summary)</em> pair to a reward <em>r</em>. The reward model is trained to predict which summary a human will prefer, using the rewards as logits.</p>
<p>Finally, we optimize the policy against the reward model using RL. We use <a href="https://openai.com/blog/openai-baselines-ppo/">PPO</a> with 1 million episodes in total, where each episode consists of the policy summarizing a single article and then receiving a reward <em>r</em>. We include a KL penalty that incentivizes the policy to remain close to the supervised initialization.</p>
<h2 id="collectingdatafromhumans">Collecting data from humans</h2>
<p>Any training procedure that uses human feedback is directly influenced by the actual humans labeling the data. In our previous work on fine-tuning language models from human preferences,<span class="js-rfref" data-id="ziegler"></span> our labelers often gave high ratings to summaries we thought were average, which was reflected in the quality of our trained models.</p>
<p>In response, in this project we invested heavily in ensuring high data quality. We hired about 80 contractors using third-party vendor sites,<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn10" id="fnref10">[10]</a></sup> and paid them an hourly wage regardless of the number of summaries evaluated.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn11" id="fnref11">[11]</a></sup> Hiring contractors rather than relying on crowdsourcing websites allowed us to maintain a hands-on relationship with labelers: we created an onboarding process, developed a website with a customizable labeler interface, answered  questions in a shared chat room, and had one-on-one video calls with labelers. We also made sure to clearly communicate our definition of summary quality, after spending significant time reading summaries ourselves, and we carefully monitored agreement rates between us and labelers throughout the project.</p>
<h2 id="optimizingtherewardmodel">Optimizing the reward model</h2>
<h5 class="medium-small-copy">Optimizing our reward model eventually leads to sample quality degradation</h5>
<div id="chart-optim" class="mt-0.5">
</div>
<div class="caption mt-0">
<p>Starting from the 1.3B supervised baseline (point 0 on the x-axis), we use RL to optimize the policy against the reward model, which results in policies with different “distances” from the baseline (x-axis, measured using the KL divergence from the supervised baseline). Optimizing against the reward model initially improves summaries according to humans, but eventually overfits, giving worse summaries. This chart uses an older version of our reward model, which is why the peak of the reward model is less than 0.5. <!-- [^oldermodel] --></p>
</div>
<!-- [^oldermodel]:
     This graph uses an older version of our reward model, which is why the peak of the reward model is less than 0.5.  -->
<!-- start #optim-samples -->
<div id="optim-samples" class="full py-3" style="background-color:var(--color-hf-bg)">
<div class="container">
<div class="row">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">Post from Reddit (r/AskReddit)</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
<div class="medium-small-copy font-bold mb-0.5">I'm a 28yo man, and I would like to get into gymnastics for the first time.</div>
<div class="medium-small-copy">
<p>Title said just about all of it. I'm 28, very athletic (bike/ surf/ snowboard) and I have always wanted to do gymnastics.</p>
<p>I like to do flips and spins off bridges and on my snowboard, and it seems to me gymnastics would be a great way to do those movements I like, in a controlled environment.  The end goal of this is that it would be fun, and make me better at these movements in real life.</p>
<p>But is it too late for me?  Should 28 year old guys such as myself be content with just watching those parkour guys on youtube? Or can I learn the ways of the gymnastic jedi?  BTW, I live in San Jose CA.</p>
</div>
<hr>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">KL = 0</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-human)">
    <div class="medium-small-copy"><samp>I want to do gymnastics, but I'm 28 yrs old.  Is it too late for me to be a gymnaste?!</samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row mb-1">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">KL = 9</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-human)">
    <div class="medium-small-copy"><samp>28yo guy would like to get into gymnastics for the first time.  Is it too late for me given I live in San Jose CA?</samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
<div class="row">
<div class="col-12 col-xl-2 offset-xl-1">
  <div class="small-copy color-fg-60 text-xl-right mt-0.125 mb-1/3 balance-text">KL = 260</div>
</div>
<div class="col-12 col-md-9 col-lg-8 col-xl-6">
  <div class="pl-0.5" style="border-left:2px solid var(--color-human)">
    <div class="medium-small-copy"><samp>28yo dude stubbornly postponees start pursuing gymnastics hobby citing logistics reasons despite obvious interest??? negatively effecting long term fitness progress both personally and academically thoght wise? want change this dumbass shitty ass policy pls</samp></div>
  </div>
</div><!-- end col -->
</div><!-- end row -->
</div><!-- end container -->
</div><!-- end #optim-samples -->
<p>Optimizing  against  our  reward  model  is supposed to make our policy align with human preferences.  But the reward model is only a proxy for human preferences, as it only sees a small amount of comparison data from a narrow distribution of summaries. While the reward model performs well on the kinds of summaries it was trained on, we wanted to know how much we could optimize against it until it started giving useless evaluations.</p>
<p>We trained policies at different “optimization strengths” against the reward model, and asked our labelers to evaluate the summaries from these models. We did this by varying the KL coefficient, which trades off the incentive to get a higher reward against the incentive to remain close to the initial supervised policy. We found the best samples had roughly the same predicted reward as the 99th percentile of reference summaries from the dataset. Eventually optimizing the reward model actually makes things worse.</p>
<h2 id="limitations">Limitations</h2>
<p>If we have a well-defined notion of the desired behavior for a model, our method of training from human feedback allows us to optimize for this behavior. However, this is not a method for determining what the desired model behavior <em>should be</em>. Deciding what makes a good summary is fairly straightforward, but doing this for tasks with more complex objectives, where different humans might disagree on the correct model behavior, will require significant care. In these cases, it is likely not appropriate to use researcher labels as the “gold standard”; rather, individuals from groups that will be impacted by the technology should be included in the process to define “good” behavior, and hired as labelers to reinforce this behavior in the model.</p>
<p>We trained on the Reddit TL;DR dataset<span class="js-rfref" data-id="tldr-dataset"></span> because the summarization task is significantly more challenging than on CNN/DM. However, since the dataset consists of user-submitted posts with minimal moderation, they sometimes contain content that is offensive or reflects harmful social biases. This means our models can generate biased or offensive summaries, as they have been trained to summarize such content.</p>
<p>Part of our success involves scaling up our reward model and policy size. This requires a large amount of compute, which is not available to all researchers: notably, fine-tuning our 6.7B model with RL required about 320 GPU-days. However, since smaller models trained with human feedback can exceed the performance of much larger models, our procedure is more cost-effective than simply scaling up for training high-quality models on specific tasks.</p>
<p>Though we outperform the human-written reference summaries on TL;DR, our models have likely not reached human-level performance, as the reference summary baselines for TL;DR and CNN/DM are not the highest possible quality. When evaluating our model’s TL;DR summaries on a 7-point scale along several axes of quality (<em>accuracy</em>, <em>coverage</em>, <em>coherence</em>, and <em>overall</em>), labelers find our models can still generate inaccurate summaries, and give a perfect <em>overall</em> score 45% of the time.<sup class="footnote-ref"><a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fn12" id="fnref12">[12]</a></sup> For cost reasons, we also do not directly compare to using a similar budget to collect high-quality demonstrations, and training on those using standard supervised fine-tuning.</p>
<h2 id="futuredirections">Future directions</h2>
<p>We’re interested in scaling human feedback to tasks where humans can’t easily evaluate the quality of model outputs. For example, we might want our models to answer questions that would take humans a lot of research to verify; getting enough human evaluations to train our models this way would take a long time. One approach to tackle this problem is to give humans tools to help them evaluate more quickly and accurately. If these tools use ML, we can also improve them with human feedback, which could allow humans to accurately evaluate model outputs for increasingly complicated tasks.<span class="js-rfref" data-id="amplification"></span></p>
<p>In addition to tackling harder problems, we're also exploring different types of feedback beyond binary comparisons: we can ask humans to provide demonstrations, edit model outputs to make them better, or give explanations as to why one model output is better than another. We'd like to figure out which kinds of feedback are most effective for training models that are aligned with human preferences.</p>
<p>If you are interested in working on these research questions, <a href="https://openai.com/jobs">we’re hiring</a>!</p>
<footer class="post-footer js-post-footer">
<!-- footer item -->
<div><hr><div class="row" id="acknowledgments">
<div class="col">Acknowledgments</div>
<div class="col">
<p>We'd like to thank the following people who gave feedback on various iterations of the blog post: Douwe Kiela, Zach Lipton, Alex Irpan, Jack Clark, Jacob Hilton, Raul Puri, Miles Brundage, Greg Brockman, Ilya Sutskever, Kelly Sims, Wojciech Kryscinski, and Dzimitry Bahdanau. We'd also like to thank Justin Jay Wang for driving the blog post design, Ashley Pilipiszyn for editing, Alec Radford and Dario Amodei for guidance on the project, Shan Carter for help designing the main diagram, Gretchen Krueger for co-writing the model card, Beth Barnes for help with labeler hiring and general encouragement, and many other people at OpenAI for training our large pre-trained models, supporting us through computing infrastructure improvements and maintenance, and writing fast GPU kernels. Finally, we'd like to thank all of our contractors for providing the data that was essential for training the models in this post.</p>
</div>
</div></div>
<!-- references footer item -->
<div data-order="-1"><hr><div class="row" id="references">
<div class="col">References</div>
<div class="col">
<ol>
<li class="js-ref" data-id="tldr-dataset">
Völske, M., Potthast, M., Syed, S., & Stein, B. (2017). "<a href="https://www.aclweb.org/anthology/W17-4508.pdf">TL; DR: Mining reddit to learn automatic summarization</a>." In Proceedings of the Workshop on New Frontiers in Summarization 2017.
</li>
<li class="js-ref" data-id="cnndm">
Hermann, K. M., Kocisky, T., Grefenstette, E., Espeholt, L., Kay, W., Suleyman, M., & Blunsom, P. (2015). "<a href="https://arxiv.org/abs/2005.14165"> Teaching machines to read and comprehend</a>." In Advances in neural information processing systems 2015.
</li>
<li class="js-ref" data-id="lying">
Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). "<a href="https://arxiv.org/abs/2005.00661">On Faithfulness and Factuality in Abstractive Summarization.</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="bias1">
Sheng, E., Chang, K. W., Natarajan, P., & Peng, N. (2019). "<a href="https://arxiv.org/abs/1909.01326">The woman worked as a babysitter: On biases in language generation</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="bias2">
Bordia, S., & Bowman, S. R. (2019). "<a href="https://arxiv.org/abs/1904.03035">Identifying and reducing gender bias in word-level language models</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="bias3">
Nadeem, M., Bethke, A., & Reddy, S. (2020). "<a href="https://arxiv.org/abs/2004.09456">StereoSet: Measuring stereotypical bias in pretrained language models</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="ziegler">
Ziegler, D. M., Stiennon, N., Wu, J., Brown, T. B., Radford, A., Amodei, D., Christiano, P., & Irving, G. (2019). "<a href="https://arxiv.org/abs/1909.08593">Fine-tuning language models from human preferences</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="bohm">
Böhm, F., Gao, Y., Meyer, C. M., Shapira, O., Dagan, I., & Gurevych, I. (2019). "<a href="https://arxiv.org/abs/1909.01214">Better rewards yield better summaries: Learning to summarise without references</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="dialogue1">
Jaques, N., Ghandeharioun, A., Shen, J. H., Ferguson, C., Lapedriza, A., Jones, N., Gu, S., & Picard, R. (2019). "<a href="https://arxiv.org/pdf/1907.00456">Way off-policy batch deep reinforcement learning of implicit human preferences in dialog</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="dialogue2">
Yi, S., Goel, R., Khatri, C., Cervone, A., Chung, T., Hedayatnia, B., ... & Hakkani-Tur, D. (2019). "<a href="https://arxiv.org/abs/1904.13015">Towards coherent and engaging spoken dialog response generation using automatic conversation evaluators</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="dialogue3">
Hancock, B., Bordes, A., Mazare, P. E., & Weston, J. (2019). "<a href="https://arxiv.org/abs/1901.05415">Learning from dialogue after deployment: Feed yourself, chatbot!</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="semantic-parsing">
Lawrence, C., & Riezler, S. (2018). "<a href="https://arxiv.org/abs/1805.01252">Improving a neural semantic parser by counterfactual learning from human bandit feedback</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="translation1">
Kreutzer, J., Khadivi, S., Matusov, E., & Riezler, S. (2018). "<a href="https://arxiv.org/abs/1804.05958">Can Neural Machine Translation be Improved with User Feedback?</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="translation2">
Bahdanau, D., Brakel, P., Xu, K., Goyal, A., Lowe, R., Pineau, J., ... & Bengio, Y. (2016). "<a href="https://arxiv.org/abs/1607.07086">An actor-critic algorithm for sequence prediction</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="story">
Zhou, W., & Xu, K. (2020). "<a href="https://www.aaai.org/Papers/AAAI/2020GB/AAAI-ZhouW.1159.pdf">Learning to Compare for Better Training and Evaluation of Open Domain Natural Language Generation Models</a>." In AAAI 2020.
</li>
<li class="js-ref" data-id="review">
Cho, W., & Zhang, P., & Zhang, Y., & Li, X., & Galley, M., & Brockett, C., & Wang, M., & Gao, J. (2018). "<a href="https://arxiv.org/pdf/1811.00511.pdf">Towards coherent and cohesive long-form text generation.</a>" arXiv preprint.
</li>
<li class="js-ref" data-id="evidence">
Perez, E., & Karamcheti, S., & Fergus, R., & Weston, J., & Kiela, D., & Cho, K. (2019).
"<a href="https://arxiv.org/pdf/1811.00511.pdf"> Finding generalizable eevidence by learning to convince Q&A models.</a>" arXiv preprint.
</li>
<li class="js-ref" data-id="rl1">
Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). "<a href="https://papers.nips.cc/paper/7017-deep-reinforcement-learning-from-human-preferences.pdf">Deep reinforcement learning from human preferences</a>." In Advances in Neural Information Processing Systems 2017.
</li>
<li class="js-ref" data-id="rl2">
Ibarz, B., Leike, J., Pohlen, T., Irving, G., Legg, S., & Amodei, D. (2018). "<a href="https://papers.nips.cc/paper/8025-reward-learning-from-human-preferences-and-demonstrations-in-atari.pdf">Reward learning from human preferences and demonstrations in Atari</a>." In Advances in Neural Information Processing Systems 2018.
</li>
<li class="js-ref" data-id="gpt3">
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., ... & Agarwal, S. (2020). "<a href="https://arxiv.org/abs/2005.14165"> Language models are few-shot learners</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="t5">
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... & Liu, P. J. (2019). "<a href="https://arxiv.org/abs/1910.10683"> Exploring the limits of transfer learning with a unified text-to-text transformer</a>." arXiv preprint.
</li>
<li class="js-ref" data-id="convseq2seq">
Zhang, Y., Li, D., Wang, Y., Fang, Y., & Xiao, W. (2019). "<a href="https://arxiv.org/abs/1910.10683"> Exploring the limits of transfer learning with a unified text-to-text transformer</a>." In Applied Sciences.
</li>
<li class="js-ref" data-id="amplification">
Christiano, P., Shlegeris, B., & Amodei, D. (2018). "<a href="https://arxiv.org/abs/1810.08575"> Supervising strong learners by amplifying weak experts</a>." arXiv preprint.
</li>
</ol>
</div>
</div></div>
<!-- special footer item for footnotes -->
<div data-order="-2"><hr><div class="row" id="footnotes">
<div class="col">Footnotes</div>
<div class="col">
<hr class="footnotes-sep">
<section class="footnotes">
<ol class="footnotes-list">
<li id="fn1" class="footnote-item"><p>For training, we use the Reddit TL;DR dataset<span class="js-rfref" data-id="tldr-dataset"></span> instead of the more popular CNN/DM dataset because simple copying baselines perform better than the human-written reference summaries on CNN/DM, which is not the case for TL;DR (see Appendix D of our paper).  We performed a new web crawl to increase the TL;DR dataset size, required summaries to be between 24 and 48 tokens, and performed some other cleaning and filtering. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref1" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn2" class="footnote-item"><p>We hire human labelers to judge summary quality, and implement quality control to ensure that labeler judgments agree with our own. We describe our human data collection procedure below. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref2" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn3" class="footnote-item"><p>We generate all of our samples at temperature 0, which we found humans preferred most. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref3" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn4" class="footnote-item"><p>While we use human-written TL;DRs as our main point of comparison, they don’t always represent optimal human performance; they are sometimes intended to be funny or to summarize only a part of the post, and their grammar and style are all over the map. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref4" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn5" class="footnote-item"><p>We control by training a logistic regression model to predict the preferred summary given only the policy ID and the log ratio of the lengths of the summaries. Then, we report the regression coefficients on each policy ID, corresponding to a length ratio of 1 with the reference summaries. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref5" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn6" class="footnote-item"><p>Interestingly, we found that human evaluators preferred the Lead-3 baseline (taking the first 3 sentences of the article) to the dataset’s reference summaries, and we confirmed this ourselves. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref6" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn7" class="footnote-item"><p>We took this approach because it is hard to directly compare our TL;DR-trained models to models trained on CNN/DM; the CNN/DM summaries are much longer and written in bullet-point form. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref7" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn8" class="footnote-item"><p>In terms of ROUGE results on CNN/DM, our 6.7B supervised models are a bit worse than T5 <span class="js-rfref" data-id="t5"></span>, but a bit better than state-of-the-art models from mid-2019<span class="js-rfref" data-id="convseq2seq"></span>. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref8" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn9" class="footnote-item"><p>Our main models are trained on about 65K comparisons, though we achieve good results with as few as 8K comparisons. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref9" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn10" class="footnote-item"><p>Specifically, we use Upwork, Scale, and Lionbridge. Our contractors have a range of ages, genders, and educational backgrounds, and are mostly American or Filipino (see Appendix C of our paper for demographic data). <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref10" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn11" class="footnote-item"><p>Our criteria for hiring contractors were: (1) they were willing to do the task, and (2) they passed a minimum threshold of speed and agreement with researcher labels. We paid all our contractors at least $15/hr. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref11" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn12" class="footnote-item"><p>This is impressive relative to the TL;DR reference summaries, which get a perfect <em>overall</em> score 23% of the time, but indicates there is still room for improvement. <a href="https://openai.com/blog/learning-to-summarize-with-human-feedback/#fnref12" class="footnote-backref">↩︎</a></p>
</li>
</ol>
</section>
<!--kg-card-end: markdown-->
    </div></div></div></footer>  
</div>
            