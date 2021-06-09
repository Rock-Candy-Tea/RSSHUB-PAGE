
---
title: 'React 18 发布计划'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9451'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 20:16:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=9451'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>昨天 Vue 发了 3.1 的正式版，今天 React 发了 18 Alpha 版。</p>
<p>译文内容，还在校对中，给小伙伴们先睹为快。</p>
<p>原文：The Plan for React 18 - <a href="https://reactjs.org/blog/2021/06/08/the-plan-for-react-18.html" target="_blank" rel="nofollow noopener noreferrer">reactjs.org/blog/2021/0…</a></p>
<p>译文PR：<a href="https://github.com/reactjs/zh-hans.reactjs.org/pull/547" target="_blank" rel="nofollow noopener noreferrer">github.com/reactjs/zh-…</a></p>
</blockquote>
<p>React 团队非常激动地与你分享一些最新的工作进展：</p>
<ol>
<li>我们已经开始了 React 18 版本的工作，这将是我们的下一个主要版本。</li>
<li>我们创建了工作组，为社区逐步采用 React 18 的新特性做准备。</li>
<li>我们发布了 React 18 Alpha 版本，便于库作者尝试它并为我们提出相应反馈。</li>
</ol>
<p>目前这些更新主要面向第三方库的维护者。如果你正在学习、教学或使用 React 来构建面向用户的应用程序，你可以忽略此博客。但如果你出于好奇，我们同样欢迎你关注 React 18 工作组的讨论！</p>
<h2 data-id="heading-0">React 18 带来了什么</h2>
<p>当 React 18 发布时，它将包含开箱即用的改进（如 <a href="https://github.com/reactwg/react-18/discussions/21" title="automatic batching" target="_blank" rel="nofollow noopener noreferrer">automatic batching</a>)，全新的 API（如 <a href="https://github.com/reactwg/react-18/discussions/41" title="`startTransition`" target="_blank" rel="nofollow noopener noreferrer"><code>startTransition</code></a>）以及内置了支持 <code>React.lazy</code> 的 <a href="https://github.com/reactwg/react-18/discussions/37" title="全新 SSR 架构" target="_blank" rel="nofollow noopener noreferrer">全新 SSR 架构</a>。</p>
<p>这些功能之所以能够实现，要归功于我们在 React 18 中加入的全新且可选的 “并发渲染（concurrent rendering）” 机制。它使得 React 可以同时为多个 UI 做准备。这一变化主要在幕后，但它为 React 开启了新可能，以助你改善应用程序真实和感知的性能。</p>
<p>如果你一直在关注我们对 React 未来的研究（我们不希望你这样做！），你可能已经听说过一种 “并发模式（concurrent mode）” 的东西，使用它可能会破坏你的应用程序。为了回应社区这方面的反馈，我们重新设计了升级策略，以便大家渐进式升级。并且这种策略并非全有或全无的 “模式”，并发模式将只由某个新特性触发的更新而启用。在实践中，这意味着 <strong>你无需重写代码即可直接使用 React 18，并按需尝试新特性</strong>。</p>
<h2 data-id="heading-1">循序渐进的采用策略</h2>
<p>由于 React 18 中的并发性是可选功能，所以对于组件来说，并没有重大且开箱即用的突破性变化。<strong>你可以直接升级到 React 18，只需对你应用程序中的代码进行很少的改动，甚至无需任何改动，这与其他 React 主要版本的表现是一致的</strong>。根据我们将几个应用程序升级到 React 18 的经验来看，预计许多用户能在一个下午的时间内完成升级工作。</p>
<p>我们在 Facebook 成功地将并发功能交付给了数以万计的组件，根据我们的经验来看，我们发现大多数 React 组件 “正常工作”，无需额外的更改。我们致力于确保这对整个社区来说都是一次非常顺利的升级，所以今天我们宣布成立了 React 18 工作组。</p>
<h2 data-id="heading-2">与社区合作</h2>
<p>我们正在这个版本中尝试一些新的可能：我们邀请了来自整个 React 社区的专家、开发者、库作者和教育者参与我们的 <a href="https://github.com/reactwg/react-18" title="React 18 工作组" target="_blank" rel="nofollow noopener noreferrer">React 18 工作组</a>，以提供反馈，提出问题，甚至为该版本做贡献。我们无法邀请所有我们想邀请的人来参加这个最初的小团体，但如果实验成功，我们希望将来会有更多的人参与！</p>
<p><strong>React 18 工作组的目标是为生态做好准备，使现有的应用程序和库能够顺利、逐步地采用 React 18</strong>。该工作组托管在 <a href="https://github.com/reactwg/react-18/discussions" title="GitHub Discussions" target="_blank" rel="nofollow noopener noreferrer">GitHub Discussions</a>，以供公众阅读。工作组成员可以留下反馈，提出问题，并分享想法。核心团队也将使用 repo 的讨论区来分享我们的研究成果。随着稳定版的发布越来越近，任何重要的信息我们将在博客上发布。</p>
<p>欲了解关于升级到 React 18 的更多信息，或关于该版本的其他资源，请参阅 <a href="https://github.com/reactwg/react-18/discussions/4" title="React 18 公告" target="_blank" rel="nofollow noopener noreferrer">React 18 公告</a>.</p>
<h2 data-id="heading-3">访问 React 18 工作组</h2>
<p>大家可以在 <a href="https://github.com/reactwg/react-18" title="React 18 工作组仓库" target="_blank" rel="nofollow noopener noreferrer">React 18 工作组仓库</a> 中阅读相关讨论的情况。</p>
<p>我们预计对工作组感兴趣的小伙伴会激增，所以只有被邀请的成员可以创建或评论主题。然而，这些过程对公众是完全可见的，所以每个人都可以获得相同的信息，我们相信这是一个很好的折衷方案，既能为工作组成员创造一个富有成效的环境，又能保持对广大社区的透明度。</p>
<p>其他依旧，你可以在我们的 <a href="https://github.com/facebook/react/issues" title="issue" target="_blank" rel="nofollow noopener noreferrer">issue</a> 中提交错误报告、问题和反馈。</p>
<h2 data-id="heading-4">如何尝试 React 18 Alpha</h2>
<p>新的 alpha 版本通过 <a href="https://github.com/reactwg/react-18/discussions/9" title="`@alpha` 标签定期发布到 npm 中" target="_blank" rel="nofollow noopener noreferrer"><code>@alpha</code> 标签定期发布到 npm 中</a>。这些版本是由仓库的主分支的最新提交构建而来。当一个特性或 bug 修复被合并时，它将在下一个工作日出现在 alpha 版本中。</p>
<p>在 alpha 版本之间可能会有重大的变更或 API 变化。请谨记，<strong>alpha 版本不建议用于面向用户的生产应用中</strong>。</p>
<h2 data-id="heading-5">预计 React 18 的发布时间</h2>
<p>我们没有安排具体的发布时间，但我们预计需要几个月的反馈和迭代时间，React 18 才能做好准备，以应用于大多数生产项目。</p>
<ul>
<li>库的 Alpha 版本：今天可用</li>
<li>公开的 Beta 版：至少几个月</li>
<li>RC 版本：至少在 Beta 版发布后的几周</li>
<li>正式版：至少在 RC 版本发布之后的几周</li>
</ul>
<p>关于发布时间表的更多细节，<a href="https://github.com/reactwg/react-18/discussions/9" title="可以关注工作组" target="_blank" rel="nofollow noopener noreferrer">可以关注工作组</a>。当临近公开发布时，我们会在这个博客上发布更新。</p></div>  
</div>
            