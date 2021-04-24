
---
title: 'Specification gaming_ the flip side of AI ingenuity'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=9643'
author: DeepMind
comments: false
date: Tue, 21 Apr 2020 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9643'
---

<div>   
<p><strong>Specification gaming</strong><span style="font-weight: 400;"> is a behaviour that satisfies the literal specification of an objective without achieving the intended outcome. We have all had experiences with specification gaming, even if not by this name. Readers may have heard the myth of </span><a href="https://en.wikipedia.org/wiki/Midas"><span style="font-weight: 400;">King Midas</span></a><span style="font-weight: 400;"> and the golden touch, in which the king asks that anything he touches be turned to gold - but soon finds that even food and drink turn to metal in his hands. In the real world, when rewarded for doing well on a homework assignment, a student might copy another student to get the right answers, rather than learning the material - and thus exploit a loophole in the task specification. </span></p>
<p><span style="font-weight: 400;">This problem also arises in the design of artificial agents. For example, a reinforcement learning agent can find a shortcut to getting lots of reward without completing the task as intended by the human designer. These behaviours are common, and we have </span><a href="http://tinyurl.com/specification-gaming"><span style="font-weight: 400;">collected</span></a><span style="font-weight: 400;"> around 60 examples so far (aggregating </span><a href="https://arxiv.org/abs/1803.03453"><span style="font-weight: 400;">existing</span></a> <a href="https://www.gwern.net/Tanks#alternative-examples"><span style="font-weight: 400;">lists</span></a><span style="font-weight: 400;"> and ongoing </span><a href="https://docs.google.com/forms/d/e/1FAIpQLSeQEguZg4JfvpTywgZa3j-1J-4urrnjBVeoAO7JHIH53nrBTA/viewform"><span style="font-weight: 400;">contributions</span></a><span style="font-weight: 400;"> from the AI community). In this post, we review possible causes for specification gaming, share examples of where this happens in practice, and argue for further work on principled approaches to overcoming specification problems.</span></p>
<p><span style="font-weight: 400;">Let's look at an example. In a </span><a href="https://arxiv.org/abs/1704.03073"><span style="font-weight: 400;">Lego stacking task</span></a><span style="font-weight: 400;">, the desired outcome was for a red block to end up on top of a blue block. The agent was rewarded for the height of the bottom face of the red block when it is not touching the block. Instead of performing the relatively difficult maneuver of picking up the red block and placing it on top of the blue one, the agent simply flipped over the red block to collect the reward. This behaviour achieved the stated objective (high bottom face of the red block) at the expense of what the designer actually cares about (stacking it on top of the blue one).</span></p>  
</div>
            