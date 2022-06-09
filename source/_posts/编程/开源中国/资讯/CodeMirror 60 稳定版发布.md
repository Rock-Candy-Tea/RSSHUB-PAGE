
---
title: 'CodeMirror 6.0 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8974'
author: 开源中国
comments: false
date: Thu, 09 Jun 2022 12:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8974'
---

<div>   
<div class="content">
                                                                                            <p>CodeMirror 是一款浏览器端代码编辑器，基于 Javascript，短小精悍，实时在线代码高亮显示，他不是某个富文本编辑器的附属产品，他是许多大名鼎鼎的在线代码编辑器的基础库。如今它发布了6.0稳定版本，该版本是从头进行的重写，在性能和可维护性上都有诸多改善。</p> 
<blockquote> 
 <p>CodeMirror 6是一个新的Web代码编辑器库，是基于过去13年构建和维护1至5版本的经验而从头开始实现的。它的目标是比以前的版本更具有可扩展性和可访问性。</p> 
 <p>到今天为止，6.0版本已经稳定。今后，可能至少在几年内，所有的新版本都将在6大版本之下，并向后兼容。</p> 
 <p>这个库已经可用了一年多，而且基本稳定，只有小的破坏性变化。我一般喜欢晚点发布，以避免有太多令人遗憾的错误溜进稳定版，然后不得不无限期地保留在那里。毫无疑问，在一年后的今天，我希望我以不同的方式发布，但通过让用户在生产中使用代码相当长的时间，很多小问题和摩擦的来源都被发现和解决了，然后才被定下来。</p> 
 <p>这个系统的工作是在四年前开始的，由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprototypefund.de%2Fen%2F" target="_blank">Prototype基金资助</a>初始工作。在那之后的一年里，它被公开宣布并得到了众筹，在那之后的两年里，它被建成了一个可使用的系统，并在去年得到了完善和稳定。在最初的两年里，我与Adrian Heine合作设计和实施了最初的系统。</p> 
 <p>关于新库的更多背景，请看关于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarijnhaverbeke.nl%2Fblog%2Flezer.html" target="_blank">Lezer</a>（分析器系统）、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarijnhaverbeke.nl%2Fblog%2Ffacets.html" target="_blank">facets</a>（扩展系统）和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarijnhaverbeke.nl%2Fblog%2Fcollaborative-editing-cm.html" target="_blank">协作编辑</a>的博文。对于整个系统的概述，请看系统指南。关于5.x以来接口变化的粗略总结，请看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodemirror.net%2F6%2Fdocs%2Fmigration%2F" target="_blank">迁移指南</a>。</p> 
 <p>——Marijn Haverbeke</p> 
</blockquote> 
<p>CodeMirror 6唯一打破向后兼容性的变化是@codemirror/basic-setup被重命名为codemirror，并且不再导出EditorState（你现在可以通过在EditorView构造函数的对象中内联EditorState.create的选项来创建视图，所以你不再需要它来设置一个最小的编辑器）。所有其他软件包应该与0.20.0完全兼容。</p>
                                        </div>
                                      
</div>
            