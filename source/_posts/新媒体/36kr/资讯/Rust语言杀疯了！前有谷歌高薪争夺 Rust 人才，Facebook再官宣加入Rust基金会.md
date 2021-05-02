
---
title: 'Rust语言杀疯了！前有谷歌高薪争夺 Rust 人才，Facebook再官宣加入Rust基金会'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210502/v2_e09fa6b0a2e24c0eb6509efc6cedb0e4_img_000'
author: 36kr
comments: false
date: Sun, 02 May 2021 05:00:13 GMT
thumbnail: 'https://img.36krcdn.com/20210502/v2_e09fa6b0a2e24c0eb6509efc6cedb0e4_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/s_HuD44SxjIE3y20hi8Mrg">“新智元”（ID:AI_era）</a>，作者：新智元，36氪经授权发布。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,608" src="https://img.36krcdn.com/20210502/v2_e09fa6b0a2e24c0eb6509efc6cedb0e4_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>  新智元报道  </strong></p> 
<p>来源：reddit</p> 
<p>编辑：小匀</p> 
<p><strong>【新智元导读】</strong>继 AWS、<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>、<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>、<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>和 Mozilla后，Facebook 近日也宣布加入 Rust 基金会，并承诺将会加大对 Rust 的采用。这个编程语言最近非常受青睐，相比较 C 和 C++ 而已更快速、更安全的它，对编写驱动程序和编译器等组件很有吸引力。</p> 
<p>近日，Facebook 宣布以最高级别 (Platinum Member) 的会员身份加入 Rust 基金会，与其他基金会成员<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210422/v2_9d94d5f89e394f8082c3b500e50c340d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>负责 Rust 开源生态以及社区的运作和发展。</p> 
<p class="image-wrapper"><img data-img-size-val="539,272" src="https://img.36krcdn.com/20210502/v2_d3fc5ed853594094808c104640b2092a_img_000" referrerpolicy="no-referrer"></p> 
<p>此外，Facebook 开源生态负责人 Joel Marcey 也加入了 Rust 基金会董事会。</p> 
<p class="image-wrapper"><img data-img-size-val="411,411" src="https://img.36krcdn.com/20210502/v2_aa1464df7b724e21be7698f2f86836ea_img_000" referrerpolicy="no-referrer"></p> 
<p>他表示：「自2016年以来，Facebook 就已开始使用 Rust，并应用在开发工作的各个领域——从源代码控制工具到编译器。加入 Rust 基金会，是为了帮助贡献、改进和发展这门对 Facebook 和世界各地的开发者来说已经变得非常有价值的语言。同时还希望 Rust 成为系统编程和其他领域的主流语言选择。」</p> 
<p>另外，Rust 基金会的临时执行董事 Ashley Williams 也对Facebook的加入表示欢迎，他说，Facebook 一直是 Rust 的坚定支持者，并说到 Joel 拥有广泛而多样的经验，从标准化组织到文档框架，这些业务能力都与现在的 Rust 发展有着密切的关联。</p> 
<p>那么这个Rust基金会到底什么来头？让我们先从Rust这门语言说起。</p> 
<p><strong>从小哥私人项目到Rust基金会，这门语言很「网红」</strong></p> 
<p>众所周知，Rust是一门专注于安全，尤其是并发安全，支持函数式和命令式以及泛型等编程范式的多范式语言，在语法上与C++类似。</p> 
<p class="image-wrapper"><img data-img-size-val="548,274" src="https://img.36krcdn.com/20210502/v2_4941a2e7403d45fa8f18d0301832f07d_img_000" referrerpolicy="no-referrer"></p> 
<p>Rust语言原本是Mozilla员工Graydon Hoare的私人计划，而Mozilla于2009年开始赞助这个计划，并且在2010年首次公开。</p> 
<p>也在同一年，其编译器源代码开始由原本的OCaml语言转移到用Rust语言，进行bootstrapping工作，称做「rustc」，并于2011年实际完成。这个可自我编译的编译器在架构上采用了LLVM作为它的后端。</p> 
<p class="image-wrapper"><img data-img-size-val="447,335" src="https://img.36krcdn.com/20210502/v2_e81a4bc570a74685a16aeaac4de991f7_img_000" referrerpolicy="no-referrer"></p> 
<p>Graydon Hoare，他在2009年成为Mozilla的雇员</p> 
<p>第一个有版本号的Rust编译器于2012年1月发布。Rust 1.0是第一个稳定版本，于2015年5月15日发布。</p> 
<p>在1.0稳定版之前，语言设计也因为透过撰写Servo网页浏览器排版引擎和rustc编译器本身，而有进一步的改善。虽然它由Mozilla资助，但它其实是一个共有项目，有很大部分的代码是来自于社区的贡献者。</p> 
<p>由于Rust是在完全开放的情况下进行开发，并且相当欢迎社区的反馈。长期以来，Rust都受到大批开发者的青睐。</p> 
<p>2021年2月8日，AWS、华为、Google、微软以及Mozilla宣布成立Rust基金会，并承诺在两年的时间里，投入 100 万美元的预算，用于 Rust 项目的开发、维护和推广。</p> 
<p class="image-wrapper"><img data-img-size-val="331,121" src="https://img.36krcdn.com/20210502/v2_c58a5228e63f48cd9719bbabee962b4b_img_000" referrerpolicy="no-referrer"></p> 
<p>其中，微软正在为Windows和Azure的一些组件探索Rust，而谷歌正在使用Rust构建Android操作系统的新部分，并支持将Rust引入Linux内核的努力。</p> 
<p class="image-wrapper"><img data-img-size-val="548,308" src="https://img.36krcdn.com/20210502/v2_2f08ab97846d46c6b54fe555eda592a1_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>Facebook的Rust身影</strong></p> 
<p>虽然Facebook已经以最高级别加入了Rust基金会，在该基金会的董事会中占有一席之地。 但Facebook现在只是通过其Novi数字钱包成为该协会的核心成员。、</p> 
<p>但整体而言，Rust之于Facebook，可以简单划分为几个时段。</p> 
<p><strong>2016–2017：尽早在源代码控制中使用</strong></p> 
<p>Facebook最早的Rust代码库可追溯到2016年，当时Facebook的monorepo中的源代码更改率开始侵蚀Mercurial源代码管理工具可以跟上的最大提交率。对此，Facebook的源代码管理团队启动了一个名为Mononoke的重写项目，其目标是将Mercurial的提交率提高几个数量级，以服务于Facebook的数千名开发人员和自动化流程。</p> 
<p>首先，用C ++开发Mononoke是显而易见的选择。当时，Facebook的后端代码库非常C ++，这意味着Mononoke默认情况下将用C ++实现。但是源控制团队需要考虑源控制后端的可靠性需求。当损坏或停机可能导致服务中断时，可靠性是重中之重。这就是为什么团队选择在C ++上使用Rust的原因。</p> 
<p>Mononoke项目的生产实践，证明了Rust值得进一步投资。并且，Rust帮助他们降低了Bug的成本。</p> 
<p><strong>2017–2019: 采用曲线</strong></p> 
<p>随着时间的推移，Mononoke作为其可行性和实践的证明，其他项目也考虑并采用了Rust。</p> 
<p>最初，这些通常是开发人员工具项目，不需要与更广泛的服务基础架构集成，或者是小型服务/守护程序，可以仅使用一些围绕C ++客户端库的手写包装来完成其工作。</p> 
<p>Facebook上许多采用Rust的工程师都来自Python和Javascript背景。</p> 
<p class="image-wrapper"><img data-img-size-val="548,365" src="https://img.36krcdn.com/20210502/v2_4593e6bbc3814a3ea14a2bdb76807241_img_000" referrerpolicy="no-referrer"></p> 
<p>Python在机器学习和后端系统开发方面很受欢迎，而JavaScript则统治着网络前端系统。  </p> 
<p>他们十分赞赏Rust，因此这门编程语言不仅性能高，而且编译时还有错误检测。</p> 
<p><strong>2019–2020年：对Rust的一些专门支持</strong></p> 
<p>从2017年到2019年，Source Control团队的人数增加了一倍，成为Facebook内非官方的Rust支持团队。到2019年，Facebook的Rust开发人员数量呈指数增长，超过了100个。</p> 
<p>作为这种增长的一个重要例子，Rust是Diem（以前称为Libra）区块链开发中的领先语言，由独立的Diem协会监督。Facebook通过其数字钱包Novi，成为Diem协会的会员。Diem区块链主要用Rust编写，覆盖了94％的开源代码库。</p> 
<p class="image-wrapper"><img data-img-size-val="548,354" src="https://img.36krcdn.com/20210502/v2_1cf70105d6ac44ef8029b1b8ad6a77bf_img_000" referrerpolicy="no-referrer"></p> 
<p>此外，与Rust一起开发了Move，一种用于区块链的新型安全编程语言。</p> 
<p><strong>2021年及以后</strong></p> 
<p>2020年底，Facebook成立了一个Rust团队，该团队由负责Facebook的C ++标准工作和工具链的同一组织负责。</p> 
<p class="image-wrapper"><img data-img-size-val="548,365" src="https://img.36krcdn.com/20210502/v2_d1c72fa993e2480b86c3692f967d7a0d_img_000" referrerpolicy="no-referrer"></p> 
<p>根据官网的介绍，在短期内，这个新团队专注于四个领域：</p> 
<p>1 从语言和工具链的角度为内部用户提供支持：这包括工具链的推出，跨领域迁移，代码审查/审核，最佳实践，并充当语言和工具链问题的联系点。</p> 
<p>2 在Facebook以外的社区中做出积极贡献：该团队执行标准库和编译器的代码审查，并为Rust社区的优先事项提供开发人员资源。</p> 
<p>3 Rust与C ++的轻松安全的互操作性：Facebook需要大量的C ++代码才能与构建服务的后端系统进行通信。</p> 
<p>Facebook需要开发人员能够安全，轻松地使用这些库，而又不牺牲Rust提供的好处。相反，如果Facebook想将Rust组件与更大的C ++二进制文件集成在一起，则需要异步代码中的智能运行时互操作性。</p> 
<p>Facebook的服务器高度分散且线程密集。Rust任务需要在C ++线程池上很好地发挥作用，并安全地共享同步原语和I / O资源。Facebook已经在C ++领域完成了大量工作，以改善异步性，已经支持并迅速采用了C ++ 20的协程。</p> 
<p>将Rust引入游戏将是对它的扩展，并将基于Rust异步库堆栈中已经发生的出色工作。</p> 
<p class="image-wrapper"><img data-img-size-val="548,308" src="https://img.36krcdn.com/20210502/v2_510fe1d172174166a193ef209c366688_img_000" referrerpolicy="no-referrer"></p> 
<p>4 积极支持和与Rust基金会互动：自2016年以来，Facebook一直致力于Rust社区并通过Rust扩展其发展。在加入Rust基金会后，Facebook表示希望一通推进Rust的发展，让其成为主流语言之一。</p> 
<p><strong>他们加入基金会说明了什么？</strong></p> 
<p>通过基金会的成员来看，除了最初的Mozilla，其他成员大多都和云有关系。</p> 
<p>一方面，Rust 的安全性使其适合写偏底层的软件，比如运行时。</p> 
<p>另外，Rust可能会在未来与Golang组CP——Rust负责底层部分，Go负责中间部分，共同服务上层各种语言的应用。</p> 
<p>参考资料：</p> 
<p>https://www.tectalk.co/rust-programming-language-we-want-to-take-it-into-the-mainstream-says-facebook/</p> 
<p>https://www.zhihu.com/question/443595816</p> 
<p>https://engineering.fb.com/2021/04/29/developer-tools/rust/</p>  
</div>
            