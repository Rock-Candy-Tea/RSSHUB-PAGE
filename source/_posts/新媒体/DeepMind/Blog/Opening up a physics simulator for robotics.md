
---
title: 'Opening up a physics simulator for robotics'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=3921'
author: DeepMind
comments: false
date: Mon, 18 Oct 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3921'
---

<div>   
<h4><strong>Advancing research everywhere with the acquisition of MuJoCo</strong></h4>
<p>When you walk, your feet make contact with the ground. When you write, your fingers make contact with the pen. Physical contacts are what makes interaction with the world possible. Yet, for such a common occurrence, contact is a surprisingly complex phenomenon. Taking place at microscopic scales at the interface of two bodies, contacts can be soft or stiff, bouncy or spongy, slippery or sticky. It’s no wonder our fingertips have <a href="https://courses.lumenlearning.com/boundless-biology/chapter/somatosensation/" rel="noopener" target="_blank">four different types</a> of touch-sensors. This subtle complexity makes simulating physical contact — a vital component of robotics research — a tricky task.</p>
<p>The rich-yet-efficient contact model of the <a href="https://mujoco.org/" rel="noopener" target="_blank">MuJoCo physics simulator</a> has made it a leading choice by robotics researchers and today, we're proud to announce that, as part of <a href="https://deepmind.com/about" rel="noopener" target="_blank">DeepMind's mission</a> of advancing science, we've acquired MuJoCo and are making it <a href="https://mujoco.org/download" rel="noopener" target="_blank">freely available</a> for everyone, to support research everywhere. Already widely used within the robotics community, including as the physics simulator of choice for DeepMind’s robotics team, MuJoCo features a rich contact model, powerful scene description language, and a well-designed API. Together with the community, we will continue to improve MuJoCo as open-source software under a permissive licence. As we work to prepare the codebase, we are making MuJoCo <a href="https://mujoco.org/download" rel="noopener" target="_blank">freely available</a> as a precompiled library.</p>
<p>A balanced model of contact. MuJoCo, which stands for <strong>Mu</strong>lti-<strong>Jo</strong>int Dynamics with <strong>Co</strong>ntact, hits a sweet spot with its contact model, which accurately and efficiently captures the salient features of contacting objects. Like other rigid-body simulators, it avoids the fine details of deformations at the contact site, and often runs much faster than real time. Unlike other simulators, MuJoCo resolves contact forces using the convex <a href="https://en.wikipedia.org/wiki/Gauss%27s_principle_of_least_constraint" rel="noopener" target="_blank">Gauss Principle</a>. Convexity ensures unique solutions and well-defined inverse dynamics. The model is also flexible, providing multiple parameters which can be tuned to approximate a wide range of contact phenomena.</p>  
</div>
            