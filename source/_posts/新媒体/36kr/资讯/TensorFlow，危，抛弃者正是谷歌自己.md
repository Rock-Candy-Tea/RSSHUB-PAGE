
---
title: 'TensorFlow，危，抛弃者正是谷歌自己'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220620/v2_7666aabbc6924cc68adbbdb8dd29d979_img_000'
author: 36kr
comments: false
date: Mon, 20 Jun 2022 06:49:17 GMT
thumbnail: 'https://img.36krcdn.com/20220620/v2_7666aabbc6924cc68adbbdb8dd29d979_img_000'
---

<div>   
<p>收获接近16.6万个Star、见证深度学习崛起的TensorFlow，地位已岌岌可危。</p> 
<p>并且这次，冲击不是来自老对手PyTorch，而是自家新秀<strong>JAX</strong>。</p> 
<p>最新一波AI圈热议中，连fast.ai创始人Jeremy Howard都下场表示：</p> 
<blockquote> 
 <p>JAX正逐渐取代TensorFlow这件事，早已<strong>广为人知</strong>了。现在它就在发生（至少在谷歌内部是这样）。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="874,274" src="https://img.36krcdn.com/20220620/v2_7666aabbc6924cc68adbbdb8dd29d979_img_000" referrerpolicy="no-referrer"></p> 
<p>LeCun更是认为，深度学习框架之间的激烈竞争，已经进入了一个新的阶段。</p> 
<p class="image-wrapper"><img data-img-size-val="860,286" src="https://img.36krcdn.com/20220620/v2_6f7ddaef9f104d10845da5bacc61d9a3_img_000" referrerpolicy="no-referrer"></p> 
<p>LeCun表示，当初谷歌的TensorFlow确实比Torch更火。然而Meta的PyTorch出现之后，现在其受欢迎程度已经超过TensorFlow了。</p> 
<p>现在，包括Google Brain、DeepMind以及不少外部项目，都已经开始用上JAX。</p> 
<p>典型例子就是最近爆火的DALL·E Mini，为了充分利用TPU，作者采用了JAX进行编程。有人用过后感叹：</p> 
<blockquote> 
 <p>这可比PyTorch快多了。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="711,82" src="https://img.36krcdn.com/20220620/v2_c1eb0a3817864b0f942d52668aa94a4b_img_000" referrerpolicy="no-referrer"></p> 
<p>据《商业内幕》透露，预计在未来几年内，JAX将覆盖谷歌<strong>所有</strong>采用机器学习技术的产品。</p> 
<p>这样看来，如今大力在内部推广JAX，更像是谷歌在框架上发起的一场“自救”。</p> 
<h2><strong>JAX从何而来？</strong></h2> 
<p>关于JAX，谷歌其实是有备而来。</p> 
<p>早在2018年的时候，它就由谷歌大脑的一个三人小团队给搭出来了。</p> 
<p>研究成果发表在了题为Compiling machine learning programs via high-level tracing的论文中：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,453" src="https://img.36krcdn.com/20220620/v2_a30408b5a1ae47b2b27772ae29dcf01c_img_000" referrerpolicy="no-referrer"></p> 
<p>Jax是一个用于高性能数值计算的Python库，而深度学习只是其中的功能之一。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,608" src="https://img.36krcdn.com/20220620/v2_d7bf1ea78a5e4920ae0eb8d870421870_img_000" referrerpolicy="no-referrer"></p> 
<p>自诞生以来，它受欢迎的程度就一直在上升。</p> 
<p>最大的特点就是<strong>快</strong>。</p> 
<p>一个例子感受一下。</p> 
<p>比如求矩阵的前三次幂的和，用NumPy实现，计算需要约478毫秒。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,268" src="https://img.36krcdn.com/20220620/v2_9ab501d48fb243b89d41305cb93fc0ce_img_000" referrerpolicy="no-referrer"></p> 
<p>用JAX就只需要5.54 毫秒，比NumPy快86倍。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,214" src="https://img.36krcdn.com/20220620/v2_12f296951ed947d9afbf7ab3ee5d09be_img_000" referrerpolicy="no-referrer"></p> 
<p>为什么这么快？原因有很多，包括：</p> 
<p>1、NumPy加速器。NumPy的重要性不用多说，用Python搞科学计算和机器学习，没人离得开它，但它原生一直不支持GPU等硬件加速。</p> 
<p>JAX的计算函数API则全部基于NumPy，可以让模型很轻松在GPU和TPU上运行。这一点就拿捏住了很多人。</p> 
<p>2、XLA。XLA（Accelerated Linear Algebra）就是加速线性代数，一个优化编译器。JAX建立在XLA之上，大幅提高了JAX计算速度的上限。</p> 
<p>3、JIT。研究人员可使用XLA将自己的函数转换为实时编译（JIT）版本，相当于通过向计算函数添加一个简单的函数修饰符，就可以将计算速度提高几个数量级。</p> 
<p>除此之外，JAX与Autograd完全兼容，支持自动差分，通过grad、hessian、jacfwd和jacrev等函数转换，支持反向模式和正向模式微分，并且两者可以任意顺序组成。</p> 
<p>当然，JAX也是有一些<strong>缺点</strong>在身上的。</p> 
<p>比如：</p> 
<p>1、虽然JAX以加速器著称，但它并没有针对CPU计算中的每个操作进行充分优化。</p> 
<p>2、JAX还太新，没有形成像TensorFlow那样完整的基础生态。因此它还没有被谷歌以成型产品的形式推出。</p> 
<p>3、debug需要的时间和成本不确定，“副作用”也不完全明确。</p> 
<p>4、不支持Windows系统，只能在上面的虚拟环境中运行。</p> 
<p>5、没有数据加载器，得借用TensorFlow或PyTorch的。</p> 
<p>……</p> 
<p>尽管如此，简单、灵活又好用的JAX还是率先在DeepMind中流行起来。2020年诞生的一些深度学习库Haiku和RLax等都是基于它开发。</p> 
<p>这一年，PyTorch原作者之一Adam Paszke，也全职加入了JAX团队。</p> 
<p>目前，JAX的开源项目在GitHub上已有18.4k标星，比TensorFlow高了不少了。</p> 
<p>值得注意的是，在此期间，有不少声音都表示它很可能取代TensorFlow。</p> 
<p>一方面是因为JAX的实力，另一方面主要还是跟TensorFlow自身的很多原因有关。</p> 
<h2><strong>为什么谷歌要转投JAX？</strong></h2> 
<p>诞生于2015年的TensorFlow，曾经也风靡一时，推出后很快超过了Torch、Theano和Caffe等一众“弄潮儿”，成为最受欢迎的机器学习框架。</p> 
<p>然而在2017年，焕然一新的PyTorch“卷土重来”。</p> 
<p>这是Meta基于Torch搭建的机器学习库，由于上手简单、通俗易懂，很快受到一众研究者的青睐，甚至有超过TensorFlow的趋势。</p> 
<p>相比之下，TensorFlow却在频繁更新和界面迭代中变得越来越臃肿，逐渐失去了开发者的信任。</p> 
<p>（从Stack Overflow上的提问占比来看，PyTorch逐年上升，TensorFlow却一直停滞不前）</p> 
<p class="image-wrapper"><img data-img-size-val="1066,768" src="https://img.36krcdn.com/20220620/v2_7219c2a85d404dd683c5b72dcc8296a5_img_000" referrerpolicy="no-referrer"></p> 
<p>在竞争之中，TensorFlow的缺点逐渐暴露出来，API不稳定、实现复杂、学习成本高等问题并没有随着更新解决多少，反而结构变得更复杂了。</p> 
<p>相比之下，TensorFlow却没有继续发挥比较能打的“运行效率”等优势。</p> 
<p>在学术界，PyTorch的使用率正逐渐超过TensorFlow。</p> 
<p>尤其是在各大顶会如ACL、ICLR中，使用PyTorch实现的算法框架近几年已经占据了超过80%，相比之下TensorFlow的使用率还在不断下降。</p> 
<p>也正是因此，谷歌坐不住了，试图用JAX夺回对机器学习框架的“主导权”。</p> 
<p>虽然JAX名义上不是“专为深度学习构建的通用框架”，然而从发布之初起，谷歌的资源就一直在向JAX倾斜。</p> 
<p>一方面，谷歌大脑和DeepMind逐渐将更多的库构建在JAX上。</p> 
<p>包括谷歌大脑的Trax、Flax、Jax-md，以及DeepMind的神经网络库Haiku和强化学习库RLax等，都是基于JAX构建的。</p> 
<p>据谷歌官方表示：</p> 
<blockquote> 
 <p>JAX生态系统开发中，也会考虑确保其与现有TensorFlow库（如Sonnet和TRFL）的设计（尽可能）保持一致。</p> 
</blockquote> 
<p>另一方面，更多的项目也开始基于JAX实现，最近爆火的DALL·E mini项目就是其中一个。</p> 
<p>由于能更好地利用谷歌TPU的优势，JAX在运行性能上比PyTorch要好得多，更多之前搭建在TensorFlow上的工业界项目也正在转投JAX。</p> 
<p>甚至有网友调侃JAX如今爆火的原因：可能是TensorFlow的使用者实在无法忍受这个框架了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,316" src="https://img.36krcdn.com/20220620/v2_61b2ac21024b419499f25c854f0f8e91_img_000" referrerpolicy="no-referrer"></p> 
<p>那么，JAX到底有没有希望替代TensorFlow，成为与PyTorch抗衡的新力量呢？</p> 
<h2><strong>更看好哪一个框架？</strong></h2> 
<p>总体来看，很多人还是很坚定地站PyTorch。</p> 
<p>他们似乎不喜欢谷歌每年都出一个新框架的速度。</p> 
<p class="image-wrapper"><img data-img-size-val="876,230" src="https://img.36krcdn.com/20220620/v2_f87c5030a6b34086899b780698f31c24_img_000" referrerpolicy="no-referrer"></p> 
<p>“JAX虽然很吸引人，但还不够具备“革命性”的能力促使大家抛弃PyTorch来使用它。”</p> 
<p class="image-wrapper"><img data-img-size-val="890,614" src="https://img.36krcdn.com/20220620/v2_e6420d641510438399235abced67967b_img_000" referrerpolicy="no-referrer"></p> 
<p>但看好JAX的也并非少数。</p> 
<p>就有人表示，PyTorch是很完美，但JAX也在缩小差距。</p> 
<p class="image-wrapper"><img data-img-size-val="882,540" src="https://img.36krcdn.com/20220620/v2_ba84ba24026d4fa4b25bf88894d939ff_img_000" referrerpolicy="no-referrer"></p> 
<p>甚至还有人疯狂给JAX打call，表示它比PyTorch要厉害10倍，并称：如果Meta不继续加把劲儿的话谷歌就会赢了。（手动狗头）</p> 
<p class="image-wrapper"><img data-img-size-val="880,194" src="https://img.36krcdn.com/20220620/v2_14af86b651574618a980c1ef6a6e602e_img_000" referrerpolicy="no-referrer"></p> 
<p>不过，总有不怎么care谁输谁赢的人，他们的目光放得很长远：</p> 
<blockquote> 
 <p>没有最好，只有更好。最重要的是更多玩家和好的idea统统都加入进来，让开源和真正优秀的创新画上等号。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="872,214" src="https://img.36krcdn.com/20220620/v2_25903da16e8145828c6ad92dbc00384e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">项目地址：https://github.com/google/jax</p> 
<h2>参考链接：</h2> 
<p>https://twitter.com/jeremyphoward/status/1538380788324257793https://twitter.com/ylecun/status/1538419932475555840https://mp.weixin.qq.com/s/AoygUZK886RClDBnp1v3jwhttps://www.deepmind.com/blog/using-jax-to-accelerate-our-researchhttps://github.com/tensorflow/tensorflow/issues/53549</p> 
<p class="editor-note">本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/XkXRMveB9JRRT4_XIWk3EA">“量子位”（ID:QbitAI）</a>，作者：萧箫 丰色，36氪经授权发布。</p>  
</div>
            