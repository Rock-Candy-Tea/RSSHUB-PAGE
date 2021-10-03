
---
title: 'Building architectures that can handle the world’s data'
categories: 
 - 新媒体
 - DeepMind
 - Blog
headimg: 'https://picsum.photos/400/300?random=6589'
author: DeepMind
comments: false
date: Tue, 03 Aug 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6589'
---

<div>   
<h4>Perceiver and Perceiver IO work as multi-purpose tools for AI</h4>
<p>Most architectures used by AI systems today are specialists. A 2D residual network may be a good choice for processing images, but at best it’s a loose fit for other kinds of data — such as the Lidar signals used in self-driving cars or the torques used in robotics. What’s more, standard architectures are often designed with only one task in mind, often leading engineers to bend over backwards to reshape, distort, or otherwise modify their inputs and outputs in hopes that a standard architecture can learn to handle their problem correctly. Dealing with more than one kind of data, like the sounds and images that make up videos, is even more complicated and usually involves complex, hand-tuned systems built from many different parts, even for simple tasks. As part of DeepMind's mission of solving intelligence to advance science and humanity, we want to build systems that can solve problems that use many types of inputs and outputs, so we began to explore a more general and versatile architecture that can handle all types of data.</p>  
</div>
            