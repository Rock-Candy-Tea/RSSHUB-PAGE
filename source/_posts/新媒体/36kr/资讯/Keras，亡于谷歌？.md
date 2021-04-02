
---
title: 'Keras，亡于谷歌？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210402/v2_5b7db72ab3464b2f86e3c4ff166a252c_img_000'
author: 36kr
comments: false
date: Fri, 02 Apr 2021 06:27:15 GMT
thumbnail: 'https://img.36krcdn.com/20210402/v2_5b7db72ab3464b2f86e3c4ff166a252c_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/PqXmFPi0qdSQWu-1hOREXw">“机器之心”（ID:almosthuman2014）</a>，36氪经授权发布。</p> 
<p>将 Keras 并入 TensorFlow，到底是不是一个正确的决定？</p> 
<p>近日，Reddit 上出现了一个「悼念」Keras 的帖子，引发了不少人的围观。发帖者表示，谷歌已经慢慢地将 Keras 杀死了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,362" src="https://img.36krcdn.com/20210402/v2_5b7db72ab3464b2f86e3c4ff166a252c_img_000" referrerpolicy="no-referrer"></p> 
<p>乍一看，这一观点似乎有点耸人听闻：Keras 活得好好的，怎么能说已经被谷歌杀死了呢？而且前不久，这个神经网络库刚刚过完 6 岁生日。MIT CSAIL 官方账号还发推表示，Keras 目前已经成为全世界使用最多的十大软件工具之一。</p> 
<p class="image-wrapper"><img data-img-size-val="1052,822" src="https://img.36krcdn.com/20210402/v2_ab8fa89d10bd420ca3a13d217ca67bea_img_000" referrerpolicy="no-referrer"></p> 
<p>这一切还要从 Keras 和谷歌的恩怨说起。</p> 
<p>Keras 与谷歌的 TensorFlow 有一段极其复杂的历史，这个故事很长，有很多细节，有时甚至会有一些矛盾。</p> 
<p>Keras 最初是由 Google AI 开发人员 / 研究人员 Francois Chollet 创建并开发的，作者于 2015 年 3 月 27 日将 Keras 的第一个版本 commit 并 release 到他的 GitHub 上。一开始，Francois 开发 Keras 是为了方便他自己的研究和实验。但随着深度学习的普及，许多开发人员、程序员和机器学习从业人员都因其易于使用的 API 而涌向 Keras。</p> 
<p>为了训练你自己的自定义神经网络，Keras 需要一个后端。后端是一个计算引擎——它可以构建网络的图和拓扑结构，运行优化器，并执行具体的数字运算。你可以把后台看作是你的数据库，Keras 是你用来访问数据库的编程语言。</p> 
<p>一开始，在 v1.1.0 之前，Keras 的默认后端都是 Theano。与此同时，Google 发布了 TensorFlow，这是一个用于机器学习和神经网络训练的符号数学库。Keras 开始支持 TensorFlow 作为后端。渐渐地，TensorFlow 成为最受欢迎的后端，这也就使得 TensorFlow 从 Keras v1.1.0 发行版开始成为 Keras 的默认后端。</p> 
<p>一般来说，一旦 TensorFlow 成为了 Keras 的默认后端，TensorFlow 和 Keras 的使用量会一起增长——没有 TensorFlow 的情况下就无法使用 Keras，所以如果你在系统上安装了 Keras，那么你也得安装 TensorFlow。</p> 
<p> 同样的，TensorFlow 用户也越来越被高级 Keras API 的简单易用所吸引。tf.keras 是在 TensorFlow v1.10.0 中引入的，这是将 keras 直接集成到 TensorFlow 包中的第一步。</p> 
<p>tf.keras 软件包与你通过 pip 安装的 keras 软件包（即 pip install keras）是分开的。为了确保兼容性，原始的 keras 包没有被包含在 tensorflow 中，因此它们的开发都很有序。</p> 
<p>然而，这种情况后来发生了改变改变——当谷歌在 2019 年 6 月发布 TensorFlow 2.0 时，他们宣布 Keras 现在是 TensorFlow 的官方高级 API，用于快速简单的模型设计和训练。随着 Keras 2.3.0 的发布，Francois 在声明中写道：</p> 
<p>这是 Keras 首个与 tf.keras 同步的版本，也是 Keras 支持多个后端（即 Theano，CNTK 等）的最终版本。最重要的是，所有深度学习从业人员都应将其代码转换成 TensorFlow 2.0 和 tf.keras 软件包。原始的 keras 软件包仍会接收 bug 并修复，但请向前看，你应该开始使用 tf.keras 了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,540" src="https://img.36krcdn.com/20210402/v2_7cf2e28f52aa4badb452986799ecb501_img_000" referrerpolicy="no-referrer"></p> 
<p>对于 Keras 和 TensorFlow 来说，二者的合并似乎是一个双赢的决定，但很多开发者不这么认为。上述发帖者就是其中之一。</p> 
<p>ta 认为，这一决定已经慢慢地将 Keras 杀死了。为了解释这一观点，ta 还给出了三个理由：</p> 
<p>第一个理由是：在合并期间，Keras API 被有效地「冻结」了，这使得它在特性方面落后于其他竞争者；</p> 
<p>第二个理由是：TF 2 发布得太晚了。最重要的是，最初的几个 2.x 版本漏洞百出，甚至现在也缺乏一些基本的特性；</p> 
<p>第三个理由是：谷歌没有在 TF 1 和 2 之间进行坚决的切割，而是将 TF 1 中的很多包和垃圾直接移植到 TF 2，使得框架非常臃肿。当某个地方出问题时，你会被满屏冗长的神秘错误信息和堆栈追踪所淹没。</p> 
<p class="image-wrapper"><img data-img-size-val="1075,369" src="https://img.36krcdn.com/20210402/v2_da3e74e7155246209d1c848d1ccff171_img_000" referrerpolicy="no-referrer"></p> 
<p>基于这些体验，发帖者认为，Keras 已经被谷歌杀死了。</p> 
<p>除此之外，之前的一些开发者也指出了二者合并之后带来的一些问题。比如 API 混乱。二者合并之后，tf.keras 中的高级 API 与 tf 中的底层 API 经常需要混用，这样的整合会让开发者不知所措。与此同时，API 的割裂也加大了开发者寻找教程的难度。比如在 TF 2.0 版本中，除了「TF2.0」 这个关键字，你还要弄清楚：这个文档是关于 TF2.0 本身的，还是关于 tf.keras 的。</p> 
<h2>悼念？我用着挺好的啊</h2> 
<p>虽然 Keras 并入 TensorFlow 造成了一些混乱，但有不少开发者认为，这一举动并没有毁掉 Keras，反而解决了很多实际问题。</p> 
<p>一位用户名为「acardosoj」的开发者认为，「Keras API 比以前更容易了。现在你有了更多的函数可以选择，可以更加轻松地利用 TensorFlow 分布式训练。你可以用几行代码在数百个 GPU 上训练一个巨大的模型。」这些在 2016 年都是不可能的。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,390" src="https://img.36krcdn.com/20210402/v2_75f7954022e44ecb8f204e7fcbde276f_img_000" referrerpolicy="no-referrer"></p> 
<p>用户名为「carlthome」的开发者也认为，今天的 Keras 的确增加了很多功能，tf.data、tf.metrics 和 tf.distribute 也因为 tf.keras 的存在而变得更易用。因此他认为，尽管 TensorFlow 的生态系统还需要改善，我们也不应该忽视这些年取得的进步。</p> 
<p class="image-wrapper"><img data-img-size-val="1077,501" src="https://img.36krcdn.com/20210402/v2_9f22b95e09b24a40a703ded88f25cd2e_img_000" referrerpolicy="no-referrer"></p> 
<p>甚至有位 TF 的用户表示，从 TF 转向完全集成了 Keras API 的 TF 2 是一个最好的选择。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,395" src="https://img.36krcdn.com/20210402/v2_9e408252067c4845b8328af92512b27f_img_000" referrerpolicy="no-referrer"></p> 
<p>虽然很多人表示，Keras 和 TF 的结合确实带来了一些改进，但他们也承认，现在整个的 TensorFlow 以及它与 Keras 的合并都很混乱。既然如此，谷歌的团队为什么不多花点工夫梳理一下呢？有些开发者认为，这可能是因为，谷歌的很多人都去开发 Jax 了。</p> 
<p class="image-wrapper"><img data-img-size-val="1078,282" src="https://img.36krcdn.com/20210402/v2_b7feec2d47224d3ca807f5b4df97cd1e_img_000" referrerpolicy="no-referrer"></p> 
<p>「Tensorflow 从一开始就是一团糟，它非常适合作为可<a class="project-link" data-id="259561" data-name="微分" data-logo="https://img.36krcdn.com/20201105/v2_0ad10c1c18294d899b85a62b785a337f_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/259561" target="_blank">微分</a>编程的工具，但在设计上有一些问题影响了灵活性。PyTorch 的动态图计算做的更好，TF2 想追赶但为时已晚。」</p> 
<p class="image-wrapper"><img data-img-size-val="824,343" src="https://img.36krcdn.com/20210402/v2_a720ddebb83747feb0379de2a51abf0d_img_000" referrerpolicy="no-referrer"></p> 
<p>实际上，很多谷歌程序员可能都已经转向 Jax 了。Jax 是谷歌开发的一个 Python 库，用于机器学习和数学计算，具有正向和反向自动微分功能，非常擅长计算高阶导数。程序员们还开发了像 Haiku 这样的工具，使 Jax 可面向对象。</p> 
<p class="image-wrapper"><img data-img-size-val="813,348" src="https://img.36krcdn.com/20210402/v2_d4b0ba65cf194b6cab696d6f3dfbd041_img_000" referrerpolicy="no-referrer"></p> 
<p>与其说 TensorFlow 杀死了 Keras，还不如说 TF2 杀死了 Tensorflow。当转向 Jax 的人数越来越多，Keras 会随之销声匿迹吗？</p> 
<h3>参考链接：</h3> 
<p>https://www.reddit.com/r/MachineLearning/comments/mhrpbm/d_keras_killed_by_google/</p>  
</div>
            