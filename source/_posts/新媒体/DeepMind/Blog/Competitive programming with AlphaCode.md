
---
title: 'Competitive programming with AlphaCode'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=6674'
author: DeepMind
comments: false
date: Wed, 02 Feb 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6674'
---

<div>   
<p><strong>Solving novel problems and setting a new milestone in competitive programming.</strong></p>
<p></p>
<p>Creating solutions to unforeseen problems is second nature in human intelligence – a result of critical thinking informed by experience. The machine learning community has made tremendous progress in generating and understanding textual data, but advances in problem solving remain limited to relatively simple maths and programming problems, or else retrieving and copying existing solutions. As part of <a href="https://deepmind.com/about" rel="noopener" target="_blank">DeepMind’s mission</a> to solve intelligence, we created a system called AlphaCode that writes computer programs at a competitive level. AlphaCode achieved an estimated rank within the top 54% of participants in programming competitions by solving new problems that require a combination of critical thinking, logic, algorithms, coding, and natural language understanding.</p>
<p></p>
<p>In <a href="https://storage.googleapis.com/deepmind-media/AlphaCode/competition_level_code_generation_with_alphacode.pdf" rel="noopener" target="_blank">our preprint</a>, we detail AlphaCode, which uses transformer-based language models to generate code at an unprecedented scale, and then smartly filters to a small set of promising programs.</p>
<p></p>
<p>We validated our performance using competitions hosted on <a href="https://codeforces.com/" rel="noopener" target="_blank">Codeforces</a>, a popular platform which hosts regular competitions that attract tens of thousands of participants from around the world who come to test their coding skills. We selected for evaluation 10 recent contests, each newer than our training data. AlphaCode placed at about the level of the median competitor, marking the first time an AI code generation system has reached a competitive level of performance in programming competitions.</p>
<p></p>
<p>To help others build on our results, we’re releasing our dataset of competitive programming problems and solutions <a href="https://github.com/deepmind/code_contests" rel="noopener" target="_blank">on GitHub</a>, including extensive tests to ensure the programs that pass these tests are correct — a critical feature current datasets lack. We hope this benchmark will lead to further innovations in problem solving and code generation.</p>  
</div>
            