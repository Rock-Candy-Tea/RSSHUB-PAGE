
---
title: '研发知识：MDD、MDF是什么？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffc4741e25604b3eacc3c22101cd600d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 01:43:45 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffc4741e25604b3eacc3c22101cd600d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">MDD</h1>
<p>模型驱动开发 Model Driven Development（MDD）是一种<strong>以模型作为主要工件的高级别抽象的开发方法</strong>，是iuap平台下的元数据驱动设计框架，前后端的统一基于元数据的架构。模型在工具的支持下，作为核心资产被转换成代码或者可运行配置，可以<strong>降低开发成本，应对复杂需求变更。</strong></p>
<p><strong>MDD开发框架，是用友云针对企业数字化中台理念实现的一套开发框架</strong>。从企业云服务核心问题域出发，总结提炼出最佳实践，且形成了统一的标准及规约。致力于支撑中台能力快速孵化，形成中台各能力间连接的纽带，<strong>最终实现中台基础上的企业数字化业务重构及创新快速开发实现。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffc4741e25604b3eacc3c22101cd600d~tplv-k3u1fbpfcp-watermark.image" alt="MDD.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">MDF</h1>
<p>MDF框架（Model-Driven Framework）是一个<strong>基于元数据的模型驱动开发框架</strong>。它支持通过模式化的配置自动生成并渲染页面，继承了bpass业务中台的支撑服务和能力中心相关能力。Web开发和Mobile移动开发共用一套开发框架，共用一套扩展脚本，并<strong>支持不同维度的扩展开发</strong>（js扩展脚本、新增Metaui扩展组件、扩展及配置组件样式和交互等）。<strong>具有分层架构，分包解耦，架构灵活的特点。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb5212287b884c6bb0d4b81a99f20565~tplv-k3u1fbpfcp-watermark.image" alt="MDF整体架构.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">MDF框架开发特有名词</h2>
<p><strong>mdf-app</strong>：mdf前端框架的脚手架工程。</p>
<p><strong>mdf-metaui-web</strong>：mdf前端框架的核心UI组件包，包含UI组件和UI渲染引擎。</p>
<p><strong>mdf-cube</strong>：mdf前端框架核心前端公共逻辑和公共交互包，包含了对UI组件和View Model之间的双向绑定，模板页面前端公共逻辑（Action）。</p>
<p><strong>mdf-plugin-meta</strong>：脚手架运行时主要中间件（插件），主要为前后端之间各种服务的转发和前后端传输数据公共处理。</p>
<p><strong>ynpm</strong>：面向用友前端开发的npm包镜像仓库。</p>
<p><strong>View Model（VM）</strong>：视图模型，每一个基于模板开发的页面都有自己的视图模型，小到组件大到容器也都有自己对应的视图模型，即MVVM架构中视图模型。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66b9cc7be4744eaf8d49149b0126aeb9~tplv-k3u1fbpfcp-watermark.image" alt="MVVM.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            