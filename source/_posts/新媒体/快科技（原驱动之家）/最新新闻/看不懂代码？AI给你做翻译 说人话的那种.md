
---
title: '看不懂代码？AI给你做翻译 说人话的那种'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220202/S7dc57eb6-8790-41d6-a6e1-527ea1365ff0.jpg'
author: 快科技（原驱动之家）
comments: false
date: Wed, 02 Feb 2022 19:34:38 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220202/S7dc57eb6-8790-41d6-a6e1-527ea1365ff0.jpg'
---

<div>   
<p>GitHub Copilot，最近又出了个新功能。</p>
<p>这一次，它不再是帮你写代码了，而是充当一个“翻译官”：</p>
<p>用“人话”告诉你，这段代码到底写了啥。</p>
<p><strong>瞧，只需要选中一段代码，然后点一下旁边的“Ask Copilot”，就会快速得到代码的“人话版”解释：</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/7dc57eb6-8790-41d6-a6e1-527ea1365ff0.jpg" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="364" src="https://img1.mydrivers.com/img/20220202/S7dc57eb6-8790-41d6-a6e1-527ea1365ff0.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>示例中的代码片段是这样的：</p>
<p></p><p align="center"><a href="https://img1.mydrivers.com/img/20220202/3c03cb700f3842a1a8d11914d70e9b54.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="231" src="https://img1.mydrivers.com/img/20220202/s_3c03cb700f3842a1a8d11914d70e9b54.png" style="border: black 1px solid;" w="283" referrerpolicy="no-referrer"></a></p>
<p></p>
<p>Copilot对此进行“翻译”后，输出的内容是：</p>
<p>定义一个函数max_int()，它将一个列表作为输入。</p>
<p>设置一个变量max_int=l[0]，它包含列表中的第一个元素。</p>
<p>设置一个for循环，迭代列表中的每个元素。</p>
<p>如果元素大于max_int，便让max_int等于I。</p>
<p>返回max_int。</p>
<p>这便是GitHub Copilot的最新功能——Explain Code。</p>
<p>之前Copilot是基于人类的注释生成代码，现在好了，它也学会了反向输出。</p>
<p>网友们的反应也是可想而知了：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/c8e94745-69ec-4335-b741-8a1e6ea0425c.jpg" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="389" src="https://img1.mydrivers.com/img/20220202/Sc8e94745-69ec-4335-b741-8a1e6ea0425c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但在“新奇”之后，这件事也引发了不小的讨论。</p>
<p>AI给代码做注释，有必要吗？</p>
<p>不仅是Copilot，“AI给代码做注释”这事最近在Reddit也比较火。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/1cb47511-5028-43da-b0d9-0502937c2fae.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="442" src="https://img1.mydrivers.com/img/20220202/S1cb47511-5028-43da-b0d9-0502937c2fae.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>有位贴主上传了他用AI技术，给代码做注释的demo。</p>
<p><span style="color:#ff0000;"><strong>不同于Copilot的Explain Code，这个AI不会非常详尽地去描述每行代码运行的过程。</strong></span></p>
<p><span style="color:#ff0000;"><strong>而是概括性地去讲“这段代码是干嘛的”。</strong></span></p>
<p>以下面这个代码片段为例：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/621b096f-d151-4bf2-b6b6-7c96e7de7463.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="378" src="https://img1.mydrivers.com/img/20220202/S621b096f-d151-4bf2-b6b6-7c96e7de7463.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在AI“解读”过后，它就会告诉你：</p>
<p>这段代码是用来从GitHub的Repo中收集数据。</p>
<p>会返回一个数据的矩阵。</p>
<p>再如下面这个代码片段：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/7ed3da4b-a74f-4d9d-971d-4e483b3fb928.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="345" src="https://img1.mydrivers.com/img/20220202/S7ed3da4b-a74f-4d9d-971d-4e483b3fb928.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>AI给出的注释是：</p>
<p>函数运行的是梯度下降算法。</p>
<p>而后它还会对函数中的变量依次做解释。</p>
<p>看似不错的效果，但依旧还是引来了网友们激烈的讨论。</p>
<p>“乐观派”网友认为：</p>
<p>辅助写注释和写测试比写代码的帮助大更多，而犯错可能更少。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/34a7cd21-74e7-4a5b-a337-32fa333fa997.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="60" src="https://img1.mydrivers.com/img/20220202/S34a7cd21-74e7-4a5b-a337-32fa333fa997.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但有人质疑这种AI的能力：</p>
<p>如果我函数写的特别乱、变量这名字乱糟糟的，它还能好使吗？</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/918f27e2-609d-4618-b6a5-0629bdeef0a7.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="195" src="https://img1.mydrivers.com/img/20220202/S918f27e2-609d-4618-b6a5-0629bdeef0a7.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>也有人认为，诸如此类的AI“没有什么用处”：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/061e53bf-3268-4c0b-ac44-56b7af2282d5.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="158" src="https://img1.mydrivers.com/img/20220202/S061e53bf-3268-4c0b-ac44-56b7af2282d5.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>更形象一点的比喻，这种AI起到的作用，可能就是“复读机”……</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220202/d5bd2bfe-2ed7-407d-b05b-5eb9882ee1c3.png" target="_blank"><img alt="看不懂代码？AI给你做翻译 说人话的那种" h="86" src="https://img1.mydrivers.com/img/20220202/Sd5bd2bfe-2ed7-407d-b05b-5eb9882ee1c3.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>那么对于“AI给打码写注释”这件事，你觉得是否有用呢？</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/daima.htm"><i>#</i>代码</a><a href="https://news.mydrivers.com/tag/ai.htm"><i>#</i>AI</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/WM60YyQaySPXj8nIlN83Nw">量子位</a></span>
<span>责任编辑：祥云</span>
</p>
        
</div>
            