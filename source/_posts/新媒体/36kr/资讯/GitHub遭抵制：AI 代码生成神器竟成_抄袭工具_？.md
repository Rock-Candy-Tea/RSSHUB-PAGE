
---
title: 'GitHub遭抵制：AI 代码生成神器竟成_抄袭工具_？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210707/v2_4d54108056b34950824ea4d760da90e0_img_000'
author: 36kr
comments: false
date: Wed, 07 Jul 2021 08:27:45 GMT
thumbnail: 'https://img.36krcdn.com/20210707/v2_4d54108056b34950824ea4d760da90e0_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/_cMQifZy7B3NiigmrrkxoQ">“CSDN”（ID:CSDNnews）</a>，作者：郑丽媛，36氪经授权发布。</p> 
<p>上周，<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>、GitHub、OpenAI 三方联手推出的<a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650852025&idx=1&sn=750a6ffa79d46699042cd545a02d7aa6&chksm=bd58bb6a8a2f327c1f5be28978f0816f63dbfbb7571da5d05f91079d5422a15571a0ca8c3812&scene=21#wechat_redirect">AI 代码生成神器 GitHub Copilot</a>一经官宣便引起巨大关注：试问哪个开发者不想要这么一位“虚拟程序员”来解放自己的双手？</p> 
<p>因此即使目前GitHubCopilot 处于并不完<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>技术预览版阶段，许多开发者们还是迫不及待地体验尝试。</p> 
<p>可这一试，试出问题来了：GitHubCopilot 生成的代码为何这么眼熟，就连注释都“原汁原味”，这是抄袭吗？</p> 
<h2>真 · 雷神之“锤”</h2> 
<p>其实有关 GitHub Copilot 直接复制代码的问题，微软早在官宣时就曾回应：“只有 0.1% 的情况下，GitHub Copilot 提供的代码建议中可能包含一些来自训练集的字符或片段。”</p> 
<p>但微软口中的这个“0.1% 的情况”，已经出现了。</p> 
<p>一位开发者 @mitsuhiko 在推特上公布了他的发现：让 GitHub Copilot 生成快速平方根倒数算法（Fast Inverse Square Root），结果出来的代码竟与《雷神之锤 3》中那段“传奇代码”一模一样！（注：快速平方根倒数算法也被称为平方根倒数速算法，此算法由于出现在《雷神之锤3》源代码中被人们所熟知。）</p> 
<p class="image-wrapper"><img data-img-size-val="562,269" src="https://img.36krcdn.com/20210707/v2_4d54108056b34950824ea4d760da90e0_img_000" referrerpolicy="no-referrer"></p> 
<p>这段代码无疑是“抄袭”：不仅包含了快速平方根倒数算法中至今都无人理解的神奇数字“0x5f3759df”，就连当年《雷神之锤 3》开发者对这串数字的吐槽都保留得“原汁原味”。</p> 
<p>如此一来，GitHub Copilot “抄袭代码”不仅实锤，还是真 · 雷神之“锤”，无法开脱，由此引发的代码版权问题也愈演愈烈。</p> 
<h2>GitHub Copilot 算是 GPL 协议中规定的衍生作品吗？</h2> 
<p>在 GitHub Copilot 直接复制快速平方根倒数算法这个过程中有个矛盾点，即这段代码是遵循 GNU GPL 2.0 协议进行开源的，而 GitHub Copilot 却要在未来扩展为付费服务提供。</p> 
<p>（注：GNU GPL 2.0 协议要求任何包含该开源许可证的衍生作品，即使仅有几行代码，也必须免费提供全部源代码以及修改和分发它们的权利。）</p> 
<p>在此基础上，就产生了一个巨大争议：这个现象表示 GitHub Copilot 在训练过程中必定使用过 GPL 协议下的代码，那么机器学习系统产生的作品，甚至机器学习系统本身，都算是 GPL 协议中规定的衍生作品吗？</p> 
<ul> 
 <li>如果答案是“否”，那是不是说明开发者可以利用 GitHub Copilot 来“清除”代码的 GPL 协议，从此再也无需遵循该协议？</li> 
 <li>如果答案是“是”，那么不仅 GitHub Copilot 应该免费开源，整个 GitHub 都要成为一个开源项目：据 GitHub 博客中“在 GitHub Copilot 的早期开发过程中，作为内部试用的一部分，近 300 名员工在日常工作中使用了它”的说法，这些员工很有可能已经将 GitHub Copilot 生成的代码整合到 GitHub 的方方面面，那么 GitHub 就也应该是个开源项目。</li> 
</ul> 
<p>为此，长期关注版权保护问题以及开源和自由软件的有力推动者 Julia Reda 写了一篇文章并坚定认为：GitHub Copilot 并未侵犯开发者的版权。</p> 
<p>她指出，简单地阅读和处理信息并不需要版权许可。举个例子，如果你去书店，从书架上拿一本书开始阅读，在这个过程中你是没有侵犯任何版权的，而人工智能这类数字技术的训练过程就是如此，它们需要大量内容数据。</p> 
<p>Julia Reda 在文中表示：“版权和数字技术之间的确因此会有许多冲突，所幸政策制定者和法院早就意识到：如果每个技术副本都需要许可，那么数字技术将完全无法发展使用。”</p> 
<p>早在 2001 年，欧盟就允许这种作为技术过程一部分的临时性复制行为不受版权限制，尽管当时反对的声音颇多。</p> 
<p>后来到 2019 年，欧盟研究协会更是要求欧洲版权法明确许可所谓的文本和数据挖掘，即永久存储受版权保护的作品以实现自动化分析。也就是说，根据欧洲版权法，无论使用何种许可协议，抓取 GPL 许可的代码或任何其他受版权保护的作品都是合法的。</p> 
<p>此外，Julia Reda 还认为机器自动生成的代码不能视为衍生作品：</p> 
<ul> 
 <li>首先，有人认为即使复制受版权保护作品的最小摘录也构成侵犯版权，这很不合理。按这种说法，就算不提 GitHub Copilot从训练数据中复制的短代码片段本来就不太可能达到原创标准，如果两个或多个开发人员在各自的程序中使用相同的基本代码，岂不是会产生无穷无尽的争议？</li> 
 <li>其次，版权法只适用于智力创作——没有创作者，就没有作品。也就是说像 GitHub Copilot 这样的机器生成代码根本不符合版权保护的条件，因此也并不是衍生作品。</li> 
</ul> 
<h2>争议颇多，甚至有开发者决定退出 GitHub</h2> 
<p>即便 Julia Reda 如此主张，但广大开发者对此并不买账。GitHub Copilot 的版权争议引发了很多人对 Github 的不满，甚至有开发者因此决定退出 GitHub：</p> 
<p>“我认为这是对版权持有人权利的严重侵犯，因此我不能继续依赖 GitHub 的服务。”</p> 
<p class="image-wrapper"><img data-img-size-val="601,425" src="https://img.36krcdn.com/20210707/v2_c7753d78c7624166939c8d934ef85b22_img_000" referrerpolicy="no-referrer"></p> 
<p>也有开发者批评 GitHub Copilot 将免费代码用作商业 AI 应用的资源：</p> 
<p>“GitHub Copilot 自己也承认，他们接受过大量 GPL 代码的训练，所以我不知道为什么这不是一种将开源代码转化为商业作品的形式。”</p> 
<p class="image-wrapper"><img data-img-size-val="516,433" src="https://img.36krcdn.com/20210707/v2_6249c0d1c56f45ed8ffe3244eff7a973_img_000" referrerpolicy="no-referrer"></p> 
<p>那么对此你有什么看法吗？</p> 
<h3>参考链接</h3> 
<ul> 
 <li>https://juliareda.eu/2021/07/github-copilot-is-not-infringing-your-copyright/</li> 
 <li>https://news.ycombinator.com/item?id=27736650</li> 
 <li>https://twitter.com/mitsuhiko/status/1410886329924194309</li> 
</ul>  
</div>
            