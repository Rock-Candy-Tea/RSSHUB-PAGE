
---
title: 'Arm可伸缩矩阵扩展（SME）在Linux 5.19发布之前准备就绪'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0426/22486ff178cc5a0.jpg'
author: cnBeta
comments: false
date: Tue, 26 Apr 2022 10:05:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0426/22486ff178cc5a0.jpg'
---

<div>   
<strong>Linux
5.19将为支持Arm可伸缩矩阵扩展（SME）做好所有基础准备工作。可扩展矩阵扩展（SME）是Armv9-A的一个新扩展，它建立在SVE/SVE2矢量扩展的基础上，允许矩阵叠瓦存储、加载/存储/插入/提取叠瓦矢量、SVE矢量的外积和流式SVE模式。</strong>带有SME的流式SVE模式启用了新的SME存储和指令以及SVE2指令的一个子集，而离开流式模式后行为与SVE2没有变化。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0426/22486ff178cc5a0.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>SME是一序列增强CPU构架对矩阵运算支持的最新更新，SME为支持矩阵运算引入了一个新的编程模式和寄存器状态。</p><p>SME是在可伸缩向量扩展（Scalable Vector Extensions， SVE和SVE2）的基础上建立的，并增加了有效处理矩阵的能力，主要功能包括：</p><ul class=" list-paddingleft-2"><li><p>矩阵tile的存储</p></li><li><p>存取，插入，提取 tile向量，包括on-the-fly 转置</p></li><li><p>计算SVE向量的外积（Outer product）</p></li><li><p>Streaming SVE 模式</p></li></ul><p>您可以在<a href="https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture">community.arm.com</a>了解更多关于Arm的SME。</p><p>除了Arm工程师为支持可伸缩矩阵扩展而进行的编译器方面的修改外，内核方面的修改也是必要的，这就是工程师一直在进行的工作，而且现在似乎已经为Linux 5.19做好了准备。</p><p>通过ARM64的Git仓库，现在的for-next/sme分支包含了Arm可伸缩矩阵扩展的内核启用工作。为了在未来带有该扩展的Arm CPU上启用SME支持/使用，需要进行各种内核修改。这也包括为新的流模式和现有的SVE代码的变化而暴露的ABI的文件，用于SME的使用。</p><p>现在，对可扩展矩阵扩展（SME）的基线支持已经存在，引入Kconfig选项以使其可以被构建。虽然功能注册没有对具有SME的系统在运行时支持SVE提出强制性要求，但对流模式SVE的支持却大多与普通SVE共享，因此其依赖于SVE。</p><p>除了需要这组SME补丁外，系统管理员还可以通过一个新的ARM64_SME构建时间开关来切换对SME扩展的支持。</p><p>如果没有任何问题在最后一刻出现，这个初始的Arm SME支持已经准备好在Linux 5.19主线中使用。</p>   
</div>
            