
---
title: 'AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/8/c269bc23-045a-4d91-9871-e8619e2a38ec.gif'
author: IT 之家
comments: false
date: Mon, 16 Aug 2021 02:37:27 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/8/c269bc23-045a-4d91-9871-e8619e2a38ec.gif'
---

<div>   
<p>AI 已经能教你画油画了。</p><p>随便给一张图，笔画序列秒秒钟呈现。</p><p>比如世界名画蒙娜丽莎。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/c269bc23-045a-4d91-9871-e8619e2a38ec.gif" w="320" h="315" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="320" height="315" referrerpolicy="no-referrer"></p><p>亦或是写实类的小鸟。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/0e4504b3-5a5d-486d-9e4d-ac970fc6db1c.gif" w="512" h="512" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="512" height="512" referrerpolicy="no-referrer"></p><p>还有极具氛围感的河灯。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/bcf74973-5421-4e5c-aefe-f953cbdddaa2.gif" w="512" h="512" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="512" height="512" referrerpolicy="no-referrer"></p><p>总之什么风格都可以驾驭。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/c5578709-d209-4779-9f0d-5769ce153e19.png" w="1080" h="282" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="1080" height="214" referrerpolicy="no-referrer"></p><p>这项技术在 Reddit 上 21 小时内就已经有 600 + 的点赞量。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/cf60c532-ecd9-4391-9cca-87b5b025b8e2.png" w="1080" h="134" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="1080" height="102" referrerpolicy="no-referrer"></p><p>究竟是如何打造的呢？</p><h2>用前馈网络预测笔画</h2><p>神经绘画，就是为给定的图像生成一系列笔画，并使用神经网络进行绘画式的真实再现过程。</p><p>研究团队提出了一个基于 Transformer 的框架，叫做 Paint Transformer，用前馈网络来预测笔画的参数。</p><p>由于当前没有可用的数据集来训练 Paint Transformer，受物体检测启发，研究人员设计了一个自训练 Pipeline。</p><p>整个模型由两个模块组成：笔画预测器和笔画渲染器。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/e5d37b37-a02b-453a-841c-c2fc1c310b07.png" w="1080" h="369" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="1080" height="280" referrerpolicy="no-referrer"></p><p>给定目标图像和中间画布图像，笔画预测器，生成一组参数以确定当前笔画集。</p><p>预测器包含了两个用于特征嵌入的 CNN 网路和一个用于参数预测的 Transformer。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/8e3cbb6b-a19a-43d8-b574-214046784079.png" w="624" h="392" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="624" height="392" referrerpolicy="no-referrer"></p><p>随后，笔画渲染器为笔画集汇总的每个笔画，生成笔画图像，并将它们绘制到画，产生结果图像，大小为 512*512。</p><p>在 DETR（用 Transformer 进行对象检测）的基础上，增加了二进制神经元来预测笔画是否应该被保留。</p><p>这样它就可以在没有任何现成的数据集的情况下进行训练，同时还能实现出色的泛化能力。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/a10d242b-d63a-4152-ade9-70a7d26951c7.png" w="1080" h="210" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="1080" height="159" referrerpolicy="no-referrer"></p><p>实验表明，这一方法比以前的方法取得了更好的绘画性能，而且训练和推理成本更低。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/42e7e245-c328-44f5-b3a0-5d2f5bafb148.png" w="1080" h="366" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="1080" height="278" referrerpolicy="no-referrer"></p><h2>百度南大团队打造</h2><p>这项技术由百度、南京大学、罗格斯大学共同打造。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/64e2ed7a-6a8f-4303-9a16-5b4c5e56ce16.png" w="1080" h="327" title="AI 教你画油画：任意画风都可驾驭，笔画序列秒秒钟呈现" width="1080" height="248" referrerpolicy="no-referrer"></p><p>目前代码已经开源，并在一刻相册 App 上应用。</p><p>论文地址：</p><p>https://arxiv.org/abs/2108.03798</p><p>GitHub 网址：</p><p>https://github.com/wzmsltw/PaintTransformer</p>
          
</div>
            