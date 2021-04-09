
---
title: '2021 年了，TensorFlow 和 PyTorch 两个深度学习框架地位又有什么变化吗？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=4857'
author: 知乎
comments: false
date: Fri, 09 Apr 2021 03:51:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=4857'
---

<div>   
小小将的回答<br><br><p>变化太大了，今年面试的实习生，当问他们常用的深度学习框架时，他们清一色的选择了：PyTorch。</p><p>我个人认为几个原因导致地位逆转：</p><p>（1）PyTorch的易用性更好（当一个框架本身能衍生很多上层框架时，你就能知道它本身是多么不友好了，说的就是TF），而且生态已经起来了，大部分论文开源都是用PyTorch；</p><p>（2）TF2看起来并不太成功，反而破坏TF1的生态。TF1和TF2往往混杂在一起，让人摸不着头脑。</p><p>（3）关于大家最担心的部署优化问题，其实目前PyTorch也在不断提升这块的劣势，目前Torch->ONNX->TensorRT已经相对成熟了，其他的端侧框架如ncnn也支持torch了。当然动态图比静态图确实要多踩一点坑，但带来的可能是模型迭代效率的提升。</p><p>（4）关于分布式训练，TensorFlow可能优势更大，但可能大部分人最多跑个单机多卡就够了，所以性能上不会差距太大，而且分布式训练还有很多第三方框架来支持比如horovod。而且本身PyTorch自带的DDP也不差。</p><p>其实我从16年开始接触深度学习，最早学习的框架是theano，当TensorFlow出来后，theano的使用者就慢慢转向了TensorFlow，到19年我又开始转向PyTorch。每次转变后，我只能说一句话：真香。</p><p>声明：我的观察只限于在比较卷的CV领域。</p>  
</div>
            